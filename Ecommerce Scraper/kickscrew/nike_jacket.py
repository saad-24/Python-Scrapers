import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Initializer:
    def __init__(self):
        self.category_link_lst = []
        self.product_link_lst = ['https://www.kickscrew.com/products/nike-acg-polartec-r-wolf-tree-cv0652-010', 'https://www.kickscrew.com/products/nike-nba-celtics-sport-jacket-green-cj7147-312', 'https://www.kickscrew.com/products/nike-f-c-cz1000-010', 'https://www.kickscrew.com/products/nike-ar4523-414', 'https://www.kickscrew.com/products/nike-bv2821-222', 'https://www.kickscrew.com/products/nike-cz4353-010', 'https://www.kickscrew.com/products/nike-sportswear-swoosh-logo-dh6685-010', 'https://www.kickscrew.com/products/nike-nba-cj7149-010', 'https://www.kickscrew.com/products/nike-heritage-windrunner-cj9448-010', 'https://www.kickscrew.com/products/nike-bv4684-557', 'https://www.kickscrew.com/products/nike-ct7363-657', 'https://www.kickscrew.com/products/nike-x-lpl-rng-ct9111-010', 'https://www.kickscrew.com/products/nike-sportswear-heritage-windrunner-cj4359-084', 'https://www.kickscrew.com/products/nike-sportswear-synthetic-fill-cz4907-010', 'https://www.kickscrew.com/products/nike-u8fd0u52a8u5bbdu677eu8fdeu5e3du4f11u95f2u5939u514bu5916u5957-u7537u6b3e-u9ed1u8272-da6690-010', 'https://www.kickscrew.com/products/nike-ci9585-021', 'https://www.kickscrew.com/products/nike-acg-bq3446-010', 'https://www.kickscrew.com/products/nike-928484-657', 'https://www.kickscrew.com/products/nike-cu4489-063', 'https://www.kickscrew.com/products/nike-giannis-lightweight-da5670-372', 'https://www.kickscrew.com/products/nike-nba-courtside-av6592-010', 'https://www.kickscrew.com/products/nike-bv5386-412', 'https://www.kickscrew.com/products/nike-sportswear-trend-ul-jkt-dd6171-435', 'https://www.kickscrew.com/products/nike-sportswear-hooded-and-fleece-jacket-with-zipper-placket-men-s-black-dm1220-010', 'https://www.kickscrew.com/products/nike-aeroloft-cd8954-043', 'https://www.kickscrew.com/products/nike-ck7509-010', 'https://www.kickscrew.com/products/nike-aj7947-010', 'https://www.kickscrew.com/products/nike-tech-pack-synthetic-fill-at4571-060', 'https://www.kickscrew.com/products/nike-jordan-legacy-aj13-cw0838-414', 'https://www.kickscrew.com/products/nike-804392-451', 'https://www.kickscrew.com/products/nike-jordan-dc4639-010', 'https://www.kickscrew.com/products/nike-dc6978-337', 'https://www.kickscrew.com/products/nike-sportswear-tech-cu3770-010', 'https://www.kickscrew.com/products/nike-jordan-dc4638-010', 'https://www.kickscrew.com/products/nike-hooded-down-jacket-men-s-white-dd6964-072', 'https://www.kickscrew.com/products/nike-air-cu4169-010', 'https://www.kickscrew.com/products/nike-logo-cu7793-010', 'https://www.kickscrew.com/products/nike-logo-dd6789-077', 'https://www.kickscrew.com/products/nike-bv0192-492', 'https://www.kickscrew.com/products/nike-golf-x-stone-island-av5229-406', 'https://www.kickscrew.com/products/nike-big-swoosh-logo-ci9596-010', 'https://www.kickscrew.com/products/nike-aj7760-663', 'https://www.kickscrew.com/products/nike-885930-010', 'https://www.kickscrew.com/products/jordan-men-aj1070-814', 'https://www.kickscrew.com/products/nike-sportswear-cj4561-657', 'https://www.kickscrew.com/products/nike-da6716-469', 'https://www.kickscrew.com/products/nike-sportswear-swoosh-cj4885-100', 'https://www.kickscrew.com/products/nike-lightweight-nba-cj7115-010', 'https://www.kickscrew.com/products/nike-logo-bv2648-063', 'https://www.kickscrew.com/products/nike-sportswear-bv4720-010', 'https://www.kickscrew.com/products/nike-logo-dd6088-219', 'https://www.kickscrew.com/products/nike-windrunner-cq2921-100', 'https://www.kickscrew.com/products/nike-dri-fit-logo-cu4948-010', 'https://www.kickscrew.com/products/nike-dd4542-010', 'https://www.kickscrew.com/products/nike-sportswear-ar3133-012', 'https://www.kickscrew.com/products/nike-sportswear-swoosh-dj8038-401', 'https://www.kickscrew.com/products/nike-dd8413-010', 'https://www.kickscrew.com/products/nike-sportswear-tech-pack-bv4431-886', 'https://www.kickscrew.com/products/nike-cw3894-100', 'https://www.kickscrew.com/products/nike-sportswear-dd6495-133', 'https://www.kickscrew.com/products/nike-nba-ce-courtside-cn1439-419', 'https://www.kickscrew.com/products/nike-bv5700-043', 'https://www.kickscrew.com/products/nike-bv2966-325', 'https://www.kickscrew.com/products/nike-do0776-010', 'https://www.kickscrew.com/products/nike-sportswear-down-fill-windrunner-cu4403-010', 'https://www.kickscrew.com/products/nike-sportswear-cz9880-657', 'https://www.kickscrew.com/products/nike-therma-flex-showtime-nba-899861-495', 'https://www.kickscrew.com/products/nike-cn9776-622', 'https://www.kickscrew.com/products/nike-sb-skateboard-dunk-high-x-concepts-ck7290-475', 'https://www.kickscrew.com/products/nike-da2795-429', 'https://www.kickscrew.com/products/jordan-casual-sports-hooded-jacket-men-s-white-da9833-133', 'https://www.kickscrew.com/products/nike-cz4892-010', 'https://www.kickscrew.com/products/nike-sportswear-bv4684-451', 'https://www.kickscrew.com/products/nike-ci9585-010', 'https://www.kickscrew.com/products/nike-928890-752', 'https://www.kickscrew.com/products/nike-logo-dd0574-010', 'https://www.kickscrew.com/products/nike-sb-skateboard-logo-ck5447-010', 'https://www.kickscrew.com/products/nike-as-m-men-s-nk-flight-jacket-cn8509-013', 'https://www.kickscrew.com/products/nike-x-skepta-cu9743-010', 'https://www.kickscrew.com/products/nike-m-men-s-nk-tf-turf-rpl-miler-jacket-dh6682-010', 'https://www.kickscrew.com/products/nike-sportswear-windrunner-down-fill-aa8854-101', 'https://www.kickscrew.com/products/nike-big-swoosh-logo-dh2474-456', 'https://www.kickscrew.com/products/nike-dr6862-104', 'https://www.kickscrew.com/products/nike-tech-fleece-dh7827-492', 'https://www.kickscrew.com/products/nike-dr6864-104', 'https://www.kickscrew.com/products/nike-sb-ck5470-010', 'https://www.kickscrew.com/products/nike-jordan-dj0878-010', 'https://www.kickscrew.com/products/nike-storm-fit-adv-m65-dd6873-004', 'https://www.kickscrew.com/products/nike-sportswear-tech-pack-ck0711-094', 'https://www.kickscrew.com/products/nike-sportswear-jacket-bv5300-064', 'https://www.kickscrew.com/products/nike-sportswear-synthetic-fill-bv4583-886', 'https://www.kickscrew.com/products/nike-do2323-410', 'https://www.kickscrew.com/products/nike-sportswear-windrunner-dc4113-714', 'https://www.kickscrew.com/products/nike-therma-bv3999-011', 'https://www.kickscrew.com/products/nike-x-off-white-men-aa3298-010', 'https://www.kickscrew.com/products/nike-dri-fit-bv2719-072', 'https://www.kickscrew.com/products/nike-sportswear-tatting-jacket-coat-men-white-cu4310-100', 'https://www.kickscrew.com/products/nike-mens-sports-hooded-jacket-blue-bv4790-480', 'https://www.kickscrew.com/products/nike-storm-fit-division-flash-dd6044-010', 'https://www.kickscrew.com/products/nike-male-jacket-cu4206-010', 'https://www.kickscrew.com/products/nike-641196-547', 'https://www.kickscrew.com/products/nike-windrunner-cz9055-869', 'https://www.kickscrew.com/products/nike-ck3106-432', 'https://www.kickscrew.com/products/nike-x-off-white-aa3256-010', 'https://www.kickscrew.com/products/nike-693534-065', 'https://www.kickscrew.com/products/nike-mnk-dry-hoodie-fzflc-cz6377-451', 'https://www.kickscrew.com/products/nike-sportswear-cz9895-010', 'https://www.kickscrew.com/products/nike-logo-cw7349-010', 'https://www.kickscrew.com/products/nike-cn7067-100', 'https://www.kickscrew.com/products/nike-do2966-010', 'https://www.kickscrew.com/products/nike-therma-flex-showtime-nba-76-at9478-280', 'https://www.kickscrew.com/products/nike-sportswear-windrunner-da0002-657', 'https://www.kickscrew.com/products/nike-cj5475-250', 
'https://www.kickscrew.com/products/nike-acg-therma-fit-adv-rope-de-dope-dj1257-010', 'https://www.kickscrew.com/products/nike-lebron-m-men-s-nk-down-otw-jacke-down-jacket-black-ck6774-010', 'https://www.kickscrew.com/products/nike-yoga-dd2183-010', 'https://www.kickscrew.com/products/nike-sportswear-tech-pack-ar1543-475', 'https://www.kickscrew.com/products/nike-ci9203-451', 'https://www.kickscrew.com/products/nike-strike-da6665-087', 'https://www.kickscrew.com/products/nike-dc0502-375', 'https://www.kickscrew.com/products/nike-academy-bq7347-102', 
'https://www.kickscrew.com/products/nike-premium-ck6779-761', 'https://www.kickscrew.com/products/nike-sportswear-logo-do6938-100', 'https://www.kickscrew.com/products/nike-sportswear-bv4720-891', 'https://www.kickscrew.com/products/nike-jordan-cd8734-091', 'https://www.kickscrew.com/products/nike-academy-synthetic-fill-893799-451', 'https://www.kickscrew.com/products/nike-jordan-dq0385-110', 'https://www.kickscrew.com/products/nike-ar2184-012', 'https://www.kickscrew.com/products/nike-shield-flash-bv5616-547', 'https://www.kickscrew.com/products/nike-jordan-dc9582-203', 'https://www.kickscrew.com/products/nike-cu0226-634', 'https://www.kickscrew.com/products/nike-sportswear-coaches-da8735-010', 'https://www.kickscrew.com/products/nike-jacket-men-s-black-white-aj7936-100', 'https://www.kickscrew.com/products/nike-air-x-kim-jones-dc9983-451', 'https://www.kickscrew.com/products/nike-lab-da0311-010', 'https://www.kickscrew.com/products/nike-jordan-at9959-010', 
'https://www.kickscrew.com/products/nike-sportswear-tech-pack-ck0698-095', 'https://www.kickscrew.com/products/nike-sportswear-dri-fit-tech-pack-dd6595-010', 'https://www.kickscrew.com/products/nike-therma-926466-100', 'https://www.kickscrew.com/products/nike-logo-804389-063', 
'https://www.kickscrew.com/products/nike-sportswear-cu4480-031', 'https://www.kickscrew.com/products/nike-as-m-men-s-nk-therma-hd-fz-winterized-at3918-010', 'https://www.kickscrew.com/products/nike-yoga-cu6261-283', 'https://www.kickscrew.com/products/nike-sportswear-bv5211-331', 'https://www.kickscrew.com/products/nike-acg-polartec-r-wolf-tree-cv0652-216', 'https://www.kickscrew.com/products/nike-sportswear-swoosh-cj5640-010', 'https://www.kickscrew.com/products/nike-sportwear-tech-pack-ck0711-010', 'https://www.kickscrew.com/products/nike-jordan-zion-flight-dj5868-246', 'https://www.kickscrew.com/products/nike-sportswear-tech-pack-cu3759-095', 'https://www.kickscrew.com/products/nike-sportswear-down-fill-aj7949-010', 'https://www.kickscrew.com/products/nike-cu4362-010', 'https://www.kickscrew.com/products/nike-acg-bq7198-010', 'https://www.kickscrew.com/products/nike-acg-ct2949-247', 'https://www.kickscrew.com/products/nike-therma-aj4451-091', 'https://www.kickscrew.com/products/nike-sportswear-dri-fit-tech-pack-dd6595-087', 'https://www.kickscrew.com/products/nike-dc1292-010', 'https://www.kickscrew.com/products/nike-at4879-100', 'https://www.kickscrew.com/products/nike-thrma-cz7394-320', 'https://www.kickscrew.com/products/nike-x-drake-nocta-da4137-739', 'https://www.kickscrew.com/products/nike-nba-db1432-312', 'https://www.kickscrew.com/products/nike-showtime-911116-021', 'https://www.kickscrew.com/products/nike-861580-010', 'https://www.kickscrew.com/products/nike-therma-fit-adv-dd2131-326', 'https://www.kickscrew.com/products/nike-lebron-da6718-010', 'https://www.kickscrew.com/products/nike-da2493-010', 'https://www.kickscrew.com/products/nike-dri-fit-928011-013', 'https://www.kickscrew.com/products/nike-tech-fleece-cz1797-072', 'https://www.kickscrew.com/products/nike-logo-db2471-010', 'https://www.kickscrew.com/products/nike-logo-ct6657-480', 'https://www.kickscrew.com/products/air-jordan-939969-010', 'https://www.kickscrew.com/products/nike-as-m-men-s-nk-flight-jacket-cn8509-010', 'https://www.kickscrew.com/products/nike-logo-dq5064-133', 
'https://www.kickscrew.com/products/nike-928484-078', 'https://www.kickscrew.com/products/nike-logo-dd3309-010', 'https://www.kickscrew.com/products/nike-lebron-mens-james-basketball-sport-hoodie-jacket-golden-at3903-723', 'https://www.kickscrew.com/products/nike-air-logo-color-block-casual-sports-hooded-jacket-men-s-red-928630-687', 'https://www.kickscrew.com/products/nike-ck6363-063', 'https://www.kickscrew.com/products/nike-jordan-air-23-engineered-bq5766-100', 'https://www.kickscrew.com/products/nike-jordan-animal-instinct-cu1686-010', 'https://www.kickscrew.com/products/nike-nba-db4787-010', 'https://www.kickscrew.com/products/nike-sb-cv4306-325', 'https://www.kickscrew.com/products/nike-ar1816-010', 'https://www.kickscrew.com/products/nike-jordan-zion-flight-dj5868-010', 'https://www.kickscrew.com/products/nike-men-s-sports-warm-woven-cotton-jacket-blue-943355-423', 'https://www.kickscrew.com/products/nike-dwn-fill-snl-nfs-down-jacket-men-black-white-ck1850-121', 'https://www.kickscrew.com/products/nike-sportswear-cw4820-010', 'https://www.kickscrew.com/products/nike-logo-dd6789-326', 'https://www.kickscrew.com/products/nike-nike-sportswear-down-fill-windrunner-shield-cu4409-430', 'https://www.kickscrew.com/products/nike-ar2210-101', 'https://www.kickscrew.com/products/nike-sportswear-airmoji-wvn-jkt-jacket-teeth-da8735-389', 'https://www.kickscrew.com/products/nike-da6697-010', 'https://www.kickscrew.com/products/nike-as-m-men-s-nk-flex-hybrid-jkt-cu6739-010', 'https://www.kickscrew.com/products/nike-dm5941-068', 'https://www.kickscrew.com/products/nike-ar3132-728', 'https://www.kickscrew.com/products/nike-air-hood-fz-flc-logo-cd9223-010', 'https://www.kickscrew.com/products/nike-aj5322-451', 'https://www.kickscrew.com/products/nike-repel-synthetic-fill-ck6073-010', 'https://www.kickscrew.com/products/nike-18ss-short-street-style-jacket-at4489-614', 'https://www.kickscrew.com/products/nike-m-men-s-sportswear-down-fill-hd-jacket-806862-010', 'https://www.kickscrew.com/products/nike-cu5739-652', 'https://www.kickscrew.com/products/nike-sportswear-cq7768-010', 'https://www.kickscrew.com/products/nike-as-m-men-s-sportswear-sf-windrunner-hd-jkt-dd6796-415', 'https://www.kickscrew.com/products/nike-nba-cj7146-495', 'https://www.kickscrew.com/products/nike-dc4113-841', 'https://www.kickscrew.com/products/nike-bq3446-411', 'https://www.kickscrew.com/products/nike-therma-fit-tech-pack-jacket-men-s-gray-dd6635-060', 'https://www.kickscrew.com/products/nike-sportswear-swoosh-logo-dd5968-077', 'https://www.kickscrew.com/products/nike-bv4533-010', 'https://www.kickscrew.com/products/air-jordan-bq6957-010', 'https://www.kickscrew.com/products/nike-tech-fleece-cz1797-063', 'https://www.kickscrew.com/products/nike-sportswear-windrunner-da0002-010', 'https://www.kickscrew.com/products/nike-bv4763-222', 'https://www.kickscrew.com/products/nike-x-martine-rose-track-jacket-aq4456-323', 'https://www.kickscrew.com/products/nike-as-m-men-s-nk-rpl-miler-jkt-jacket-logo-dd4747-084', 'https://www.kickscrew.com/products/nike-men-s-sportswear-jacket-pink-dm7900-603', 'https://www.kickscrew.com/products/nike-lab-heritage-jacket-hyper-pink-red-aa1569-604', 'https://www.kickscrew.com/products/nike-cd9551-480', 'https://www.kickscrew.com/products/nike-nike-sportswear-down-fill-windrunner-shield-long-down-jacket-white-cu4409-100', 'https://www.kickscrew.com/products/nike-sportswear-logo-dm1184-411', 'https://www.kickscrew.com/products/nike-sportswear-windrunner-cz0782-133', 'https://www.kickscrew.com/products/nike-swoosh-logo-aa5010-100', 'https://www.kickscrew.com/products/nike-ao1501-010', 'https://www.kickscrew.com/products/nike-sportswear-punk-logo-cz1670-380', 'https://www.kickscrew.com/products/nike-sportswear-tech-pack-synthetic-fill-at4571-657', 'https://www.kickscrew.com/products/nike-ck1850-634', 'https://www.kickscrew.com/products/nike-jordan-dn3406-010', 'https://www.kickscrew.com/products/nike-flex-ck1910-010', 'https://www.kickscrew.com/products/nike-sportswear-heritage-windrunner-cj4359-657', 'https://www.kickscrew.com/products/nike-cj4987-060', 'https://www.kickscrew.com/products/nike-male-jacket-cq8924-812', 'https://www.kickscrew.com/products/nike-cj4501-902', 'https://www.kickscrew.com/products/nike-bv5184-657', 'https://www.kickscrew.com/products/nike-bv4875-010', 'https://www.kickscrew.com/products/nike-aj3588-010', 'https://www.kickscrew.com/products/nike-big-swoosh-logo-bq6546-410', 'https://www.kickscrew.com/products/nike-run-division-flash-cu5537-010', 'https://www.kickscrew.com/products/nike-air-db6063-657', 'https://www.kickscrew.com/products/nike-dri-fit-db2439-312', 'https://www.kickscrew.com/products/nike-sportswear-swoosh-logo-dd5967-010', 'https://www.kickscrew.com/products/nike-ar2184-451', 'https://www.kickscrew.com/products/nike-cu5000-430', 'https://www.kickscrew.com/products/nike-men-paris-saint-germain-coat-padded-jacket-navy-psg-ci1303-414', 'https://www.kickscrew.com/products/nike-bv4709-096', 'https://www.kickscrew.com/products/nike-sportswear-windrunner-cj4378-364', 'https://www.kickscrew.com/products/nike-sportswear-city-made-logo-da0078-320', 'https://www.kickscrew.com/products/air-jordan-34-ar1170-010', 'https://www.kickscrew.com/products/nike-dj5219-010', 'https://www.kickscrew.com/products/nike-x-sacai-parka-ct3267-475', 'https://www.kickscrew.com/products/nike-air-dri-fit-dm7550-010', 'https://www.kickscrew.com/products/as-w-np-df-pckbl-hz-jacket-black-white-dd6280-010', 'https://www.kickscrew.com/products/nike-as-w-nike-sportswear-nike-sportswear-swsh-wvn-jkt-jacket-phantom-sanddrift-dm6204-030', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-tf-turf-city-jkt-jacket-black-white-dh4080-010', 'https://www.kickscrew.com/products/nike-as-w-j-heritage-woven-sld-jkt-jacket-black-gym-red-dn4417-010', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-swsh-shrpa-gx-fz-jkt-jacket-black-white-dd5621-010', 'https://www.kickscrew.com/products/nike-as-w-nike-sportswear-nike-sportswear-essntl-wvn-jkt-jacket-hbr-pink-oxford-white-dm6182-601', 'https://www.kickscrew.com/products/as-w-j-new-classics-2-0-top-light-army-light-bone-dj2717-320', 'https://www.kickscrew.com/products/nike-as-w-nike-sportswear-nike-sportswear-essntl-wvn-jkt-jacket-field-white-black-dm6244-100', 'https://www.kickscrew.com/products/nike-as-w-nk-icon-clash-wvn-jkt-black-dm7474-010', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-swsh-shrpa-gx-fz-jkt-jacket-rattan-sail-dd5621-206', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-essntl-shrpa-jkt-jacket-hemp-white-do7761-200', 'https://www.kickscrew.com/products/as-w-nk-arolft-jkt-black-reflective-silv-cz1544-010', 'https://www.kickscrew.com/products/as-w-j-new-classics-2-0-top-black-cave-purple-dj2717-010', 'https://www.kickscrew.com/products/nike-as-w-nike-sportswear-nike-sportswear-essntl-wvn-jkt-jacket-hbr-white-black-dm6182-100', 'https://www.kickscrew.com/products/as-w-nk-sfadv-run-dvn-jkt-sail-atomic-orange-dd6420-133', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-icn-clsh-shrpa-jkt-jacket-lo-sail-dd5089-133', 'https://www.kickscrew.com/products/nike-as-w-nike-sportswear-nike-sportswear-essntl-wvn-jkt-jacket-hbr-black-white-dm6182-010', 'https://www.kickscrew.com/products/as-w-nk-arolft-jkt-sail-reflective-silv-cz1544-133', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-stmt-dwn-jkt-jacket-black-mystic-stone-cu5814-010', 'https://www.kickscrew.com/products/as-wnsw-tf-turf-rpl-windrner-hd-jkt-regal-pink-regal-pink-dh4074-695', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-tch-flc-long-fz-black-black-cw4297-010', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-icn-clsh-jkt-jacket-syn-fill-black-black-cz1871-010', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-essntl-wvn-jkt-jacket-field-harvest-moon-white-dm6244-851', 'https://www.kickscrew.com/products/as-w-nk-run-dvn-reflective-jkt-indigo-haze-cave-purple-dd6463-519', 'https://www.kickscrew.com/products/as-w-nk-df-rn-dvn-po-pckbl-jkt-pale-coral-black-dd5394-864', 'https://www.kickscrew.com/products/nike-as-w-nk-df-bliss-luxe-anorak-mineral-clay-clear-dh3528-215', 'https://www.kickscrew.com/products/nike-as-w-j-srt-cny-chinese-new-year-ma-1-jkt-jacket-black-starfish-do4146-010', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-tch-flc-wr-hoodie-fz-black-black-cw4299-010', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-tch-flc-crew-bleached-coral-bv3452-697', 'https://www.kickscrew.com/products/as-w-nike-sportswear-nike-sportswear-tch-flc-crew-pink-quartz-white-bv3452-606', 'https://www.kickscrew.com/products/as-w-nk-run-dvn-reflective-jkt-black-atomic-orange-dd6463-010']
class Browser:
    def session(self):
        self.driver = webdriver.Chrome()

class Scraper(Initializer, Browser):
    def collect_categories(self):
        # jordan = self.driver.find_element(By.XPATH, '//div[@class="tier-1"]/ul/li[1]/a')
        nike = self.driver.find_element(By.XPATH, '//div[@class="tier-1"]/ul/li[2]/a')
        # yeezy = self.driver.find_element(By.XPATH, '//div[@class="tier-1"]/ul/li[3]/a')
        # addidas = self.driver.find_element(By.XPATH, '//div[@class="tier-1"]/ul/li[4]/a')
        self.category_link_lst.extend([nike.get_attribute('href')])
        print(self.category_link_lst)


    def collect_product_info(self, filename):
            wait = WebDriverWait(self.driver, 20)
            for i in self.product_link_lst:
                self.driver.get(i)

            # time.sleep(1)
                product_link = []
                product_link.append(self.driver.current_url)
                print(self.driver.current_url)

                # time.sleep(1)
                # product id
                product_id = []

                # time.sleep(1)
                # Model
                model_lst = []
                try:
                    model = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="pdp-product-info-col"]/span[@class="pdp-body-text"]')))
                    model_lst.append(model.text)
                    print(model.text)
                except:
                    model_lst.append("Not Found")
                
                # time.sleep(1)
                # Images
                image_lst = []
                try:
                    image = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="product-media product-media--image"]/div/img')))
                    image_lst.append(image.get_attribute('src'))
                    print(image.get_attribute('src'))
                except:
                    image_lst.append("Not Found")
                
                # time.sleep(1)
                # price
                price_lst = []
                try:
                    price = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="product-detail__form"]/div[@class="price-area product-detail__gap-sm"]/span')))
                    price_lst.append(price.text)
                    print(price.text)
                except:
                    price_lst.append("Not Found")

                # time.sleep(1)
                # name
                title_lst = []
                brand_lst = []
                try:
                    title = wait.until(EC.presence_of_element_located((By.XPATH, '//h1[@class="product-area__details__title product-detail__gap-sm h2"]')))
                    title_lst.append(title.text)
                    print(title.text)
                    air = 'Jordan'
                    nike = 'Nike'
                    adidas = 'Adidas'
                    yeezy = 'Yeezy'
                    if air.lower() in title.text.lower():
                        brand_lst.append("Air Jordan")
                    elif nike.lower() in title.text.lower():
                        brand_lst.append("Nike")
                    elif adidas.lower() in title.text.lower():
                        if yeezy.lower() in title.text.lower():
                            brand_lst.append('Yeezy')
                        else:
                            brand_lst.append('Adidas')
                except:
                    title_lst.append("Not Found")

                # Description
                # time.sleep(1)
                description_lst = []
                try:
                    description_tab = self.driver.find_element(By.XPATH, '//div[@class="cc-tabs__tab"][4]')
                    description_tab.click()
                    time.sleep(1)
                    description = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="cc-tabs__tab"][4]/div/p[@hidden]')))
                    self.driver.execute_script("arguments[0].setAttribute('style', 'display: block;');", description)
                    description_lst.append(description.text)
                    print(description.text)
                except:
                    description_lst.append("Not Found")

                # time.sleep(1)
                # meta_title
                meta_title_lst = []
                try:
                    meta_title = wait.until(EC.presence_of_element_located((By.XPATH,'//meta[@name="title"]')))
                    meta_title_lst.append(meta_title.get_attribute('content'))
                except:
                    meta_title_lst.append("Not Found")

                
                # time.sleep(1)
                # meta description
                meta_desc_lst = []
                try:
                    meta_desc = wait.until(EC.presence_of_element_located((By.XPATH, '//meta[@property="og:description"]')))
                    meta_desc_lst.append(meta_desc.get_attribute('content'))
                except:
                    meta_desc_lst.append("Not Found")

                time.sleep(1)
                # additional images
                additional_image_lst = []
                add_image = []
                try:
                    images = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="product-media product-media--image"]/div/img')))
                    for i in images:
                        add_image.append(i.get_attribute('src'))
                        print(i.get_attribute('src'))
                    my_string = '|'.join(add_image)
                    additional_image_lst.append(my_string)
                        
                except:
                    additional_image_lst.append("Not Found")

                # time.sleep(2)
                # product_attributes
                attributes_lst = []
                product_attribute_lst = []
                try:
                    labels = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="pdp-product-info-col"]//h3')))
                    values = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="pdp-product-info-col"]//span')))
                    try:
                        heading = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="cc-tabs__tab"][1]/div/h3')))
                    except:
                        heading = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="cc-tabs__tab"][1]/h2')))
                    time.sleep(2)
                    for label, value in zip(labels, values):
                        attribute = "{}:{}:{}".format(heading.text, label.text, value.text)
                        attributes_lst.append(attribute)

                    my_string = '|'.join(attributes_lst)
                    product_attribute_lst.append(my_string)

                except:
                    product_attribute_lst.append("Not Found")


                # time.sleep(1)
                # product category
                product_cat = []
                product_cat.append("SNEAKERS|SNEAKERS")
                # try:
                #     product_category = category
                #     sub_category = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="vendor product-detail__gap-sm"]/span')))
                #     category_string = "{}|{}>{}".format(product_category, product_category, sub_category.text)
                #     product_cat.append(category_string)
                # except:
                #     product_cat.append("Not Found")


                # time.sleep(2)
                product_options_lst = []
                options_lst = []
                try:
                    sizes = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-option-name="Size"]//div[@class="clickyboxes clickyboxes-sq-picker-grid cc-init"]/div/a[@data-qty="qty"]/label/span[1]')))
                    size_prices = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-option-name="Size"]//div[@class="clickyboxes clickyboxes-sq-picker-grid cc-init"]/div/a[@data-qty="qty"]/label/span[2]')))
                    for shoe_size, size_price in zip(sizes, size_prices):
                        product_option = "select:Sizes:{}:+{}.0000.100:1:+0.00000000:1:".format(shoe_size.text, size_price.text)
                        options_lst.append(product_option)

                    my_string = '|'.join(options_lst)
                    product_options_lst.append(my_string)

                except:
                    product_options_lst.append("Not Found")

                
                data = []
                data.extend([product_id, model_lst, 100, image_lst, price_lst, product_link, title_lst, description_lst, meta_title_lst, meta_desc_lst, additional_image_lst, product_attribute_lst, brand_lst, product_cat, product_options_lst])

                with open(filename, 'a', encoding='utf8', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(data)




    def collect_products(self,filename):
        global next_btn
        wait = WebDriverWait(self.driver, 5)
        for i in self.category_link_lst:
            self.driver.get(i)
            time.sleep(2)
            categories = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-widget="product-types"]//ul//li//a')))
            category_lst = []
            for category in categories:
                category_lst.append(category.get_attribute('href'))
                
            
            for i in category_lst:
                if i == 'https://www.kickscrew.com/collections/nike?product_type=Sneakers':
                    product_link_lst = []
                    self.driver.get(i)
                    print(i)
                    print('yes')
                    category_name = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@class="ais-Menu-item ais-Menu-item--selected"]/div/a/span[1]')))
                    b = category_name.text
                    try:
                        next_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Next"]')))
                    except:
                        products = self.driver.find_elements(By.XPATH, '//li[@class="ais-Hits-item"]/article/a')
                        for product in products:
                            try:
                                oosbadge = self.driver.find_element(By.XPATH, "//span[contains(text(),'Out of Stock')]")
                            except:
                                product_link_lst.append(product.get_attribute('href'))
                                print(product.get_attribute('href'))

                    while next_btn:
                        products = self.driver.find_elements(By.XPATH, '//li[@class="ais-Hits-item"]/article/a')
                        for product in products:
                            try:
                                oosbadge = self.driver.find_element(By.XPATH, "//span[contains(text(),'Out of Stock')]")
                            except:
                                product_link_lst.append(product.get_attribute('href'))
                                print(product.get_attribute('href'))
                        
                        try:
                            next_link = self.driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
                            a = next_link.get_attribute('href')
                        except:
                            break

                        self.driver.get(a)
                
                    print(len(product_link_lst))
                    for j in product_link_lst:
                        self.driver.get(j)

                        self.collect_product_info(filename, category=b)


            
class CSV():
    def make_csv(self, filename):
        with open(filename, 'w', encoding='utf8', newline='') as f:
            csv_writer = csv.writer(f)
            columns = ['Product ID','Model','Quantity','Image','Price','Link','Name_en','Description_en','Meta_title_en','Meta_description_en','Additional_Image','Product_Attributes','Brand','Product_Category','Product_Option']
            csv_writer.writerow(columns)

class Scraper_Implementor(Scraper,CSV):
    def implementor(self, url, filename):
        super().session()
        super().make_csv(filename)
        # self.driver.get(url)
        # super().collect_categories()
        # super().collect_products(filename)
        super().collect_product_info(filename)
        

        

filename = 'product_sample38.csv'
obj = Scraper_Implementor()
obj.implementor('https://www.kickscrew.com/', filename)