import os
from time import strftime, timezone

import discord
import validators
from discord import guild
from discord.ext import commands
import requests
import random
from datetime import datetime, date, timedelta
import locale
from discord.utils import get

intents = discord.Intents.default()  # or .all() if you ticked all, that is easier
intents.members = True  # If you ticked the SERVER MEMBERS INTENT
client = commands.Bot(command_prefix=".", intents=intents)  # "Import" the intents

locale.setlocale(category=locale.LC_ALL, locale='fr_FR.utf8')

# liste des donjons
listDonjons = [
    ["https://i.ytimg.com/vi/SOMdH1dWt4o/hqdefault.jpg", "1", "Kardorim"],
    ["https://lh3.googleusercontent.com/4AWeBSifWK9gt_nFT7BoV5yYtBRyW8-TKcSJy9xk_A7aSeH_7Ofbct5EaXU5M0flMCD6l5pOjKymu716zrcwj1LFNkQbI884CriQUnP8CQ", "1", "Tournesol Affamé"],
    ["https://lh3.googleusercontent.com/c0Zh3gQj6Lb8slyEgO-4pDq8pkboRetvmkiL0LPqjbf1xyqX_KnNmed3SZi3Y-KUYZvMDAMoSjYqmBIzre5OBDMiKL1A23bExJYxkvS_fA", "1", "Mob l'Éponge"],
    ["https://jolstatic.fr/upload/dofus/Bouftous/bouftouroyal.png", "1", "Bouftou Royal"],
    ["https://static1.millenium.org/articles/1/30/60/31/@/621523-3945-article_m-1.png", "1", "Kankreblath"],
    ["https://jolstatic.fr/dofus/equipe/472077/articles/maisonFantome/boostache.jpg", "1", "Boostache"],
    ["https://static.wikia.nocookie.net/bestiaire-dofus/images/b/bd/Scaraboss_dor%C3%A9.jpg/revision/latest/scale-to-width-down/200?cb=20110502094859&path-prefix=fr", "1", "Scarabosse Doré"],
    ["https://ekladata.com/GhxCOWfkvaoogthxFEKCGRyVVx8.jpg", "1", "Batofu"],
    ["https://jolstatic.fr/attachments/0/4/734/4/ZmYxNWM0Nzc4OGJmMTA5NzM4NjczZDRlMmYzMGI5YmU/chafer11.png", "1", "Chafer Rönin"],
    ["https://doflex.fr/s/npcs/png/ba710cdcde62e2cbab2e54e06a3a7456.png", "1", "Grunob"],
    ["https://lh3.googleusercontent.com/Yt0c4LmBy8lVaAc0YT_8Cya3lVf-Erh1mWmlLmJWmNtexzccKuhW2MiWmt2ASjYVir1Nhn94ZChcAtjbPLDeIfYQAgHQGsJqa-d0Un-n", "1", "Bworkette"],
    ["https://lh3.googleusercontent.com/M8HTuBhpzVL8MY3GvdDs3EqMLRmKcjfZhnZ8TuSM2k9FmO8EDRf-f5_PcJRJkoH4LEbEOSt__LRvZdQzf7uYg_VOy9RA0HUqNqqYJZWh", "1", "Coffre des Forgerons"],
    ["https://guidedofus.com/wp-content/uploads/2019/11/shin-larve.png", "1", "Shin Larve"],
    ["https://lh3.googleusercontent.com/hx8qudgPeJx7r41J-BS-OQNB5icRoAocC5cVp-z0bg-SMkv7cI9QUnY-9oZAi2tl-5Ed0FarPYrfkCYtoXD-D8n4i1mMhzp_-dI7KSTLPA", "1", "Corailleur Magistral"],
    ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4xiiX9v6G2nAcB7oimc70u_DxFTJs1f9zMA&usqp=CAU", "1", "Kwakwa"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj42-rakoopeur-sommaire_orig.jpg", "1", "Rakoopeur"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/a/a2/Wey_Wabbit.png/revision/latest?cb=20150210142231&path-prefix=fr", "2", "Wa wabbit"],
    ["https://lh3.googleusercontent.com/bu_Bhj2fFzmIXtUM9UYr97nElfG35glegASXngtK0Hmn2-w8zLxCQ3YA6_4ZV8nncCkTDtwNJ3_0qYIoEx5OLhdU_QyDuHM0wbTiRn01iA", "2", "Kanniboul Ebil"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/f/f5/Nelween.jpg/revision/latest?cb=20150515093119&path-prefix=fr", "2", "Nelween"],
    ["https://lh3.googleusercontent.com/xLpH0PzgWFmCihf52dpiP5CsLx1Dq3ZerFpg42RrFYarwVBZrT-WwQmSC2NLfyxd-n8oEFRH4sypOgBJwPWb710Mh2bJiKisAWff7_93_g", "2", "Gourlo le Terrible"],
    ["https://lh3.googleusercontent.com/Pf62RE_1Tc79BZT5LfZlybdkGrXl1XPA8WXODS9GcSJyOBmvhPBbOYWurmuudJknZW__-Z_mJOPpII0gcPjXzopdu0oeKZ7YcOZrtfhV", "2", "Craqueleur Légendaire"],
    ["https://static.wikia.nocookie.net/krosmoz/images/0/08/Draegnerys.png/revision/latest?cb=20210422191245&path-prefix=fr", "2", "Draegnerys"],
    ["https://lh3.googleusercontent.com/_lwfMvZQpJq1Q7YllE2Yg4JpqwdnCj9THoz4D_cbDRC1j_j1Ad9g_4y0SmvHqENmyq-wTvyV1iQfigG6jKeV-89ViaUQP-oNuQmkmw44Tg", "2", "Wa wobot"],
    ["https://static.wikia.nocookie.net/krosmoz/images/6/62/Mantiscore.png/revision/latest?cb=20210422203436&path-prefix=fr", "2", "Mantiscore"],
    ["https://static.wikia.nocookie.net/krosmoz/images/7/73/Reine_Ny%C3%A9e.jpg/revision/latest?cb=20210422211822&path-prefix=fr", "2", "Reine Nyée"],
    ["https://lh3.googleusercontent.com/PkaN9b6mdHCGOzZkOn4o4aQTRouTGOuQ5kx-JYtyZwUjFtECYLfe4glzwyC-bErwOpAxaAiqy0PH15oq7N6Qdpv4llM7wf1OuqsonOOGBQ", "2", "Abraknyde Ancestral"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/9/9b/Chouque.png/revision/latest?cb=20150902084023&path-prefix=fr", "2", "le Chouque"],
    ["https://jolstatic.fr/dofus/equipe/548763/donjons/MagikRiktus/Choudini.png", "2", "Choudini"],
    ["https://lh3.googleusercontent.com/hnz40FsMXCSnYLLU-ohNl8wznKgYp6WtP5ic1E4XcPQqSSGWaz5sjZ75vs2e2ml19M_dc7Q59Pid43VWAWwgwJ-4N1XDc70W5uGbnBI", "3", "Dragon Cochon"],
    ["https://lh3.googleusercontent.com/NYQE_d9mHOR49mX20HIrUSI4_aDnSSwusgu1CEZ1z9xpLt-GlqGxlSFLMfBP9xvIqBNZfkdUcUnT3jexTZIK1EZuliRfIxpH6u6iU8TX", "3", "Koulosse"],
    ["https://methodwakfu.com/wp-content/uploads/2019/11/Milkar_Image-1.png", "3", "Meulou"],
    ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmNWh-RIpkyet6dOTHGCCYmcF82A6NfMqVcA&usqp=CAU", "3", "Moon"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/e/e6/Dramak.png/revision/latest/scale-to-width-down/216?cb=20150120072036&path-prefix=fr", "3", "Maitre des Pantins"],
    ["https://jolstatic.fr/dofus/equipe/472077/articles/enutrosor/mallefisk/Monstres/mimikado.jpg", "3", "Malléfisk"],
    ["https://static.wikia.nocookie.net/krosmoz/images/f/fb/Kharnozor.png/revision/latest?cb=20210422201358&path-prefix=fr", "3", "Kharnozor"],
    ["https://lh3.googleusercontent.com/TZ_P2KyJ-2_bb-bK_T-G0vhG5nqPpe1AyttALW3TaFwtOPvei1lcJtgaiTN9bUrWXZZXyjoZo90UDAQt82HLlLiE1-Gg8gCWnNvba-oT", "3", "Silf le Rasboul Majeur"],
    ["https://lh3.googleusercontent.com/MEbuepNxF7zKecL_cFDthGeDjrqzoBiPH5LspipFilIzWjUKWjNZ699GiOt-0fKyWuwdhQ1KNibJza-cX7H0WQa9mhNlMuOafbjRuxLV", "3", "Maitre Corbac"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj21-rat-blanc-sommaire_orig.jpg", "3", "Rat Blanc"],
    ["939", "3", "Rat Noir"],
    ["https://lh3.googleusercontent.com/JptzmIPPG3ANJXCfrQXN79ngTDdzUIJcFBQc89h2X_FGdZFAYGQ5EA_N1T4buAxuh1AfVGRY2d9S2az9q_0lZRNy8V-LE5z2d7QZK3k", "3", "Pounicheur"],
    [
        "https://static.wikia.nocookie.net/dofus-rp/images/a/a1/Damadrya.webp/revision/latest?cb=20210407203650&path-prefix=fr",
        "3", "Damadrya"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/f/f9/BlopMR.png/revision/latest/scale-to-width-down/274?cb=20230224094657&path-prefix=fr", "3", "Blop Multicolore Royal"],
    ["https://lh3.googleusercontent.com/4nI6PlsVo7r-N3Us534HJsQzP9GLgJYoycXXQ6liv8imNh7Nu0p_2nwdyFE5EktOFiV3kvCSCPfcA_jP0I6Ur9g2pqw9NHCbb68cmsmmPA", "3", "Minotoror"],
    ["https://staticns.ankama.com/comm/news/dofus/www/03_2013/carrousel-relance-frigost.jpg", "3", "Royalmouth"],
    ["https://lh3.googleusercontent.com/sUrTP3k6q2Q9BkYan-XuT19b_oOlo0sgOe4mK766gi_1wemuxTmt2yuidsv4iyB3zzI2FJIltM_x72Anj9NIxL_OHxpvj2jsfJwGwPK7", "3", "Tofu Royal"],
    ["https://static.wikia.nocookie.net/dofus-wakfu/images/a/af/126.png/revision/latest?cb=20171126173825&path-prefix=fr", "3", "Crocabulia"],
    ["https://lh3.googleusercontent.com/rrOO2c_Po2S81OpblqubI-r6_kq8eaY-DhOTY-mxn3wGOn5PoYDrbatT7U31llpWw_YxUSSHT4fZO8snq7JagFHREBTMqnxnV7HNh40uvg", "3", "Skeunk"],
    ["https://lh3.googleusercontent.com/p9hDS68a3pyF216gHIlfGXGEyLWCK52TdH3WlRtBo8jxLXUu_bJrtfDGKI4oChZFZewEEICXojjgOVgJNB6shaE7khbgWCds4oMqUx6vjw", "3", "Fraktale"],
    ["https://lh3.googleusercontent.com/vD1CrELpHcoaW3hVGKtD5JoIlBhMwHy1xj4f1YMMgCth9cuEHPAUnPxVsavC4hTFA8SxHiH4POdA0uvAMm8p_nGzMI2LdjiORhUnOHc", "3", "Haute Truche"],
    ["https://static.wikia.nocookie.net/krosmoz/images/c/c2/El_Piko.jpg/revision/latest?cb=20210422191746&path-prefix=fr", "3", "El Piko"],
    ["https://lh3.googleusercontent.com/E9ygY-kPnuJ6ti-YR5Pc3zB3h3ZujXpksgGv0iEuNQ8uTNyizAztapKguBIz28a_rlT5RlGYHBUrqCBL-3IlilUwaL1in_1hfzh7xz7JzA", "3", "Capitaine Ekarlatte"],
    [
        "https://static.wikia.nocookie.net/krosmoz/images/c/cd/Nagate_la_Dame_des_eaux.png/revision/latest/top-crop/width/360/height/360?cb=20210422205010&path-prefix=fr",
        "3", "Nagate"],
    [
        "https://static.wikia.nocookie.net/krosmoz/images/1/16/Tanukou%C3%AF_San.png/revision/latest?cb=20210422214342&path-prefix=fr",
        "3", "Tanukoui San"],
    ["https://lh3.googleusercontent.com/rpKYNQ_kny-y0MgEbgyy7pvYeZ7KPPFw_EBw6CnvrbJX5kq-D_7BF2xOOPpdEhDQ8tInRaTHMzD8x7KWuEVGMILeseqKfA3WBVDPKh8", "3", "Chêne Mou"],
    ["https://lh3.googleusercontent.com/1wa8YqAfIUwSxlra7GJhjrj5gDt7LzV8Jdr8nThkaln8r-49ZMwd_IEbE2awnazUec0Whi1UgaOaxyTfP8DQpLWhZRMxHtWgj-G0f7FV", "3", "Tynril"],
    ["https://lh3.googleusercontent.com/BF8ZdcAY88qo76osVtB3rxXtKNjLW_gGlNe61H_ktdysQ6FqVDVsoeZVLoTTiCnYWaguiOmAxSiHuI3O6k5lwQTYKiRb_H59vwJwr_k9", "3", "Mansot Royal"],
    ["https://pbs.twimg.com/media/EqkmPb_W4AEjN-F?format=jpg&name=large", "3", "Hanshi et Shihan"],
    ["https://www.dofus.com/fr/mmorpg/encyclopedie/monstres/6249-founoroshi", "3", "Founoroshi"],
    ["https://staticns.ankama.com/comm/news/dofus/www/03_2013/carrouselbenleripate.jpg", "3", "Ben le Ripate"],
    ["https://4.bp.blogspot.com/-LZPwi-AuGiA/UntawkEc0AI/AAAAAAAAA6k/LsR3KzvPb3E/s1600/sphincter-cell.jpg", "3", "Sphincter Cell"],
    ["https://cdna.artstation.com/p/assets/images/images/019/912/544/large/yohan-baes-phossile.jpg?1565554176", "3", "Phossile"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/5/58/HellMina.png/revision/latest?cb=20220524080032&path-prefix=fr", "3", "Hell mina"],
    ["https://jolstatic.fr/dofus/equipe/548763/donjons/Kimbo/kimbo.png", "4", "Kimbo"],
    ["https://lh3.googleusercontent.com/ea3y5wRdEN1xz1HQcJ6tsA6GYEfCxFRbZAGsQddu3A01WokCICOz3lFu9-WIp627XSmpN3CSYUITlaqWdKtquI3_qVz8k4R2LRRZY40Z4A", "4", "Minotot"],
    ["https://static1.millenium.org/articles/5/14/25/75/@/44115-dofus-2018-11-23-23-02-14-hackh-article_image_t-2.png", "4", "Obsidiantre"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/7/74/Kanigroula2.jpg/revision/latest?cb=20230327085619&path-prefix=fr", "4", "Kanigroula"],
    ["https://static.wikia.nocookie.net/krosmoz/images/f/f4/Ush_Galesh_2.jpg/revision/latest?cb=20210422215414&path-prefix=fr", "4", "Ush Galesh"],
    [
        "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-shogun-tofugawa.png",
        "4", "Shogun"],
    ["https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRrvqh8B582nCuo1xP39qqc9Nh1fye3xDxVH6Omp6n9LLET5Fcm", "4", "Tengu Givrefoux"],
    ["https://lh3.googleusercontent.com/UoE8lqfRTd4-HYKD64MPdE-c2ApM8KKvm3IghluOoi_LqwWo1QJP2sOxMl_KHmXwjfZQ9KqFcSUuOodv67mngW5xMVU9hMbngPCa1hNk", "4", "Père Ver"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-xlii.png", "4", "XLII"],
    ["https://jolstatic.fr/dofus/equipe/412805/donjons/Koumiho/boss_2.png", "4", "Koumiho"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/a/a8/Hqdefault.jpg/revision/latest?cb=20190911141528&path-prefix=fr", "4", "Korriandre"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/9/94/Bworker.png/revision/latest?cb=20141007081701&path-prefix=fr", "4", "Bworker"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/f/f1/Ougah.png/revision/latest?cb=20150811203443&path-prefix=fr", "4", "Ougah"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj44-ensorcellement3_orig.jpg", "5", "Belladone"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/c/c5/Barb%C3%A9ryl.png/revision/latest?cb=20230103224045&path-prefix=fr", "5", "Barbéryl Clochecuivre"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj25-toxoliath-sommaire_orig.jpg", "5", "Toxoliath"],
    ["https://jolstatic.fr/dofus/equipe/412805/donjons/Kolosso/kolosso.png", "5", "Kolosso"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/wanted8-0fuji-givrefoux_orig.png", "5", "Fuji Givrefoux"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-grolloum.png", "5", "Grolloum"],
    ["https://i.skyrock.net/5018/84165018/pics/3111417225_1_3_OhfNxH9d.jpg", "5", "Glourséleste"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/a/a6/Ombre.png/revision/latest?cb=20150423133333&path-prefix=fr", "5", "Ombre"],
    ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh6qYhEXnH1sZPznpXVtrSt82JfDEA0Iw0GSogMjopqpk-InrLQ5tPDtkeFWHLgovldWY&usqp=CAU", "5", "Comte Razof"],
    ["https://static.wikia.nocookie.net/krosmoz/images/e/e8/Missiz_Frizz.jpg/revision/latest?cb=20210422204613&path-prefix=fr", "5", "Missiz Frizz"],
    ["https://static.wikia.nocookie.net/dofusrol/images/b/be/301_all_200_200.jpg/revision/latest/scale-to-width-down/250?cb=20130421021908", "5", "Sylargh"],
    ["https://www.eclypsia.com/wp-content/uploads/eclypsia/2022/12/klime.jpg", "5", "Klime"],
    ["https://jolstatic.fr/dofus/equipe/412805/donjons/Nileza/top-nileza.png", "5", "Nileza"],
    ["https://static.wikia.nocookie.net/krosmoz/images/2/2e/Illu_Comte_Harebourg.png/revision/latest?cb=20221107153510&path-prefix=fr", "5", "Comte Harebourg"],
    ["https://cdnb.artstation.com/p/assets/images/images/000/107/299/large/charlene-le-scanff-character-design-dofus-ankama-07.jpg?1403128496", "5", "Merkator"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/7/74/Nidas1.jpg/revision/latest?cb=20230128203518&path-prefix=fr", "5", "Roi Nidas"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/7/7c/RDV.png/revision/latest/scale-to-width-down/1200?cb=20230128212952&path-prefix=fr", "5", "Reine des Voleurs"],
    ["https://jolstatic.fr/dofus/equipe/412805/donjons/Baleine/protozorreur.png", "5", "Protozorreur"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/a/af/Vortex.webp/revision/latest?cb=20210513093405&path-prefix=fr", "5", "Vortex"],
    ["https://jolstatic.fr/dofus/equipe/412805/donjons/Chaloeil/chaloeil.png", "5", "Chaloeil"],
    ["https://static1.millenium.org/articles/1/28/88/51/@/312291-menook-article_cover_bd-6.png", "5", "Capitaine Meno"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-koutoulou.png", "5", "larve de Koutoulou"],
    ["https://i.ytimg.com/vi/0JTRNFH3Nko/maxresdefault.jpg", "5", "Dantinéa"],
    ["https://static.wikia.nocookie.net/krosmoz/images/0/07/Tal_Kasha.jpg/revision/latest?cb=20210422214254&path-prefix=fr", "5", "Tal kasha"],
    ["https://static.wikia.nocookie.net/krosmoz/images/0/0e/Annerice_la_Shushess.jpg/revision/latest?cb=20210422182109&path-prefix=fr", "5", "Anerice la Shushess"],
    ["https://cdn1.ankama-shop.com/3076-thickbox_default/affiche-ilyzaelle-relief-effet-dore.jpg", "5", "Ilyzaelle"],
    ["https://static.wikia.nocookie.net/krosmoz/images/a/a5/Solar.jpg/revision/latest?cb=20210422213823&path-prefix=fr", "5", "Solar"],
    ["https://static.wikia.nocookie.net/dofus-rp/images/1/1a/Bethel.png/revision/latest?cb=20171112215040&path-prefix=fr", "5", "Bethel Akarna"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj10-dazak-sommaire_orig.jpg", "5", "Dazak Martegel"],
    ["https://jolstatic.fr/dofus/equipe/412805/donjons/Torkelonia/torkelonia.png", "5", "Torkélonia"],
    [
        "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-corruption.png",
        "5", "Corruption"],
    ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgwukbMo2HBtgWYORFotBd30p-jYdzUE96Fw&usqp=CAU", "5",
     "Guerre"],
    ["https://jolstatic.fr/www/captures/93/4/141454.png", "5", "Servitude"],
    ["https://jolstatic.fr/dofus/equipe/412805/donjons/Misere/misere.png", "5", "Misère"],
    [
        "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-orukam.png",
        "5", "Roi imagami"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj19-amirukam-sommaire_orig.jpg", "5",
     "Reine Amirukam"],
    ["http://image.noelshack.com/fichiers/2022/36/7/1662902767-kabahal.png", "5", "Kabahal"],
    ["https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/cavaliers-eliocalypse-sommaire_orig.jpg", "5",
     "4 cavaliers"],  # 4 Cavaliers
    [
        "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-eternel-conflit.png",
        "5", "Eternel Conflit"]  # Eternel Conflit
]
donjonsDict = {
    "https://i.ytimg.com/vi/SOMdH1dWt4o/hqdefault.jpg": "1",  # Kardorim
    "https://lh3.googleusercontent.com/4AWeBSifWK9gt_nFT7BoV5yYtBRyW8-TKcSJy9xk_A7aSeH_7Ofbct5EaXU5M0flMCD6l5pOjKymu716zrcwj1LFNkQbI884CriQUnP8CQ": "1",  # Tournesol Affamé
    "https://lh3.googleusercontent.com/c0Zh3gQj6Lb8slyEgO-4pDq8pkboRetvmkiL0LPqjbf1xyqX_KnNmed3SZi3Y-KUYZvMDAMoSjYqmBIzre5OBDMiKL1A23bExJYxkvS_fA": "1",  # Mob l'Éponge
    "https://jolstatic.fr/upload/dofus/Bouftous/bouftouroyal.png": "1",  # Bouftou Royal
    "https://static1.millenium.org/articles/1/30/60/31/@/621523-3945-article_m-1.png": "1",  # Kankreblath
    "https://jolstatic.fr/dofus/equipe/472077/articles/maisonFantome/boostache.jpg": "1",  # Boostache
    "https://static.wikia.nocookie.net/bestiaire-dofus/images/b/bd/Scaraboss_dor%C3%A9.jpg/revision/latest/scale-to-width-down/200?cb=20110502094859&path-prefix=fr": "1",  # Scarabosse Doré
    "https://ekladata.com/GhxCOWfkvaoogthxFEKCGRyVVx8.jpg": "1",  # Batofu
    "https://jolstatic.fr/attachments/0/4/734/4/ZmYxNWM0Nzc4OGJmMTA5NzM4NjczZDRlMmYzMGI5YmU/chafer11.png": "1",  # Chafer Rönin
    "https://doflex.fr/s/npcs/png/ba710cdcde62e2cbab2e54e06a3a7456.png": "1",  # Grunob
    "https://lh3.googleusercontent.com/Yt0c4LmBy8lVaAc0YT_8Cya3lVf-Erh1mWmlLmJWmNtexzccKuhW2MiWmt2ASjYVir1Nhn94ZChcAtjbPLDeIfYQAgHQGsJqa-d0Un-n": "1",  # Bworkette
    "https://lh3.googleusercontent.com/M8HTuBhpzVL8MY3GvdDs3EqMLRmKcjfZhnZ8TuSM2k9FmO8EDRf-f5_PcJRJkoH4LEbEOSt__LRvZdQzf7uYg_VOy9RA0HUqNqqYJZWh": "1",  # Coffre des Forgerons
    "https://guidedofus.com/wp-content/uploads/2019/11/shin-larve.png": "1",  # Shin Larve
    "https://lh3.googleusercontent.com/hx8qudgPeJx7r41J-BS-OQNB5icRoAocC5cVp-z0bg-SMkv7cI9QUnY-9oZAi2tl-5Ed0FarPYrfkCYtoXD-D8n4i1mMhzp_-dI7KSTLPA": "1",  # Corailleur Magistral
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4xiiX9v6G2nAcB7oimc70u_DxFTJs1f9zMA&usqp=CAU": "1",  # Kwakwa
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj42-rakoopeur-sommaire_orig.jpg": "1", #Rakoopeur
    "https://static.wikia.nocookie.net/dofus-rp/images/a/a2/Wey_Wabbit.png/revision/latest?cb=20150210142231&path-prefix=fr": "2",  # Wa wabbit
    "https://lh3.googleusercontent.com/bu_Bhj2fFzmIXtUM9UYr97nElfG35glegASXngtK0Hmn2-w8zLxCQ3YA6_4ZV8nncCkTDtwNJ3_0qYIoEx5OLhdU_QyDuHM0wbTiRn01iA": "2",  # Kanniboul Ebil
    "https://static.wikia.nocookie.net/dofus-rp/images/f/f5/Nelween.jpg/revision/latest?cb=20150515093119&path-prefix=fr": "2",  # Nelween
    "https://lh3.googleusercontent.com/xLpH0PzgWFmCihf52dpiP5CsLx1Dq3ZerFpg42RrFYarwVBZrT-WwQmSC2NLfyxd-n8oEFRH4sypOgBJwPWb710Mh2bJiKisAWff7_93_g": "2",  # Gourlo le Terrible
    "https://lh3.googleusercontent.com/Pf62RE_1Tc79BZT5LfZlybdkGrXl1XPA8WXODS9GcSJyOBmvhPBbOYWurmuudJknZW__-Z_mJOPpII0gcPjXzopdu0oeKZ7YcOZrtfhV": "2",  # Craqueleur Légendaire
    "https://static.wikia.nocookie.net/krosmoz/images/0/08/Draegnerys.png/revision/latest?cb=20210422191245&path-prefix=fr": "2",  # Draegnerys
    "https://lh3.googleusercontent.com/_lwfMvZQpJq1Q7YllE2Yg4JpqwdnCj9THoz4D_cbDRC1j_j1Ad9g_4y0SmvHqENmyq-wTvyV1iQfigG6jKeV-89ViaUQP-oNuQmkmw44Tg": "2",  # Wa wobot
    "https://static.wikia.nocookie.net/krosmoz/images/6/62/Mantiscore.png/revision/latest?cb=20210422203436&path-prefix=fr": "2",  # Mantiscore
    "https://static.wikia.nocookie.net/krosmoz/images/7/73/Reine_Ny%C3%A9e.jpg/revision/latest?cb=20210422211822&path-prefix=fr": "2",  # Reine Nyée
    "https://lh3.googleusercontent.com/PkaN9b6mdHCGOzZkOn4o4aQTRouTGOuQ5kx-JYtyZwUjFtECYLfe4glzwyC-bErwOpAxaAiqy0PH15oq7N6Qdpv4llM7wf1OuqsonOOGBQ": "2",  # Abraknyde Ancestral
    "https://static.wikia.nocookie.net/dofus-rp/images/9/9b/Chouque.png/revision/latest?cb=20150902084023&path-prefix=fr": "2",  # le Chouque
    "https://jolstatic.fr/dofus/equipe/548763/donjons/MagikRiktus/Choudini.png": "2",  # Choudini
    "https://lh3.googleusercontent.com/hnz40FsMXCSnYLLU-ohNl8wznKgYp6WtP5ic1E4XcPQqSSGWaz5sjZ75vs2e2ml19M_dc7Q59Pid43VWAWwgwJ-4N1XDc70W5uGbnBI": "3",  # Dragon Cochon
    "https://lh3.googleusercontent.com/NYQE_d9mHOR49mX20HIrUSI4_aDnSSwusgu1CEZ1z9xpLt-GlqGxlSFLMfBP9xvIqBNZfkdUcUnT3jexTZIK1EZuliRfIxpH6u6iU8TX": "3",  # Koulosse
    "https://methodwakfu.com/wp-content/uploads/2019/11/Milkar_Image-1.png": "3",  # Meulou
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmNWh-RIpkyet6dOTHGCCYmcF82A6NfMqVcA&usqp=CAU": "3",  # Moon
    "https://static.wikia.nocookie.net/dofus-rp/images/e/e6/Dramak.png/revision/latest/scale-to-width-down/216?cb=20150120072036&path-prefix=fr": "3",  # Maitre des Pantins
    "https://jolstatic.fr/dofus/equipe/472077/articles/enutrosor/mallefisk/Monstres/mimikado.jpg": "3",  # Malléfisk
    "https://static.wikia.nocookie.net/krosmoz/images/f/fb/Kharnozor.png/revision/latest?cb=20210422201358&path-prefix=fr": "3",  # Kharnozor
    "https://lh3.googleusercontent.com/TZ_P2KyJ-2_bb-bK_T-G0vhG5nqPpe1AyttALW3TaFwtOPvei1lcJtgaiTN9bUrWXZZXyjoZo90UDAQt82HLlLiE1-Gg8gCWnNvba-oT": "3",  # Silf le Rasboul Majeur
    "https://lh3.googleusercontent.com/MEbuepNxF7zKecL_cFDthGeDjrqzoBiPH5LspipFilIzWjUKWjNZ699GiOt-0fKyWuwdhQ1KNibJza-cX7H0WQa9mhNlMuOafbjRuxLV": "3",  # Maitre Corbac
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj21-rat-blanc-sommaire_orig.jpg": "3",  # Rat Blanc
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj22-rat-noir-sommaire_orig.jpg": "3",  # Rat Noir
    "https://lh3.googleusercontent.com/JptzmIPPG3ANJXCfrQXN79ngTDdzUIJcFBQc89h2X_FGdZFAYGQ5EA_N1T4buAxuh1AfVGRY2d9S2az9q_0lZRNy8V-LE5z2d7QZK3k": "3",  # Pounicheur
    "https://static.wikia.nocookie.net/dofus-rp/images/a/a1/Damadrya.webp/revision/latest?cb=20210407203650&path-prefix=fr": "3",
    # Damadrya
    "https://static.wikia.nocookie.net/dofus-rp/images/f/f9/BlopMR.png/revision/latest/scale-to-width-down/274?cb=20230224094657&path-prefix=fr": "3",  # Blop Multicolore Royal
    "https://lh3.googleusercontent.com/4nI6PlsVo7r-N3Us534HJsQzP9GLgJYoycXXQ6liv8imNh7Nu0p_2nwdyFE5EktOFiV3kvCSCPfcA_jP0I6Ur9g2pqw9NHCbb68cmsmmPA": "3",  # Minotoror
    "https://staticns.ankama.com/comm/news/dofus/www/03_2013/carrousel-relance-frigost.jpg": "3",  # Royalmouth
    "https://lh3.googleusercontent.com/sUrTP3k6q2Q9BkYan-XuT19b_oOlo0sgOe4mK766gi_1wemuxTmt2yuidsv4iyB3zzI2FJIltM_x72Anj9NIxL_OHxpvj2jsfJwGwPK7": "3",  # Tofu Royal
    "https://static.wikia.nocookie.net/dofus-wakfu/images/a/af/126.png/revision/latest?cb=20171126173825&path-prefix=fr": "3",  # Crocabulia
    "https://lh3.googleusercontent.com/rrOO2c_Po2S81OpblqubI-r6_kq8eaY-DhOTY-mxn3wGOn5PoYDrbatT7U31llpWw_YxUSSHT4fZO8snq7JagFHREBTMqnxnV7HNh40uvg": "3",  # Skeunk
    "https://lh3.googleusercontent.com/p9hDS68a3pyF216gHIlfGXGEyLWCK52TdH3WlRtBo8jxLXUu_bJrtfDGKI4oChZFZewEEICXojjgOVgJNB6shaE7khbgWCds4oMqUx6vjw": "3",  # Fraktale
    "https://lh3.googleusercontent.com/vD1CrELpHcoaW3hVGKtD5JoIlBhMwHy1xj4f1YMMgCth9cuEHPAUnPxVsavC4hTFA8SxHiH4POdA0uvAMm8p_nGzMI2LdjiORhUnOHc": "3",  # Haute Truche
    "https://static.wikia.nocookie.net/krosmoz/images/c/c2/El_Piko.jpg/revision/latest?cb=20210422191746&path-prefix=fr": "3",  # El Piko
    "https://lh3.googleusercontent.com/E9ygY-kPnuJ6ti-YR5Pc3zB3h3ZujXpksgGv0iEuNQ8uTNyizAztapKguBIz28a_rlT5RlGYHBUrqCBL-3IlilUwaL1in_1hfzh7xz7JzA": "3",  # Capitaine Ekarlatte
    "https://static.wikia.nocookie.net/krosmoz/images/c/cd/Nagate_la_Dame_des_eaux.png/revision/latest/top-crop/width/360/height/360?cb=20210422205010&path-prefix=fr": "3",
    # Nagate
    "https://static.wikia.nocookie.net/krosmoz/images/1/16/Tanukou%C3%AF_San.png/revision/latest?cb=20210422214342&path-prefix=fr": "3",
    # Tanukoui San
    "https://lh3.googleusercontent.com/rpKYNQ_kny-y0MgEbgyy7pvYeZ7KPPFw_EBw6CnvrbJX5kq-D_7BF2xOOPpdEhDQ8tInRaTHMzD8x7KWuEVGMILeseqKfA3WBVDPKh8": "3",  # Chêne Mou
    "https://lh3.googleusercontent.com/1wa8YqAfIUwSxlra7GJhjrj5gDt7LzV8Jdr8nThkaln8r-49ZMwd_IEbE2awnazUec0Whi1UgaOaxyTfP8DQpLWhZRMxHtWgj-G0f7FV": "3",  # Tynril
    "https://lh3.googleusercontent.com/BF8ZdcAY88qo76osVtB3rxXtKNjLW_gGlNe61H_ktdysQ6FqVDVsoeZVLoTTiCnYWaguiOmAxSiHuI3O6k5lwQTYKiRb_H59vwJwr_k9": "3",  # Mansot Royal
    "https://pbs.twimg.com/media/EqkmPb_W4AEjN-F?format=jpg&name=large": "3",  # Hanshi et Shihan
    "https://www.dofus.com/fr/mmorpg/encyclopedie/monstres/6249-founoroshi": "3",  # Founoroshi
    "https://staticns.ankama.com/comm/news/dofus/www/03_2013/carrouselbenleripate.jpg": "3",  # Ben le Ripate
    "https://4.bp.blogspot.com/-LZPwi-AuGiA/UntawkEc0AI/AAAAAAAAA6k/LsR3KzvPb3E/s1600/sphincter-cell.jpg": "3",  # Sphincter Cell
    "https://cdna.artstation.com/p/assets/images/images/019/912/544/large/yohan-baes-phossile.jpg?1565554176": "3",  # Phossile
    "https://static.wikia.nocookie.net/dofus-rp/images/5/58/HellMina.png/revision/latest?cb=20220524080032&path-prefix=fr": "3",  # Hell mina
    "https://jolstatic.fr/dofus/equipe/548763/donjons/Kimbo/kimbo.png": "4",  # Kimbo
    "https://lh3.googleusercontent.com/ea3y5wRdEN1xz1HQcJ6tsA6GYEfCxFRbZAGsQddu3A01WokCICOz3lFu9-WIp627XSmpN3CSYUITlaqWdKtquI3_qVz8k4R2LRRZY40Z4A": "4",  # Minotot
    "https://static1.millenium.org/articles/5/14/25/75/@/44115-dofus-2018-11-23-23-02-14-hackh-article_image_t-2.png": "4",  # Obsidiantre
    "https://static.wikia.nocookie.net/dofus-rp/images/7/74/Kanigroula2.jpg/revision/latest?cb=20230327085619&path-prefix=fr": "4",  # Kanigroula
    "https://static.wikia.nocookie.net/krosmoz/images/f/f4/Ush_Galesh_2.jpg/revision/latest?cb=20210422215414&path-prefix=fr": "4",  # Ush Galesh
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-shogun-tofugawa.png": "4",
    # Shogun
    "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRrvqh8B582nCuo1xP39qqc9Nh1fye3xDxVH6Omp6n9LLET5Fcm": "4",  # Tengu Givrefoux
    "https://lh3.googleusercontent.com/UoE8lqfRTd4-HYKD64MPdE-c2ApM8KKvm3IghluOoi_LqwWo1QJP2sOxMl_KHmXwjfZQ9KqFcSUuOodv67mngW5xMVU9hMbngPCa1hNk": "4",  # Père Ver
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-xlii.png": "4",  # XLII
    "https://jolstatic.fr/dofus/equipe/412805/donjons/Koumiho/boss_2.png": "4",  # Koumiho
    "https://static.wikia.nocookie.net/dofus-rp/images/a/a8/Hqdefault.jpg/revision/latest?cb=20190911141528&path-prefix=fr": "4",  # Korriandre
    "https://static.wikia.nocookie.net/dofus-rp/images/9/94/Bworker.png/revision/latest?cb=20141007081701&path-prefix=fr": "4",  # Bworker
    "https://static.wikia.nocookie.net/dofus-rp/images/f/f1/Ougah.png/revision/latest?cb=20150811203443&path-prefix=fr": "4",  # Ougah
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj44-ensorcellement3_orig.jpg": "5", #Belladone
    "https://static.wikia.nocookie.net/dofus-rp/images/c/c5/Barb%C3%A9ryl.png/revision/latest?cb=20230103224045&path-prefix=fr": "5", #Barbéryl Clochecuivre"
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj25-toxoliath-sommaire_orig.jpg": "5",  # Toxoliath
    "https://jolstatic.fr/dofus/equipe/412805/donjons/Kolosso/kolosso.png": "5",  # Kolosso
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/wanted8-0fuji-givrefoux_orig.png": "5",  # Fuji Givrefoux
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-grolloum.png": "5",  # Grolloum
    "https://i.skyrock.net/5018/84165018/pics/3111417225_1_3_OhfNxH9d.jpg": "5",  # Glourséleste
    "https://static.wikia.nocookie.net/dofus-rp/images/a/a6/Ombre.png/revision/latest?cb=20150423133333&path-prefix=fr": "5",  # Ombre
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh6qYhEXnH1sZPznpXVtrSt82JfDEA0Iw0GSogMjopqpk-InrLQ5tPDtkeFWHLgovldWY&usqp=CAU": "5",  # Comte Razof
    "https://static.wikia.nocookie.net/krosmoz/images/e/e8/Missiz_Frizz.jpg/revision/latest?cb=20210422204613&path-prefix=fr": "5",  # Missiz Frizz
    "https://static.wikia.nocookie.net/dofusrol/images/b/be/301_all_200_200.jpg/revision/latest/scale-to-width-down/250?cb=20130421021908": "5",  # Sylargh
    "https://www.eclypsia.com/wp-content/uploads/eclypsia/2022/12/klime.jpg": "5",  # Klime
    "https://jolstatic.fr/dofus/equipe/412805/donjons/Nileza/top-nileza.png": "5",  # Nileza
    "https://static.wikia.nocookie.net/krosmoz/images/2/2e/Illu_Comte_Harebourg.png/revision/latest?cb=20221107153510&path-prefix=fr": "5",  # Comte Harebourg
    "https://cdnb.artstation.com/p/assets/images/images/000/107/299/large/charlene-le-scanff-character-design-dofus-ankama-07.jpg?1403128496": "5",  # Merkator
    "https://static.wikia.nocookie.net/dofus-rp/images/7/74/Nidas1.jpg/revision/latest?cb=20230128203518&path-prefix=fr": "5",  # Roi Nidas
    "https://static.wikia.nocookie.net/dofus-rp/images/7/7c/RDV.png/revision/latest/scale-to-width-down/1200?cb=20230128212952&path-prefix=fr": "5",  # Reine des Voleurs
    "https://jolstatic.fr/dofus/equipe/412805/donjons/Baleine/protozorreur.png": "5",  # Protozorreur
    "https://static.wikia.nocookie.net/dofus-rp/images/a/af/Vortex.webp/revision/latest?cb=20210513093405&path-prefix=fr": "5",  # Vortex
    "https://jolstatic.fr/dofus/equipe/412805/donjons/Chaloeil/chaloeil.png": "5",  # Chaloeil
    "https://static1.millenium.org/articles/1/28/88/51/@/312291-menook-article_cover_bd-6.png": "5",  # Capitaine Meno
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-koutoulou.png": "5",  # larve de Koutoulou
    "https://i.ytimg.com/vi/0JTRNFH3Nko/maxresdefault.jpg": "5",  # Dantinéa
    "https://static.wikia.nocookie.net/krosmoz/images/0/07/Tal_Kasha.jpg/revision/latest?cb=20210422214254&path-prefix=fr": "5",  # Tal kasha
    "https://static.wikia.nocookie.net/krosmoz/images/0/0e/Annerice_la_Shushess.jpg/revision/latest?cb=20210422182109&path-prefix=fr": "5",  # Anerice la Shushess
    "https://cdn1.ankama-shop.com/3076-thickbox_default/affiche-ilyzaelle-relief-effet-dore.jpg": "5",  # Ilyzaelle
    "https://static.wikia.nocookie.net/krosmoz/images/a/a5/Solar.jpg/revision/latest?cb=20210422213823&path-prefix=fr": "5",  # Solar
    "https://static.wikia.nocookie.net/dofus-rp/images/1/1a/Bethel.png/revision/latest?cb=20171112215040&path-prefix=fr": "5",  # Bethel Akarna
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj10-dazak-sommaire_orig.jpg": "5",  # Dazak Martegel
    "https://jolstatic.fr/dofus/equipe/412805/donjons/Torkelonia/torkelonia.png": "5",  # Torkélonia
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-corruption.png": "5",
    # Corruption
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgwukbMo2HBtgWYORFotBd30p-jYdzUE96Fw&usqp=CAU": "5",
    # Guerre
    "https://jolstatic.fr/www/captures/93/4/141454.png": "5",  # Servitude
    "https://jolstatic.fr/dofus/equipe/412805/donjons/Misere/misere.png": "5",  # Misère
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-orukam.png": "5",
    # Roi imagami
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/dj19-amirukam-sommaire_orig.jpg": "5",  # Reine Amirukam
    "http://image.noelshack.com/fichiers/2022/36/7/1662902767-kabahal.png": "5",  # Kabahal
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/cavaliers-eliocalypse-sommaire_orig.jpg": "5",
    # 4 Cavaliers
    "https://www.dofuspourlesnoobs.com/uploads/1/3/0/1/13010384/custom_themes/586567114324766674/files/card/dj-eternel-conflit.png": "5",
    # Eternel Conflit
}

global messageBot

def checkGoodFormatGrp(listArg):
    nbUserInGrp = int(listArg[1])

    if (listArg[1].isdigit()):
        return nbUserInGrp
    else:
        return False


def checkGoodFormatRandom(listArg):
    boolFormat = False
    if (listArg[1].isdigit()):
        level = int(listArg[1])
    else:
        return False
    if (listArg[2].isdigit()):
        nbDay = int(listArg[2])
    else:
        return False
    if (level > 0 and level <= 5):
        boolFormat = True
    else:
        return False
    return boolFormat


def checkGoodFormat(listArg):
    argument = 1
    boolFormat = False
    if len(listArg) <= 1:
        return False
    if len(listArg) == 5:
        name = listArg[1] + " " + listArg[2]
        argument += 2
    else:
        name = listArg[1]
        argument += 1
    nbDj = len(listDonjons)
    boolname = False
    idName = ""
    for i in range(0, nbDj):
        if (name in listDonjons[i][2].lower() and len(name) >= 4):
            idName = listDonjons[i][0]
            boolname = True
        i += 1
    if (boolname == False):
        return False
    if (listArg[argument].isdigit()):
        nbDay = int(listArg[argument])
        argument += 1
    else:
        return False
    if (boolname):
        boolFormat = True
    else:
        return False
    return idName


async def sendRandomDj(listArg):
    level = listArg[1]
    nbDay = int(listArg[2])
    nbHours = listArg[3]

    keys = [k for k, v in donjonsDict.items() if v == level]
    idChoixDonjon = random.choice(keys)

    valid = validators.url(idChoixDonjon)
    if valid == True:
        choixDonjon = ""
        imgUrl = idChoixDonjon
    else:
        response = requests.get("https://fr.dofus.dofapi.fr/monsters/" + idChoixDonjon)
        if response.status_code != 200:
            return
        data = response.json()
        choixDonjon = data["name"]
        imgUrl = data["imgUrl"]

    dateNbDay = date.today() + timedelta(nbDay)
    nameDay = dateNbDay.strftime("%A")
    dateNbDay = dateNbDay.strftime("%d/%m/%Y")

    await channelBot.send(
        '@here Reagi par :thumbsup: si tu souhaites participer pour le **' + str(nameDay) + " " + str(
            dateNbDay) + ' à ' + nbHours + '**\nLe donjon choisi **aléatoirement** est : ' + choixDonjon + ' :arrow_down:')
    messageBot = await channelBot.send(imgUrl)
    emoji = '\N{THUMBS UP SIGN}'
    await messageBot.add_reaction(emoji)


async def randomDj(lastMsgSend):
    lastMsgSendContent = lastMsgSend.content
    if ("%randomdj" in lastMsgSendContent and lastMsgSendContent.startswith('%')):
        channelSend = lastMsgSend.channel

        listArg = lastMsgSendContent.split()
        if (checkGoodFormatRandom(listArg)):
            await sendRandomDj(listArg)
        else:
            await channelSend.send(
                "Essaies en tapant : ```%randomdj <level(1-5)> <dans combien de jour> <à quelle heure>```")
    else:
        return


async def sendDonjon(lastMsgSend, idName):
    listArg = lastMsgSend.content.split()
    argument = 1
    if len(listArg) == 5:
        name = listArg[1] + " " + listArg[2]
        argument += 2
    else:
        name = listArg[1]
        argument += 1
    user = lastMsgSend.author.name
    channel = lastMsgSend.channel
    nbDay = int(listArg[argument])
    argument += 1
    nbHours = listArg[argument]

    valid = validators.url(idName)
    if valid == True:
        choixDonjon = name
        imgUrl = idName
    else:
        response = requests.get("https://fr.dofus.dofapi.fr/monsters/" + idName)
        if response.status_code != 200:
            return
        data = response.json()
        choixDonjon = data["name"]
        imgUrl = data["imgUrl"]

    dateNbDay = date.today() + timedelta(nbDay)
    nameDay = dateNbDay.strftime("%A")
    dateNbDay = dateNbDay.strftime("%d/%m/%Y")

    await channel.send('Reagi par :thumbsup: si tu souhaites participer pour le ' + str(nameDay) + " " + str(
        dateNbDay) + ' à ' + nbHours + 'h\nLe donjon choisi par ' + str(
        user) + ' est : ' + choixDonjon + ' :arrow_down:')
    messageBot = await channel.send(imgUrl)
    emoji = '\N{THUMBS UP SIGN}'
    await messageBot.add_reaction(emoji)


async def donjon(lastMsgSend):
    lastMsgSendContent = lastMsgSend.content
    if ("%donjon" in lastMsgSendContent and lastMsgSendContent.startswith('%')):
        channelSend = lastMsgSend.channel
        listArg = lastMsgSendContent.split()
        if (checkGoodFormat(listArg) != False):
            await sendDonjon(lastMsgSend, checkGoodFormat(listArg))
        else:
            await channelSend.send(
                "Essaies en tapant : ```%donjon <nom du boss> <dans combien de jour> <à quelle heure>```")
    else:
        return


async def createRandomGrp(messageBot, nbUser):
    users = set()
    for reaction in messageBot.reactions:
        async for user in reaction.users():
            users.add(user)
    if len(users) <= 1:
        return
    usersReact = set()
    for x in users:
        if "Roulette des donjons" not in x.name:
            usersReact.add("<@" + str(x.id) + ">")
    await messageBot.channel.send(
        ((f"Les Participants: " + str(usersReact)).replace("{", "")).replace("}", "").replace("'", ""))

    nbOfGrp = 1
    # keys name, value group
    groupes = {
    }
    if (len(usersReact) <= nbUser):
        for x in usersReact:
            groupes[x] = nbOfGrp
    else:
        while len(usersReact) >= nbUser:
            thisgrp = random.sample(usersReact, k=nbUser)
            for x in thisgrp:
                groupes[x] = nbOfGrp
                usersReact.remove(x)
            nbOfGrp += 1
    if (len(usersReact) <= nbUser):
        for x in usersReact:
            groupes[x] = nbOfGrp

    nbOfGrp = groupes[list(groupes.keys())[-1]]
    i = 1
    while i <= nbOfGrp:
        thisGrp = [k for k, v in groupes.items() if v == i]
        jolimsgGrp = ((f"Groupe " + str(i) + " : " + str(thisGrp)).replace("[", "")).replace("]", "").replace("'", "")
        await messageBot.channel.send(jolimsgGrp)
        i += 1


async def groupe(lastMsgSend):
    lastMsgSendContent = lastMsgSend.content
    if ("%groupe" in lastMsgSendContent and lastMsgSendContent.startswith('%')):
        channelSend = lastMsgSend.channel
        user = lastMsgSend.author
        listArg = lastMsgSendContent.split()
        if (checkGoodFormatGrp(listArg) != False):
            nbUserInGrp = checkGoodFormatGrp(listArg)
        else:
            await channelSend.send(
                "Essaies en tapant : ```%groupe <nombre joueur par groupe>```")
    else:
        return

    messageBot = await channelSend.fetch_message(channelSend.last_message_id)

    if 'https://' in messageBot.content:
        await createRandomGrp(messageBot, nbUserInGrp)
    else:
        messages = set()
        async for message in channelSend.history(limit=200, oldest_first=True):
            # do something with all messages
            messages.add(message)
        messages = list(messages)

        latestMsgContentImg = set()
        latestMsgCreatedAt = set()

        for msg in messages:
            if ("https://" in str(msg.content) and str(msg.author) == "Roulette des donjons#7941"):
                if type(latestMsgCreatedAt) == set:
                    latestMsgCreatedAt = msg.created_at - timedelta(days=1)
                if latestMsgCreatedAt < msg.created_at:
                    latestMsgContentImg = msg
                    latestMsgCreatedAt = latestMsgContentImg.created_at
        if latestMsgContentImg is None:
            await channelSend.send("Aucun donjon n'a été lancé dans ce channel")
            return
        else:
            await createRandomGrp(latestMsgContentImg, nbUserInGrp)

async def usage_help(lastMsgSend):
    lastMsgSendContent = lastMsgSend.content
    if ("%help" in lastMsgSendContent and lastMsgSendContent.startswith('%')):
        channelSend = lastMsgSend.channel
        await channelSend.send(
            "```%randomdj <level(1-5)(1facile-5difficile)> <dans combien de jour> <à quelle heure>```:arrow_right: Envoi un donjon de manière aléatoire \n```%donjon <nom du boss> <dans combien de jour> <à quelle heure>```:arrow_right: Envoi un donjon\n```%groupe <nombre de joueurs par groupe>```:arrow_right: Créer des groupes aléatoires depuis la liste des participants (réactions à un donjon par :thumbsup:)")

async def maj_access_cagnotte(lastMsgSend):
    channelSend = client.get_channel(1051098171029332038)
    member = lastMsgSend.author
    role_donateur = get(member.guild.roles, name="Donateur Potentiel")
    role_confirme = get(member.guild.roles, name="Membre confirmé")
    role_leader = get(member.guild.roles, name="Leader")
    for guild in client.guilds:
        for member in guild.members:
            if lastMsgSend.created_at - timedelta(60) > member.joined_at:
                if role_confirme in member.roles or role_leader in member.roles:
                    if role_donateur not in member.roles:
                        await member.add_roles(role_donateur)
                        await channelSend.send("Ajout du rôle Donateur Potentiel pour " + str(member))
            if role_donateur in member.roles:
                if role_confirme not in member.roles:
                    if role_leader not in member.roles:
                        await member.remove_roles(role_donateur)
                        await channelSend.send("Suppression du rôle Donateur Potentiel pour " + str(member))

#MAIN
@client.event
async def on_message(message):  # this event is called when a message is sent by anyone
    global channelBot
    channelBot = client.get_channel(1051098638341914764)
    user = message.author
    if user == client.user:
        return
    lastMsgSend = await message.channel.fetch_message(message.channel.last_message_id)

    # Set command random donjon with level and date (ex : %randomdj 4 14/09/2022
    await randomDj(lastMsgSend)
    await donjon(lastMsgSend)
    await groupe(lastMsgSend)
    await usage_help(lastMsgSend)
    await maj_access_cagnotte(lastMsgSend)

# Lance le bot
token = "MTAxOTMwMDUwNgxNjMwODc5Nw.GxptSF.Mm9FTirlA8lEwx6wq4jQL9I8_ALZ-MvlimALXg"
# token = os.environ['DISCORD_TOKEN']
client.run(token)
