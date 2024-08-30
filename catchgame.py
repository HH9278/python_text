import pygame
import random
import sys

# 初期化
pygame.init()

# 画面サイズの設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch Game")

# 色の定義
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# フォントの設定
font = pygame.font.SysFont(None, 55)

# バスケットの設定
basket_width = 100
basket_height = 20
basket_x = screen_width // 2 - basket_width // 2
basket_y = screen_height - basket_height - 10
basket_speed = 15

# アイテムの設定
item_width = 30
item_height = 30
item_x = random.randint(0, screen_width - item_width)
item_y = -item_height
item_speed = 5

# スコアの初期化
score = 0

# ゲームオーバー関数
def game_over():
    screen.fill(white)
    text = font.render("Game Over", True, red)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# スコア表示関数
def show_score(score):
    text = font.render(f"Score: {score}", True, black)
    screen.blit(text, (10, 10))

# ゲームループ
running = True
while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
        basket_x += basket_speed

    # アイテムの移動
    item_y += item_speed

    # アイテムが画面の下に到達した場合
    if item_y > screen_height:
        game_over()

    # アイテムがバスケットにキャッチされたかどうかの判定
    if (basket_x < item_x < basket_x + basket_width or basket_x < item_x + item_width < basket_x + basket_width) and basket_y < item_y + item_height < basket_y + basket_height:
        score += 1
        item_x = random.randint(0, screen_width - item_width)
        item_y = -item_height

    # バスケットとアイテムの描画
    pygame.draw.rect(screen, black, (basket_x, basket_y, basket_width, basket_height))
    pygame.draw.rect(screen, red, (item_x, item_y, item_width, item_height))

    # スコアの表示
    show_score(score)

    pygame.display.update()

    # フレームレートの設定
    pygame.time.Clock().tick(30)

pygame.quit()