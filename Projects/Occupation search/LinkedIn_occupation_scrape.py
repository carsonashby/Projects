'''psueodcode time
We need the program to  search the company by each of the listed industries, grabbing each position name listed under 
<div class="entity-result__primary-subtitle t-14 t-black">
        <!---->Founder and CEO of Peloton<!---->
      </div>
    
    move onto the next page and repeat the process until there aren't any more searchable pages.
    Then search the next industry and repeat until we have 3679 position titles in the list      
'''
biglist = '''Accounting
Airlines/Aviation
Alternative Dispute Resolution
Alternative Medicine
Animation
Apparel & Fashion
Architecture & Planning
Arts and Crafts
Automotive
Aviation & Aerospace
Banking
Biotechnology
Broadcast Media
Building Materials
Business Supplies and Equipment
Capital Markets
Chemicals
Civic & Social Organization
Civil Engineering
Commercial Real Estate
Computer & Network Security
Computer Games
Computer Hardware
Computer Networking
Computer Software
Construction
Consumer Electronics
Consumer Goods
Consumer Services
Cosmetics
Dairy
Defense & Space
Design
Education Management
E-Learning
Electrical/Electronic Manufacturing
Entertainment
Environmental Services
Events Services
Executive Office
Facilities Services
Farming
Financial Services
Fine Art
Fishery
Food & Beverages
Food Production
Fund-Raising
Furniture
Gambling & Casinos
Glass, Ceramics & Concrete
Government Administration
Government Relations
Graphic Design
Higher Education
Hospital & Health Care
Hospitality
Human Resources
Import and Export
Individual & Family Services
Industrial Automation
Information Services
Information Technology and Services
Insurance
International Affairs
International Trade and Development
Internet
Investment Banking
Investment Management
Judiciary
Law Enforcement
Law Practice
Legal Services
Legislative Office
Leisure, Travel & Tourism
Libraries
Logistics and Supply Chain
Luxury Goods & Jewelry
Machinery
Management Consulting
Maritime
Marketing and Advertising
Market Research
Mechanical or Industrial Engineering
Media Production
Medical Devices
Medical Practice
Mental Health Care
Military
Mining & Metals
Motion Pictures and Film
Museums and Institutions
Music
Nanotechnology
Newspapers
Nonprofit Organization Management
Oil & Energy
Online Media
Outsourcing/Offshoring
Package/Freight Delivery
Packaging and Containers
Paper & Forest Products
Performing Arts
Pharmaceuticals
Philanthropy
Photography
Plastics
Political Organization
Primary/Secondary Education
Printing
Professional Training & Coaching
Program Development
Public Policy
Public Relations and Communications
Public Safety
Publishing
Railroad Manufacture
Ranching
Real Estate
Recreational Facilities and Services
Religious Institutions
Renewables & Environment
Research
Restaurants
Retail
Security and Investigations
Semiconductors
Shipbuilding
Sporting Goods
Sports
Staffing and Recruiting
Supermarkets
Telecommunications
Textiles
Think Tanks
Tobacco
Translation and Localization
Transportation/Trucking/Railroad
Utilities
Venture Capital & Private Equity
Veterinary
Warehousing
Wholesale
Wine and Spirits
Wireless
Writing and Editing'''
biglistlister = biglist.split('\n')
for i in range(len(biglistlister)):
    biglistlister[i] = biglistlister[i].removeprefix('    ')
clean_list = biglistlister


biglist = '''
Alabama
Alaska
Arizona
Arkansas
California
Colorado
Connecticut
Delaware
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
North Carolina
North Dakota
Ohio
Oklahoma
Oregon
Pennsylvania
Rhode Island
South Carolina
South Dakota
Tennessee
Utah
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming
'''
biglistlister = biglist.split('\n')
for i in range(len(biglistlister)):
    biglistlister[i] = biglistlister[i].removeprefix('    ')
biglistlister = biglistlister[1:-1]
state_list = biglistlister




if __name__ == '__main__':
    global scrapey
    scrapey = False
    occupation_list = []
    #First step will be to figure out how to pull the data out of html and into our list
    username = 'carsonjamesashby@gmail.com'
    password = 'w!3)McB:ZD:rmPJ'
    from selenium import webdriver
    import bs4
    import math
    from selenium.webdriver.common.action_chains import ActionChains 
    from selenium.webdriver.support.ui import WebDriverWait
    import time
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    #Login to linkedin and go tht the search page
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    elementID = browser.find_element_by_id('username')
    elementID.send_keys(username)
    elementID = browser.find_element_by_id('password')
    elementID.send_keys(password)
    elementID.submit()
    src = browser.page_source
    time.sleep(15)

# grabs the occupation data from the html and adds it to the list
    def Scrape(browser):
        global scrapey
        timeout = 10
        element_present = EC.presence_of_element_located((By.ID, 'main'))
        WebDriverWait(browser,timeout).until(element_present)
        if scrapey == False:
            time.sleep(1)
            for i in (range(10)):
                try:
                    templocation = "//ul/li[{}]/div/div/div[2]/div/div/div[2]/div[1]".format(i+1)
                    temp = browser.find_element_by_xpath(templocation)
                    position = str(temp.text)
                    occupation_list.append(position)


                except:
                    return
            return
        else:
            return
#Turn the page
    def Page_Turn(browser, counter):
        try:
            if counter < 10:
                time.sleep(1)
                temp_browser = str(browser.current_url)
                page_number = temp_browser[-1]
                page_number = int(page_number)
                page_number += 1
                page_number = str(page_number)
                browser.get(temp_browser[:-1] + page_number)
            else:
                time.sleep(1)
                temp_browser = str(browser.current_url)
                page_number = temp_browser[-2:]
                page_number = int(page_number)
                page_number += 1
                page_number = str(page_number)
                browser.get(temp_browser[:-2] + page_number)
        except ValueError:
            try:
                current_url = browser.current_url
                scr1 = browser.find_element_by_xpath('  /html')
                browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                time.sleep(1)
                browser.find_element_by_xpath("//ul/li[2]/button").click()
            except:
                global scrapey
                scrapey = True
                return
