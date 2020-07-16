from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pygame
import sys
import clipboard

pygame.init()
clock= pygame.time.Clock()
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
base_font= pygame.font.Font(None, 32)
url = ''



running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                url = url[:-1]
            elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                url= clipboard.paste()
            elif event.key == pygame.K_RETURN:
                driver= webdriver.Chrome()
                driver.get("https://ytmp3.cc/en13/")
                convert = driver.find_element_by_xpath('//*[@id="submit"]')
                input_ = driver.find_element_by_xpath('//*[@id="input"]')
                input_.send_keys(url)
                input_.send_keys(Keys.RETURN)

                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Download"))
                    )
                    element.click()
                except: 
                    print(driver.page_source)

            else:    
                url += event.unicode
    screen.fill((0,0,0))
    text_suface= base_font.render(url, True, (255, 255, 255))
    screen.blit(text_suface, (0,0))  
    pygame.display.flip()
    clock.tick(60)



