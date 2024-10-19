# Python script to automate calculating pixel coordinates to court coordinates.

from dataclasses import dataclass

@dataclass
class Projection:
    pixel: int
    real: float

@dataclass
class Dimension:
    width: Projection
    height: Projection

# Front Court:
# - width:  6.4m  / 495px
# - height: 4.57m / 360px

# Back Court:
# - width:  6.4m / 1108px
# - height: 2.13 / 395px

front_dimensions = Dimension(Projection(495, 6.4), Projection(360, 4.57))
back_dimensions = Dimension(Projection(1108, 6.4), Projection(395, 2.13))

def calculate_real_point_front(point_px: list) -> list:
    x = round((point_px[0] * front_dimensions.width.real)  / front_dimensions.width.pixel,  2)
    y = round((point_px[1] * front_dimensions.height.real) / front_dimensions.height.pixel, 2)

    return [x, y]

def calculate_real_point_back(point_px: list) -> list:
    x = round((point_px[0] * back_dimensions.width.real)  / back_dimensions.width.pixel,  2)
    y = round((point_px[1] * back_dimensions.height.real) / back_dimensions.height.pixel, 2)

    return [x, y]

point_px_front = [11, 48]
point_px_back = [210, 63]

point_m_front = calculate_real_point_front(point_px_front)
point_m_back = calculate_real_point_back(point_px_back)
print(f"Back: {point_m_back}")
