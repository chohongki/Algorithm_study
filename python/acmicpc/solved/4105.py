import sys
import math
input = sys.stdin.readline

while True:
    ax, ay, bx, by, cx, cy, dx, dy, ex, ey, fx, fy = map(float, input().split())

    if (ax == 0 and ay == 0 and bx == 0 and by == 0 and cx == 0 and cy == 0 and
    dx == 0 and dy == 0 and ex == 0 and ey == 0 and fx == 0 and fy == 0):
        break
    
    tri_A = abs(0.5 * (dx*ey + ex*fy + fx*dy - dy*ex -ey*fx - fy*dx))

    line_AB = ((bx-ax)**2 + (by-ay)**2)**0.5
    line_AC = ((cx-ax)**2 + (cy-ay)**2)**0.5

    # cosTheta = abs((cx-ax)*(bx-ax)+(cy-ay)*(by-ay))/(line_AB*line_AC)
    # h = tri_A / (line_AB * (1-cosTheta**2)**0.5)
    # hx = ax + (cx - ax) * h / line_AC
    # hy = ay + (cy - ay) * h / line_AC
    # gx, gy = (hx+(bx-ax)), (hy+(by-ay))

    h = tri_A / line_AB
    theta_AC = math.atan2(cy-ay, cx-ax)
    theta_AB = math.atan2(by-ay, bx-ax)
    theta_CAB = theta_AC-theta_AB
    hx = ax + abs(h/math.sin(theta_CAB))*math.cos(theta_AC)
    hy = ay + abs(h/math.sin(theta_CAB))*math.sin(theta_AC)
    gx, gy = (hx+(bx-ax)), (hy+(by-ay))

    print("%.3f %.3f %.3f %.3f" %(round(gx,3), round(gy,3), round(hx,3), round(hy,3)))
