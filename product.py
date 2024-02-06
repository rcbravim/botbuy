# PRODUCT
PRODUCT = 'https://www.amazon.com/EVGA-GeForce-Gaming-08G-P5-3667-KL-Cooling/dp/B097S8BR3C/ref=sr_1_4?crid=3IJP4GKF89VA2&dchild=1&keywords=evga+3060+ti&qid=1635938405&qsid=131-4808451-5498802&sprefix=evga+3%2Caps%2C325&sr=8-4&sres=B097CMQVF4%2CB097S8BR3C%2CB08WM28PVH%2CB09FVLSNZ2%2CB097YW4FW9%2CB09622N253%2CB096WM6JFS%2CB098PJNWKD%2CB081R425YH%2CB096HJC18P%2CB09HJS8XQW%2CB07MP5NNKF%2CB099N59B14%2CB07MFN49TK%2CB07R7RZXM6%2CB097Z8YWW1&srpt=VIDEO_CARD'
PRICE_BASE = float(529.99)

# SIGNIN PAGE
SIGNING_PAGE = r'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'
KEEP_SIGNED = '//*[@id="authportal-main-section"]/div[2]/div/div/div/form/div/div[2]/div/div/label/div/label/input'
LOGIN_BTN = '//*[@id="nav-flyout-ya-signin"]/a/span'
INPUT_EMAIL = 'ap_email'
INPUT_PASS = 'ap_password'

# BUY BUTTON
XPATH_BTN = '//*[@id="buy-now-button"]'
PATH_PRICE = '#price_inside_buybox'
CONTINUE_BUY = 'a-button-input a-button-text'
DEFAULT_ADDRESS = '//*[@id="address-book-entry-0"]/div[2]/span/a'
PLACE_ORDER = '//*[@id="placeYourOrder"]/span/input'