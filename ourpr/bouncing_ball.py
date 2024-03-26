
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# Ball properties
class Ball:

  def __init__(self, x, y, radius, color, speed):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.speed = speed
    self.direction = [1, 1]  # initial direction

  def move(self):
    self.x += self.speed * self.direction[0]
    self.y += self.speed * self.direction[1]

  def draw(self):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

  def check_collision(self, other_ball):
    distance = math.sqrt((self.x - other_ball.x)**2 +
                         (self.y - other_ball.y)**2)
    if distance <= self.radius + other_ball.radius:
      return True
    return False

  def increase_radius(self):
    self.radius += 5


# Circle properties
circle_radius = min(WIDTH, HEIGHT) // 2 - 50
circle_center = (WIDTH // 2, HEIGHT // 2)

# Create two balls
ball1 = Ball(circle_center[0] - 100, circle_center[1], 30, RED, 2)
ball2 = Ball(circle_center[0] + 100, circle_center[1], 30, BLUE, 2)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
  screen.fill(WHITE)

  # Draw the circle
  pygame.draw.circle(screen, WHITE, circle_center, circle_radius, 2)

  # Move and draw the balls
  ball1.move()
  ball1.draw()
  ball2.move()
  ball2.draw()

  # Check collision between balls
  if ball1.check_collision(ball2):
    ball1.increase_radius()
    ball2.increase_radius()

  # Check if balls hit the boundary of the circle
  for ball in [ball1, ball2]:
    if ball.x - ball.radius <= circle_center[
        0] - circle_radius or ball.x + ball.radius >= circle_center[
            0] + circle_radius:
      ball.direction[0] *= -1
    if ball.y - ball.radius <= circle_center[
        1] - circle_radius or ball.y + ball.radius >= circle_center[
            1] + circle_radius:
      ball.direction[1] *= -1

  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.flip()
  clock.tick(60)

# Quit Pygame
pygame.quit()
