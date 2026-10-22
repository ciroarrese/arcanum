"""Blockout 3D de la Sede 1 (La Boca del Subte) para usar como guía de composición y luz.

Uso (desde esta carpeta, con el módulo bpy 5.2 instalado: pip install bpy==5.2.2):
    python sede1_blockout.py cartas sede1_render.png 128
"""
import math
import sys

import bpy
from mathutils import Vector

CARDS_DIR, OUT = sys.argv[1], sys.argv[2]
SAMPLES = int(sys.argv[3]) if len(sys.argv) > 3 else 96

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene


def mat(name, color, rough=0.8, emit=None, strength=0.0, metal=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if emit:
        b.inputs["Emission Color"].default_value = (*emit, 1)
        b.inputs["Emission Strength"].default_value = strength
    return m


def box(name, loc, size, material, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(location=loc, rotation=rot)
    o = bpy.context.object
    o.name = name
    o.scale = (size[0] / 2, size[1] / 2, size[2] / 2)
    o.data.materials.append(material)
    return o


def cyl(name, loc, r, h, material, rot=(0, 0, 0), verts=24):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=loc, rotation=rot)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(material)
    return o


def sphere(name, loc, r, material):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc, segments=24, ring_count=12)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    return o


# Materiales: la paleta de la Sede 1 (sodio, ladrillo, plástico, frazada)
M = {
    "asphalt": mat("asfalto", (0.03, 0.035, 0.04), rough=0.25),
    "curb": mat("cordon", (0.18, 0.18, 0.17), rough=0.7),
    "brick": mat("ladrillo", (0.09, 0.035, 0.03), rough=0.9),
    "brick2": mat("ladrillo2", (0.07, 0.03, 0.028), rough=0.9),
    "facade": mat("fachada", (0.05, 0.05, 0.06), rough=0.9),
    "window": mat("ventana", (0.1, 0.07, 0.02), emit=(1.0, 0.62, 0.25), strength=0.8),
    "crate": mat("cajon", (0.45, 0.04, 0.03), rough=0.5),
    "blanket": mat("frazada", (0.16, 0.11, 0.2), rough=1.0),
    "rail": mat("baranda", (0.12, 0.16, 0.12), rough=0.4, metal=0.8),
    "globe": mat("globo", (0.1, 0.4, 0.15), emit=(0.25, 0.9, 0.35), strength=0.6),
    "sign": mat("cartel", (0.85, 0.82, 0.72), rough=0.6),
    "ink": mat("tinta", (0.02, 0.02, 0.02), rough=0.6),
    "can": mat("lata", (0.5, 0.52, 0.55), rough=0.35, metal=0.9),
    "wax": mat("cera", (0.9, 0.85, 0.7), rough=0.5),
    "flame": mat("llama", (1, 0.7, 0.3), emit=(1.0, 0.65, 0.25), strength=40),
    "coffee": mat("cafe", (0.12, 0.2, 0.42), rough=0.5),
    "trash": mat("tacho", (0.16, 0.18, 0.16), rough=0.5, metal=0.6),
    "lamp": mat("farola", (0.05, 0.05, 0.05), rough=0.6),
    "sodium": mat("sodio", (1, 0.5, 0.1), emit=(1.0, 0.45, 0.08), strength=30),
    "client": mat("cliente", (0.35, 0.35, 0.33), rough=0.9),
    "paper": mat("diario", (0.7, 0.68, 0.6), rough=0.9),
}

# Suelo: vereda mojada y calle
box("vereda", (0, 2, -0.05), (14, 12, 0.1), M["curb"])
box("calle", (0, 8.6, -0.06), (30, 3, 0.1), M["asphalt"])

# Paredes de ladrillo a los costados (encuadran como "abertura" la boca del subte y la calle)
box("pared_izq", (-2.6, 2.5, 2), (0.4, 7, 4), M["brick"])
box("pared_der", (2.6, 2.5, 2), (0.4, 7, 4), M["brick2"])
for i in range(16):  # juntas de ladrillo como líneas oscuras
    z = 0.25 * i + 0.1
    box(f"junta_i{i}", (-2.39, 2.5, z), (0.02, 7, 0.02), M["ink"])
    box(f"junta_d{i}", (2.39, 2.5, z), (0.02, 7, 0.02), M["ink"])

