"""Generate simple coloured STEP models for the footprints that KiCad's stock 3D library doesn't cover.

Run with:  freecad.cmd /home/dbg-06/KiCAD/Rosie/libs/3d-generator/make_models.py
Output:    ../jlc.3dshapes/*.step

These are simplified models drawn from the manufacturers' datasheet outlines (not the manufacturers' own
CAD files): body size, height, pin positions and the main openings are right, small details are left out.
Coordinates below are written in the footprint editor's frame (mm, y down, z up, origin = footprint origin);
write_step() mirrors y into KiCad's 3D model frame.
"""
import os, re, math
import FreeCAD as App, Part, Import
from FreeCAD import Vector as V

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', 'jlc.3dshapes'))
os.makedirs(OUT, exist_ok=True)

BLACK = (0.10, 0.10, 0.11)
GREY = (0.45, 0.45, 0.47)
SILVER = (0.78, 0.78, 0.80)
TIN = (0.85, 0.85, 0.85)
GOLD = (0.85, 0.70, 0.25)
CREAM = (0.93, 0.90, 0.80)
BEIGE = (0.72, 0.68, 0.52)


def box(x0, x1, y0, y1, z0, z1):
    return Part.makeBox(x1 - x0, y1 - y0, z1 - z0, V(x0, y0, z0))


def cyl(x, y, z0, z1, r):
    return Part.makeCylinder(r, z1 - z0, V(x, y, z0))


def poly_prism(pts, z0, z1):
    w = Part.makePolygon([V(x, y, z0) for x, y in pts] + [V(pts[0][0], pts[0][1], z0)])
    return Part.Face(w).extrude(V(0, 0, z1 - z0))


def octagon(cx, cy, hx, hy, c, z0, z1):
    pts = [(cx - hx + c, cy - hy), (cx + hx - c, cy - hy), (cx + hx, cy - hy + c), (cx + hx, cy + hy - c),
           (cx + hx - c, cy + hy), (cx - hx + c, cy + hy), (cx - hx, cy + hy - c), (cx - hx, cy - hy + c)]
    return poly_prism(pts, z0, z1)


def write_step(name, parts):
    """parts = [(shape, (r, g, b)), ...] -> coloured STEP"""
    doc = App.newDocument(name)
    objs = []
    for i, (shape, _) in enumerate(parts):
        o = doc.addObject('Part::Feature', 'p%d' % i)
        # KiCad's 3D frame has +y pointing the opposite way to the footprint editor's y axis
        o.Shape = shape.mirror(V(0, 0, 0), V(0, 1, 0))
        objs.append(o)
    doc.recompute()
    path = os.path.join(OUT, name + '.step')
    Import.export(objs, path)
    App.closeDocument(doc.Name)
    # FreeCAD can't attach colours headless, so add STEP style entities per solid, in file order.
    txt = open(path).read()
    solids = [int(m) for m in re.findall(r'#(\d+)\s*=\s*MANIFOLD_SOLID_BREP', txt)]
    assert len(solids) == len(parts), (name, len(solids), len(parts))
    ids = [int(m) for m in re.findall(r'^#(\d+)\s*=', txt, re.M)]
    n = max(ids) + 1
    add = []
    for sid, (_, (r, g, b)) in zip(solids, parts):
        add += ["#%d=COLOUR_RGB('',%.4f,%.4f,%.4f);" % (n, r, g, b),
                "#%d=FILL_AREA_STYLE_COLOUR('',#%d);" % (n + 1, n),
                "#%d=FILL_AREA_STYLE('',(#%d));" % (n + 2, n + 1),
                "#%d=SURFACE_STYLE_FILL_AREA(#%d);" % (n + 3, n + 2),
                "#%d=SURFACE_SIDE_STYLE('',(#%d));" % (n + 4, n + 3),
                "#%d=SURFACE_STYLE_USAGE(.BOTH.,#%d);" % (n + 5, n + 4),
                "#%d=PRESENTATION_STYLE_ASSIGNMENT((#%d));" % (n + 6, n + 5),
                "#%d=STYLED_ITEM('',(#%d),#%d);" % (n + 7, n + 6, sid)]
        n += 8
    head, sep, tail = txt.rpartition('ENDSEC;')
    # the last ENDSEC; closes the DATA section
    open(path, 'w').write(head + '\n'.join(add) + '\n' + sep + tail)
    print('wrote', path, len(parts), 'solids')


