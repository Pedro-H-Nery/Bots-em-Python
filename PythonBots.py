from selenium import webdriver
import pyautogui
import time

def baixaArquivo():
    navegador = webdriver.Chrome()
    time.sleep(2)
    navegador.get('https://www.sigaa.ufpi.br/sigaa/verTelaLogin.do')
    time.sleep(2)
    navegador.find_element("xpath", '//*[@id="conteudo"]/div[3]/form/table[1]/tbody/tr[1]/td/input').send_keys('NaoSeSabe')
    navegador.find_element("xpath", '//*[@id="conteudo"]/div[3]/form/table[1]/tbody/tr[2]/td/input').send_keys('pedro13245')
    navegador.find_element("xpath", '//*[@id="conteudo"]/div[3]/form/table[1]/tfoot/tr/td/input').click()
    time.sleep(2)
    navegador.find_element("xpath", '//*[@id="turmas-portal"]/span/a').click()
    time.sleep(2)
    navegador.find_element("xpath", '//*[@id="j_id_jsp_666485952_2"]/table/tbody/tr[33]/td[6]/a/img').click()
    time.sleep(2)
    navegador.find_element("xpath", '//*[@id="formAva:j_id_jsp_1010201818_236:0:listaMateriais:1:idInserirMaterialArquivo"]').click()
    time.sleep(3)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('CG.a01 -  Plano de Ensino (Slides)')
    time.sleep(1)
    pyautogui.press('enter')

def baixaNotas():
    navegador = webdriver.Chrome()
    time.sleep(2)
    navegador.get('https://www.sigaa.ufpi.br/sigaa/verTelaLogin.do')
    time.sleep(2)
    navegador.find_element("xpath", '//*[@id="conteudo"]/div[3]/form/table[1]/tbody/tr[1]/td/input').send_keys('NaoSeSabe')
    navegador.find_element("xpath", '//*[@id="conteudo"]/div[3]/form/table[1]/tbody/tr[2]/td/input').send_keys('pedro13245')
    navegador.find_element("xpath", '//*[@id="conteudo"]/div[3]/form/table[1]/tfoot/tr/td/input').click()
    time.sleep(2)
    navegador.find_element("xpath", '//*[@id="j_id_jsp_1325243614_229:detalharIndiceAcademico"]').click()
    time.sleep(2)

    pyautogui.hotkey('ctrl','p')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('Notas e Ira')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.press('win')
    time.sleep(2)
    pyautogui.write('Notas e Ira.pdf')
    time.sleep(1)
    pyautogui.press('enter')

def baixaMusicas(link, inicio, fim):
    pyautogui.press('win')
    time.sleep(2)
    pyautogui.write('4K Video Downloader')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(7)
    navegador = webdriver.Chrome()
    time.sleep(2)
    navegador.get(link)
    time.sleep(7)
    pyautogui.moveTo(980,330)
    time.sleep(1)
    pyautogui.scroll(-20000)
    time.sleep(3)
    for i in range(inicio,fim+1):
        x = navegador.find_element("xpath", '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer['+str(i)+']/div[2]/div[1]/div/h3/a').get_attribute('href')
        print(x)
        time.sleep(1)
        pyautogui.hotkey('alt','tab','tab')
        pyautogui.moveTo(1300,670)
        pyautogui.scroll(-1000)
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(380,670)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl','c')
        time.sleep(1)
        pyautogui.hotkey('alt','tab', 'tab')
        time.sleep(1)
        pyautogui.click(70,120)
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(30)
        pyautogui.click(410,510)
        time.sleep(1)
        pyautogui.hotkey('alt','tab', 'tab')
        time.sleep(1)
    pyautogui.hotkey('alt','tab')
    time.sleep(10)
    pyautogui.moveTo(285,175)
    pyautogui.click(button='right')
    time.sleep(2)
    pyautogui.click(340,205)
    time.sleep(2)
    pyautogui.click(535,60)
    

baixaMusicas('https://www.youtube.com/playlist?list=PL9XwASb-SpAP8gUTgr90l7L-Muy5aDtaw',1,135)