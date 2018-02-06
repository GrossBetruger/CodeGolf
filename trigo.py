import math


def get_components(theta, scalar):
    theta_rads = math.radians(theta)
    x = math.cos(theta_rads) * scalar
    y = math.sin(theta_rads) * scalar
    return x, y


if __name__ == "__main__":
    V = get_components(80, 8)
    W = get_components(-35, 7)
    V_plus_W = V[0] + W[0], V[1] + W[1]
    print V
    print W
    print V_plus_W



