---
layout: links
# multilingual page pair id, this must pair with translations of this page. (This name must be unique)
lng_pair: id_links

# publish date (used for seo)
# if not specified, site.time will be used.
#date: 2022-03-03 12:32:00 +0000

# for override items in _data/lang/[language].yml
#title: My title
#button_name: "My button"
# for override side_and_top_nav_buttons in _data/conf/main.yml
#icon: "fa fa-bath"

# seo
# if not specified, date will be used.
#meta_modify_date: 2022-03-03 12:32:00 +0000
# check the meta_common_description in _data/owner/[language].yml
#meta_description: ""

# optional
# please use the "image_viewer_on" below to enable image viewer for individual pages or posts (_posts/ or [language]/_posts folders).
# image viewer can be enabled or disabled for all posts using the "image_viewer_posts: true" setting in _data/conf/main.yml.
#image_viewer_on: true
# please use the "image_lazy_loader_on" below to enable image lazy loader for individual pages or posts (_posts/ or [language]/_posts folders).
# image lazy loader can be enabled or disabled for all posts using the "image_lazy_loader_posts: true" setting in _data/conf/main.yml.
#image_lazy_loader_on: true
# exclude from on site search
#on_site_search_exclude: true
# exclude from search engines
#search_engine_exclude: true
# to disable this page, simply set published: false or delete this file
#published: false


# you can always move this content to _data/content/ folder
# just create new file at _data/content/links/[language].yml and move content below.
###########################################################
#                Links Page Data
###########################################################
page_data:
  main:
    header: "Publications"
    info: " "

  # # To change order of the Categories, simply change order. (you don't need to change list order.)
  category:
    - title: "Bayesian Analysis"
      type: bayesian
      color: "#62b462"
    - title: "Particle Physics"
      type: pp
      color: "#F4A273"

  #   - title: "Web Design"
  #     type: id_webdesign
  #     color: "#F4A273"
  #   - title: "Programming"
  #     type: id_programming
  #     color: "#62b462"

  list:
    -
    # programming
    # - type: research
    #   title: "Research"
    #   url: "https://stackoverflow.com/"
    #   info: "My academic portfolio."
    - type: bayesian
      title: "Applied Bayesian Structural Health Monitoring: inclinometer data anomaly detection and forecasting"
      url: https://arxiv.org/abs/2307.00305
      info: David K. E. Green, Adam Jaspan

    - type: pp
      title: "Search for pair-produced scalar and vector leptoquarks decaying into third-generation quarks and first- or second-generation leptons in pp collisions with the ATLAS detector"
      url: https://link.springer.com/article/10.1007/JHEP06(2023)188
      info: The ATLAS collaboration
    - type: pp
      title: "Search for pairs of scalar leptoquarks decaying into quarks and electrons or muons in √s = 13 TeV pp collisions with the ATLAS detector, (2020), arXiv: 2006.05872 [hep-ex]"
      url: "https://link.springer.com/article/10.1007/JHEP10(2020)112"
      info: The ATLAS collaboration
    - type: pp
      title: "Implementation of merged multi-leg tt ̄ samples at NLO accuracy using Matchbox framework in Herwig 7, tech. rep. ATL-COM-PHYS-2019-1300, CERN, 2019"
      url: "https://cds.cern.ch/record/2692863"
      info: Adam Elliott Jaspan


    # # jekyiiliquid
    # - type: id_jekyiiliquid
    #   title: "Jekyll"
    #   url: "https://jekyllrb.com/"
    #   info: "Transform your plain text into static websites and blogs."
    # - type: id_jekyiiliquid
    #   title: "Jekyll Cheat Sheet"
    #   url: "https://cloudcannon.com/community/jekyll-cheat-sheet/"
    #   info: "There are so many Jekyll variables and filters to remember and it can be tricky to keep it all in your head. This cheat sheet serves as a quick reference of everything Jekyll can do."
    # - type: id_jekyiiliquid
    #   title: "Liquid for Designers"
    #   url: "https://github.com/Shopify/liquid/wiki/Liquid-for-Designers"
    #   info: "Liquid for Designers wiki on GitHub."
    # - type: id_jekyiiliquid
    #   title: "Liquid for Programmers"
    #   url: "https://github.com/Shopify/liquid/wiki/Liquid-for-Programmers"
    #   info: "Liquid for Programmers wiki on GitHub."
    # - type: id_jekyiiliquid
    #   title: "Liquid Reference"
    #   url: "https://shopify.dev/api/liquid/"
    #   info: "Liquid is a template language created by Shopify and written in Ruby. It is now available as an open source project on GitHub."

    # # webdesign
    # - type: id_webdesign
    #   title: "W3Schools"
    #   url: "https://www.w3schools.com/"
    #   info: "W3Schools offers free online tutorials, references and exercises in all the major languages of the web. Covering popular subjects like HTML, CSS, JavaScript, Python, SQL, Java, and many more."
---