# ---- Huaneng MLT-8530 SMD magnetic buzzer: 8.5 x 8.5 x 3.0, chamfered corners, sound port on top ----
def buzzer():
    c = 1.3
    h = 4.25
    body = octagon(0, 0, h, h, c, 0.0, 3.0)
    body = body.cut(cyl(0, 0, 2.4, 3.0, 0.8))          # sound port
    pads = [box(sx * 3.5 - 1.0, sx * 3.5 + 1.0, sy * 3.5 - 1.0, sy * 3.5 + 1.0, -0.02, 0.15)
            .fuse(box(sx * 4.25 - 0.05, sx * 4.25 + 0.05, sy * 3.5 - 0.8, sy * 3.5 + 0.8, 0.0, 1.0))
            for sx in (-1, 1) for sy in (-1, 1)]
    pads = [p for p in pads]
    parts = [(body, BLACK)]
    for p in pads:
        parts.append((p, TIN))
    write_step('Buzzer_Huaneng_MLT-8530', parts)


# ---- JST ZH B6B-ZR: top-entry header, 6 pins at 1.5 mm, body 10.5 x 3.5 x 5.6 ----
def zh():
    body = box(-1.5, 9.0, -1.3, 2.2, 0.0, 5.6)
    body = body.cut(box(-1.1, 8.6, -0.9, 1.8, 1.3, 5.6))   # mating cavity
    parts = [(body, CREAM)]
    for i in range(6):
        x = 1.5 * i
        parts.append((box(x - 0.15, x + 0.15, -0.25, 0.25, -1.6, 4.4), GOLD))
    write_step('JST_ZH_B6B-ZR_1x06_P1.50mm_Vertical', parts)


# ---- HRO TYPE-C-31-M-12 16-pin USB-C receptacle (front faces +y, 8.64 x 6.3 x 3.26) ----
def usbc():
    yb, yf, hz = -2.6, 3.7, 3.26
    shell = box(-4.32, 4.32, yb, yf, 0.0, hz)
    long_edges = [e for e in shell.Edges if abs(e.Vertexes[0].Point.x - e.Vertexes[1].Point.x) < 1e-6
                  and abs(e.Vertexes[0].Point.z - e.Vertexes[1].Point.z) < 1e-6]
    shell = shell.makeFillet(1.0, long_edges)               # rounded USB-C shell
    slot = box(-4.17, 4.17, yb + 0.5, yf + 0.1, 0.38, 2.88)
    shell = shell.cut(slot)
    tongue = box(-3.4, 3.4, yb + 0.5, yf - 0.9, 1.28, 1.98)
    parts = [(shell, SILVER), (tongue, BLACK)]
    # SMD contact tails on the pad row at y = -4.045
    tails = box(-3.7, 3.7, -4.77, yb + 0.1, 0.0, 0.2)
    parts.append((tails, GOLD))
    # through-hole shell tabs
    for sx in (-1, 1):
        parts.append((box(sx * 4.32 - 0.15, sx * 4.32 + 0.15, -3.13 - 0.7, -3.13 + 0.7, -1.6, 0.05), SILVER))
        parts.append((box(sx * 4.32 - 0.15, sx * 4.32 + 0.15, 1.05 - 0.4, 1.05 + 0.4, -1.6, 0.05), SILVER))
    write_step('USB_C_Receptacle_HRO_TYPE-C-31-M-12', parts)


# ---- XKB TS-1187A-B-A-B: 5.1 x 5.1 tact switch, 1.6 mm high, pads at +-3.0 / +-1.875 ----
def tact():
    base = box(-2.55, 2.55, -2.55, 2.55, 0.0, 0.5)
    cover = octagon(0, 0, 2.55, 2.55, 0.8, 0.5, 1.35)
    key = cyl(0, 0, 1.35, 1.6, 1.0)
    parts = [(base, BLACK), (cover, SILVER), (key, BLACK)]
    for sx in (-1, 1):
        for sy in (-1, 1):
            x0, x1 = (2.0, 3.25) if sx > 0 else (-3.25, -2.0)
            parts.append((box(x0, x1, sy * 1.875 - 0.375, sy * 1.875 + 0.375, 0.0, 0.3), TIN))
    write_step('SW_Push_1P1T_XKB_TS-1187A', parts)


# ---- ASMD1812 resettable fuse: 4.5 x 3.2 x about 1.9, end caps 0.6 ----
def fuse():
    body = box(-1.65, 1.65, -1.6, 1.6, 0.0, 1.9)
    parts = [(body, BEIGE)]
    for sx in (-1, 1):
        x0, x1 = (1.65, 2.25) if sx > 0 else (-2.25, -1.65)
        parts.append((box(x0, x1, -1.6, 1.6, 0.0, 1.9), TIN))
    write_step('Fuse_1812_4532Metric', parts)


buzzer()
zh()
usbc()
tact()
fuse()
