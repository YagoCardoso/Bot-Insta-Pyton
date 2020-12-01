import os
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# postagem = input('Link da postagem: ')
postagem = "https://www.instagram.com/p/CDkPC3tpO_z/"
driver = webdriver.Firefox(executable_path=os.getcwd() + os.sep + 'geckodriver.exe')
driver.implicitly_wait(10)
driver.get(postagem)

btn_entrar = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[3]/div/span/a')
btn_entrar.click()

login = driver.find_element_by_xpath('//input[@name="username"]')
login.send_keys('yago.tenere')
#login.send_keys('ymcardoso_')
senha = driver.find_element_by_xpath('//input[@name="password"]')
#senha.send_keys('@%1010#')
senha.send_keys('@%1010#')
senha.send_keys(Keys.ENTER)
time.sleep(10)

agora_nao = driver.find_element_by_xpath('//button[@class="sqdOP yWX7d    y3zKF     "]')
agora_nao.click()
time.sleep(3)

barra = driver.find_element_by_xpath('//form[@class="X7cDz"]')

barra.click()
time.sleep(5)
# comentarios = ['um', 'dois', 'tres','quatro','cinco','seis','sete','oito','nove','dee','onze','doze','treze','quatorze','quinze']
comentarios = [
'@gaby_almeidas',
'@miika.santosss',
'@eijaine_',
'@lorrannethamyres',
'@eidudagomes',
'@falaai_joao',
'@analiarp_ ',
'@grazy_silv6 @xyasmym_',
'@daddy_issueees',
'@_vaaleriaval',
'@lidianeerod',
'@raissa_silva005', 
'@natmartinss',
'@taly_moreira',
'@_beatryzcabral',
'@_ferreiranatty',
'@kedynna_carmem',
'@martins_1987',
'@gab_santosgs',
'@eidudagomes',
'@juliaoliveiraalmeida_',
'@grazy_silv6',
'@aryane_christine',
'@batistasou_',
'@francielemaria285',
'@milledellahiva',
'@stephanigil',
'@daniisales_gomes',
'@analiarp_',
'@amy.santt',
'@xyasmym_',
'@im_triz',
'@anakmaestreloofc',
'@bmarinho30',
'@freitas.bukhttps',
'@brenda_canavarros',
'@francyele_27',
'@_juliavss',
'@noemecarmo456',
'@roberta_aguilar2020',
'@_feert_23',
'@_anaclara',
'@elyana.surf007',
'@ariih_015',
'@giselegq',
'@kiinha_erica',
'@babi_vit_ribeiro',
'@crisapfreire',
'@mariciteresinha',
'@fer_costahair',
'@rayla.arruda.7',
'@amandinha_nunes_15',
'@debora.cacheada231',
'@raquel_souz123',
'@rafaelsenatti',
'@karolinejoy93',
'@paullaalves02',
'@gledson.alan',
'@deiseviana37',
'@alexandra_s_martins',
'@guiomar.carvalho.9',
'@denisspeed_',
'@bobymuniz1970hotmail.co',
'@maianejl',
'@baglivo_danny_nunes',
'@edna4500',
'@william.galo',
'@jefersondesiderio1910',
'@angela_quarteto',
'@viictorbaltar',
'@luisarayra'
'@deysybrasil',
'@adrianazezza',
'@adrianinho_ramos',
'@gessykahgeovanna',
'@tamiresmatos53',
'@dold1978',
'@gonzalezmeli09',
'@awm_coelinho',
'@menteempresaria_',
'@anapauladasilva.siqueira',
'@eloisaame',
'@kemilly_233',
'@gleycialves098'
]
for comentario in comentarios:
    pyautogui.typewrite(comentario)
    # pyautogui.press('enter')
    # pyautogui.press('enter')
    pyautogui.click(1059,723)
    time.sleep(8)
    barra.click()
    time.sleep(960)

# x=1090 y=712

# pyautogui.typewrite(comentarios[0])
# time.sleep(2)
# pyautogui.click(1090,712)