#the big finish of putting all the pieces together
    def Finish_Search(biglist):
        
        for i in range(len(biglist)):
            soup = bs4.BeautifulSoup(src, 'html.parser')
            #restart page
            browser.get('https://www.linkedin.com/search/results/people/?currentCompany=%5B%222658876%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH')
            #click all filters button
            print(biglist[i])
            browser.find_element_by_xpath('//div/nav/div/div[2]/button').click()
            #Scroll the filter box
            scr1 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
            browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            #click and add an industry
            time.sleep(1)
            action = ActionChains(browser)
            toclick = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[7]/div/ul/li[6]')
            action.move_to_element(toclick).click().perform()
            #Enter in the industry
            jobID = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[7]/div/ul/li[6]/div/div/div/input')
            jobID.send_keys(biglist[i])
            #click the industry
            time.sleep(2)
            browser.find_element_by_css_selector('div.basic-typeahead__triggered-content ').click()
            time.sleep(1)
            #click show results
            browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/button[2]/span').click()
            #Scrape the first page
            Scrape(browser)

            # WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pb2 t-black--light t-14")))
            # temp = str(browser.find_element_by_css_selector("div.pb2 t-black--light t-14"))
            # print(temp)
            # temp = temp.removeprefix('<div class="pb2 t-black--light t-14">\n<!-- -->About ')
            # temp = temp.removesuffix(' results<!-- -->\n</div>')
            # temp = temp.replace(',', '')
            # print(temp)
            # temp = int(temp)
            # temp = temp/10
            # temp = math.ceil(temp)
            #Look through all the pages and scrape
            counter = 0
            global scrapey
            scrapey = False
            for i in range(16):
                if scrapey == False:
                    Page_Turn(browser, counter)
                    counter += 1
                    Scrape(browser)

    def Location_Search(keyword):
        
        #setup health wellness and fitness
        soup = bs4.BeautifulSoup(src, 'html.parser')
        #restart page
        browser.get('https://www.linkedin.com/search/results/people/?currentCompany=%5B%222658876%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH')
        #click all filters button
        browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/section/div/nav/div/div[2]/button').click()
        #Scroll the filter box
        scr1 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        #click and add an industry
        time.sleep(1)
        action = ActionChains(browser)
        toclick = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[7]/div/ul/li[6]')
        action.move_to_element(toclick).click().perform()
        #Enter in the industry
        jobID = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[7]/div/ul/li[6]/div/div/div/input')
        jobID.send_keys('Health, Wellness and Fitness')
        #click the industry
        time.sleep(1)
        browser.find_element_by_css_selector('div.basic-typeahead__triggered-content ').click()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/button[2]/span').click()
        soup = bs4.BeautifulSoup(src, 'html.parser')
        #click all filters button
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/section/div/nav/div/div[2]').click()
        #Scroll the filter box
        scr1 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        if type(keyword) == list:
            number_of_states = 6
            for i in range(len(keyword)):
                #click and add a state
                time.sleep(1)
                action = ActionChains(browser)
                clicktemp = ('/html/body/div[4]/div/div/div[2]/ul/li[3]/div/ul/li[{}]').format(number_of_states)
                toclick = browser.find_element_by_xpath(clicktemp)
                action.move_to_element(toclick).click().perform()
                #Enter in the state
                clicktemp = ('/html/body/div[4]/div/div/div[2]/ul/li[3]/div/ul/li[{}]/div/div/div/input').format(number_of_states)
                jobID = browser.find_element_by_xpath(clicktemp)
                jobID.send_keys(keyword[i])
                #click the state
                time.sleep(2)
                clicktemp = ('/html/body/div[4]/div/div/div[2]/ul/li[3]/div/ul/li[{}]/div/div/div[2]/div/div[2]').format(number_of_states)
                browser.find_element_by_xpath(clicktemp).click()
                number_of_states += 1

        else:
            #click and add a state
            time.sleep(1)
            action = ActionChains(browser)
            toclick = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[3]/div/ul/li[6]/button')
            action.move_to_element(toclick).click().perform()
            #Enter in the state
            jobID = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[3]/div/ul/li[6]/div/div/div/input')
            jobID.send_keys(keyword)
            
            #click the state
            time.sleep(2)
            browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[3]/div/ul/li[6]/div/div/div[2]/div/div[2]').click()
           
        #click show results
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/button[2]/span').click()
        #Scrape the first page
        Scrape(browser)
        counter = -1
        for i in range(67):
            if scrapey == False:
                Page_Turn(browser, counter)
                counter += 1
                Scrape(browser)

    #first big search
        #Search New york, texas, and every other state
    
   # Location_Search("New York, United States")
    #Location_Search('Texas, United States')

    
    #Location_Search(state_list)
    Finish_Search(clean_list[75:])
    with open('wth.txt', 'w', encoding='utf-8') as f:
        for item in occupation_list:
            f.write('%s\n' % item)
   # occupation_list =[]
    #
    #with open('Occupations.txt', 'w') as f:
     #   for item in occupation_list:
     #       f.write('%s\n' % item)
    #occupation_list =[]

  #  
   # with open('Occupations.txt', 'w') as f:
    #    for item in occupation_list:
     #       f.write('%s\n' % item)
    


#Fix the problem that there is 1700 people under health, wellness and fitness, 
#possibly split the us up by state and only miss 200, then you can just go up to 46 in each column
#do texas, new york, and every other state