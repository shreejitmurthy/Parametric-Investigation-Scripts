# Python script to find the parametric equation through 2 points

from dataclasses import dataclass

g = 9.81

@dataclass
class Position:
    x: float
    y: float
    z: float

@dataclass
class VelocityArgs:
    T: float
    initial: Position
    final: Position


@dataclass
class VelocityReturn:
    vx: float
    vy: float
    vz: float

# General form of a 3-D parametric equation passing through two points
xt = "vxt + x0"
yt = "vyt + y0"
zt = "-1/2*(9.81)t^2 + vzt + z0"

# Calculating velocities
def vx(T: float, x_initial: float, x_final: float):
    v = (x_final - x_initial) / T
    return round(v, 3)

def vy(T: float, y_initial: float, y_final: float):
    v = (y_final - y_initial) / T
    return round(v, 3)

def vz(T: float, z_initial: float, z_final: float):
    v = (z_final-z_initial + (0.5 * g * T**2)) / T
    return round(v, 3)

# Combining all components
def velocity(args: VelocityArgs) -> VelocityReturn:
    return VelocityReturn(vx(args.T, args.initial.x, args.final.x), 
                          vy(args.T, args.initial.y, args.final.y), 
                          vz(args.T, args.initial.z, args.final.z))

args   = VelocityArgs(T=0.28,
                      initial=Position(0,9.75,0.61),
                      final=Position(0.48,8.78,0))
result = velocity(args)

replacements = {
    "x0": str(args.initial.x), "vx": str(result.vx),
    "y0": str(args.initial.y), "vy": str(result.vy),
    "z0": str(args.initial.z), "vz": str(result.vz)
}

for old, new in replacements.items():
    xt = xt.replace(old, new)
    yt = yt.replace(old, new)
    zt = zt.replace(old, new)

geogebra_command = f"Curve({xt}, {yt}, {zt}, t, 0, {args.T})"

print(geogebra_command)