# Fachadas del fondo con ventanas encendidas
for x, w, h in [(-6, 3, 9), (-2.5, 3.2, 12), (1.2, 3, 10), (4.8, 3.4, 13)]:
    box(f"edif_{x}", (x, 11.5, h / 2), (w, 1.5, h), M["facade"])
    for row in range(int(h // 1.4)):
        for col in range(3):
            if (row * 3 + col + int(x)) % 3:  # no todas encendidas
                continue
            box(f"vent_{x}_{row}_{col}", (x - w / 3 + col * w / 3, 10.7, 1 + row * 1.4), (0.35, 0.05, 0.5), M["window"])

# Boca del subte: hueco de escalera con barandas, dos postes con globos verdes y cartel
box("hueco", (0, 4.6, -0.04), (2.0, 2.4, 0.12), M["ink"])
for x in (-1.05, 1.05):
    cyl(f"baranda_{x}", (x, 4.6, 0.95), 0.03, 2.4, M["rail"], rot=(math.radians(90), 0, 0))
    for y in (3.5, 4.6, 5.7):
        cyl(f"parante_{x}_{y}", (x, y, 0.47), 0.025, 0.95, M["rail"])
    cyl(f"poste_{x}", (x, 3.45, 0.9), 0.04, 1.8, M["rail"])
    sphere(f"globo_{x}", (x, 3.45, 1.9), 0.16, M["globe"])
box("cartel", (0, 5.9, 2.75), (1.9, 0.08, 0.36), M["sign"])
bpy.ops.object.text_add(location=(0, 5.84, 2.67), rotation=(math.radians(90), 0, 0))
t = bpy.context.object
t.data.body = "SUBWAY"
t.data.align_x = "CENTER"
t.data.size = 0.24
t.data.extrude = 0.005
t.data.materials.append(M["ink"])

# Farola de sodio detrás, a la derecha
cyl("farola_poste", (1.9, 7.4, 2.2), 0.06, 4.4, M["lamp"])
box("farola_brazo", (1.6, 7.4, 4.35), (0.7, 0.08, 0.08), M["lamp"])
sphere("farola_luz", (1.3, 7.4, 4.25), 0.12, M["sodium"])
bpy.ops.object.light_add(type="POINT", location=(1.3, 7.4, 4.1))
bpy.context.object.data.energy = 350
bpy.context.object.data.color = (1.0, 0.55, 0.18)
bpy.context.object.data.shadow_soft_size = 0.3

# Utilería de vereda
cyl("tacho", (2.05, 1.9, 0.45), 0.3, 0.9, M["trash"])
box("diario_pegado", (-2.38, 1.6, 1.4), (0.02, 0.7, 0.9), M["paper"], rot=(math.radians(4), 0, 0))

# Cliente: maniquí de posición (el personaje final es 2D). Sentado en un balde, de frente.
cyl("balde", (0, 1.15, 0.2), 0.2, 0.4, M["can"])
cyl("torso", (0, 1.15, 0.72), 0.26, 0.65, M["client"])
sphere("cabeza", (0, 1.15, 1.22), 0.15, M["client"])

# Mesa del jugador: dos cajones de leche con una frazada encima
for x in (-0.36, 0.36):
    box(f"cajon_{x}", (x, 0.25, 0.17), (0.7, 0.36, 0.34), M["crate"])
    for k in range(4):  # ranuras del cajón
        box(f"ranura_{x}_{k}", (x - 0.24 + k * 0.16, 0.069, 0.17), (0.08, 0.01, 0.18), M["ink"])
box("frazada", (0, 0.25, 0.345), (1.5, 0.48, 0.02), M["blanket"])

# Cartas reales de 1909 sobre la frazada (Tres Tiempos)
for i, name in enumerate(["priestess_s.jpg", "tower_s.jpg", "fool_s.jpg"]):
    bpy.ops.mesh.primitive_plane_add(size=1, location=(-0.24 + i * 0.24, 0.24, 0.357))
    c = bpy.context.object
    c.scale = (0.085, 0.145, 1)
    cm = bpy.data.materials.new(f"carta_{i}")
    cm.use_nodes = True
    tex = cm.node_tree.nodes.new("ShaderNodeTexImage")
    tex.image = bpy.data.images.load(f"{CARDS_DIR}/{name}")
    cm.node_tree.links.new(tex.outputs["Color"], cm.node_tree.nodes["Principled BSDF"].inputs["Base Color"])
    cm.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.7
    c.data.materials.append(cm)

# Vela: cabo en una lata, a la derecha del jugador
cyl("lata_vela", (0.62, 0.2, 0.41), 0.06, 0.11, M["can"])
cyl("vela", (0.62, 0.2, 0.5), 0.025, 0.1, M["wax"])
sphere("llama", (0.62, 0.2, 0.57), 0.012, M["flame"])
bpy.ops.object.light_add(type="POINT", location=(0.62, 0.2, 0.6))
bpy.context.object.data.energy = 18
bpy.context.object.data.color = (1.0, 0.6, 0.25)
bpy.context.object.data.shadow_soft_size = 0.02

# Lata de café con monedas (la "caja" de la sede), a la izquierda
cyl("lata_cafe", (-0.62, 0.22, 0.43), 0.06, 0.15, M["coffee"])

# Invariante de legibilidad: luz motivada por la vela que garantiza cara y mesa como lo más claro
bpy.ops.object.light_add(type="SPOT", location=(0.45, -0.3, 0.85))
key = bpy.context.object
key.data.energy = 55
key.data.spot_size = math.radians(42)
key.data.spot_blend = 0.6
key.data.shadow_soft_size = 0.15
key.data.color = (1.0, 0.68, 0.38)
key.rotation_euler = (Vector((0, 1.15, 1.05)) - key.location).to_track_quat("-Z", "Y").to_euler()

# Luz de recorte fría y mínima para separar al cliente del fondo
bpy.ops.object.light_add(type="AREA", location=(-0.9, 2.4, 1.8))
rim = bpy.context.object
rim.data.energy = 6
rim.data.size = 0.8
rim.data.color = (0.55, 0.7, 1.0)
rim.rotation_euler = (Vector((0, 1.15, 1.0)) - rim.location).to_track_quat("-Z", "Y").to_euler()

# Mundo: noche fría
world = bpy.data.worlds.new("noche")
world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.008, 0.011, 0.02, 1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 1.0
scene.world = world

# Cámara en primera persona: sentado en la vereda, mirando por encima de la mesa
bpy.ops.object.camera_add(location=(0, -1.15, 1.05))
cam = bpy.context.object
cam.data.lens = 22
cam.rotation_euler = (Vector((0, 2.0, 0.95)) - cam.location).to_track_quat("-Z", "Y").to_euler()
cam.rotation_euler.x -= math.radians(8)
scene.camera = cam

scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = SAMPLES
scene.cycles.use_denoising = True
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.view_settings.view_transform = "AgX"
scene.view_settings.look = "AgX - Medium High Contrast"
scene.render.filepath = OUT
bpy.ops.render.render(write_still=True)
print("OK", OUT)
