# -*- coding: utf-8 -*-
import re

from parsel import Selector
from w3lib.html import remove_tags

a ="""
<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" class="w980"><head id="ctl00_Head1"><script type="text/javascript" async="" src="http://cpro.baidu.com/cpro/ui/rt.js"></script><script type="text/javascript" async="" src="http://webresource.c-ctrip.com/ResUnionOnline/R1/remarketing/js/s.js"></script><script type="text/javascript" async="" src="http://webresource.c-ctrip.com/ResUnionOnline/R1/remarketing/js/mba_ctrip.js"></script><script type="text/javascript" async="" src="http://webresource.c-ctrip.com/ResUnionOnline/R1/remarketing/js/thirdPart.js?v=2018822151213"></script><script type="text/javascript" async="" src="http://webresource.c-ctrip.com/ResUnionOnline/R1/remarketing/js/mkt_setUnionRecord.js?v=2018822151213"></script><script type="text/javascript" async="" src="http://webresource.c-ctrip.com/ResUnionOnline/R1/remarketing/js/__nts.js?v=2018822151213"></script><script type="text/javascript" async="" src="http://webresource.c-ctrip.com/ResUnionOnline/R1/remarketing/js/remarketing.js?v=20160329"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script type="text/javascript" charset="utf-8" async="" src="//m.ctrip.com/restapi/soa2/12378/json/getGeneralConfigData?key=Holiday&amp;callback=cQuery.jsonpCalendarFn"></script><script type="text/javascript" charset="utf-8" async="" src="//m.ctrip.com/restapi/soa2/12378/json/getGeneralConfigData?key=Holiday&amp;callback=cQuery.jsonpCalendarFn"></script><script type="text/javascript" charset="utf-8" async="" src="//m.ctrip.com/restapi/soa2/12378/json/getGeneralConfigData?key=Holiday&amp;callback=cQuery.jsonpCalendarFn"></script><script type="text/javascript" charset="utf-8" async="" src="//m.ctrip.com/restapi/soa2/12378/json/getGeneralConfigData?key=Holiday&amp;callback=cQuery.jsonpCalendarFn"></script><script type="text/javascript" charset="utf-8" async="" src="//m.ctrip.com/restapi/soa2/12378/json/getGeneralConfigData?key=Holiday&amp;callback=cQuery.jsonpCalendarFn"></script><script type="text/javascript" charset="utf-8" async="" src="//m.ctrip.com/restapi/soa2/12378/json/getGeneralConfigData?key=Holiday&amp;callback=cQuery.jsonpCalendarFn"></script><script type="text/javascript" charset="utf-8" async="" src="/Domestic/Tool/AjaxGetHotKeyword.aspx?cityid=2"></script><script type="text/javascript" charset="utf-8" async="" src="/Domestic/Tool/AjaxGetCitySuggestion.aspx"></script><script type="text/javascript" charset="utf-8" src="/domestic/cas/oceanball?callback=CASBiKGCyFeZycaccS&amp;_=1537517654290"></script><script type="text/javascript" charset="utf-8" src="/domestic/cas/oceanball?callback=CASaYTWrQGqqLpYbSn&amp;_=1537517654289"></script><script type="text/javascript" id="rmsd__script" async="" src="http://webresource.c-ctrip.com/resaresonline/risk/ubtrms/d.min.de4b6bfc.js" crossorigin="anonymous"></script><script type="text/javascript" charset="utf-8" async="" src="//cpro.baidu.com/cpro/ui/rt.js"></script><script type="text/javascript" charset="utf-8" src="http://webresource.c-ctrip.com/code/cquery/mod/jmp-1.0.js"></script><script type="text/javascript" charset="utf-8" src="http://webresource.c-ctrip.com/code/cquery/mod/address-1.0_calendar-6.0_dropBox-1.0_notice-1.0_tab-1.2_validate-1.1.js"></script><script type="text/javascript" charset="utf-8" src="http://webresource.c-ctrip.com/code/cquery/mod/sideBar-2.0.js"></script><script type="text/javascript" charset="utf-8" src="http://webresource.c-ctrip.com/code/cquery/mod/animate-1.0.js"></script><script type="text/javascript" async="" src="http://webresource.c-ctrip.com/ResCRMOnline/R1/js/float/headFloat.min.js?v=20160329"></script><script type="text/javascript" async="" src="http://webresource.c-ctrip.com/ResUnionOnline/R3/float/pcfloat.min.js?v=20160329"></script><script type="text/javascript" charset="utf-8" async="" defer="defer" crossorigin="anonymous" src="https://webresource.c-ctrip.com/ResUnionOnline/R1/common/marinRedirect.js?v=20180921"></script><script type="text/javascript" charset="utf-8" async="" defer="defer" crossorigin="anonymous" src="https://webresource.c-ctrip.com/resaresonline/risk/ubtrms/latest/default/rms.js?v=20180921"></script><script charset="utf-8" src="http://webresource.c-ctrip.com/ResHotelOnline/R8/search/js.merge/showhotelinformation.js?releaseno=2018-09-20-02-02-00"></script><script charset="utf-8" src="http://webresource.c-ctrip.com/ResHotelOnline/R8/search/js.merge/base-bmap.js?releaseno=2018-09-20-02-02-00"></script><script charset="utf-8" src="http://webresource.c-ctrip.com/reshotelcasonline/R6/js/butterfly.js?releaseno=2018-09-20-02-02-00"></script><script charset="utf-8" src="http://webresource.c-ctrip.com/code/cquery/cQuery_110421.js"></script><meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>上海小南国花园酒店预订价格,联系电话\位置地址【携程酒店】</title>
<meta name="keywords" content="上海小南国花园酒店,上海小南国花园酒店电话,上海小南国花园酒店地址,上海小南国花园酒店价格查询" />
<meta name="description" content="上海小南国花园酒店官网联合预订,携程酒店提供上海小南国花园酒店价格查询,涵盖上海小南国花园酒店电话、服务设施、地址交通及周边酒店信息,鲜活的上海小南国花园酒店网友真实点评、酒店图片等信息。网上订上海小南国花园酒店,来携程享受有房保证!" />
<meta http-equiv="x-dns-prefetch-control" content="on" /><meta http-equiv="X-UA-Compatible" content="IE=edge" /><link rel="dns-prefetch" href="//webresource.c-ctrip.com" /><link rel="dns-prefetch" href="//pic.c-ctrip.com" /><link rel="dns-prefetch" href="//s.c-ctrip.com" /><link rel="apple-touch-startup-image" href="//pic.c-ctrip.com/h5/common/640.png" sizes="320x460" /><link rel="apple-touch-startup-image" href="//pic.c-ctrip.com/h5/common/940.png" sizes="640x920" /><link rel="apple-touch-startup-image" href="//pic.c-ctrip.com/h5/common/1004.png" sizes="768x1004" /><link rel="apple-touch-icon-precomposed" sizes="57x57" href="//pic.c-ctrip.com/h5/common/57.png" /><link rel="apple-touch-icon-precomposed" sizes="72x72" href="//pic.c-ctrip.com/h5/common/72.png" /><link rel="apple-touch-icon-precomposed" sizes="114x114" href="//pic.c-ctrip.com/h5/common/114.png" /><link rel="apple-touch-icon-precomposed" sizes="144x144" href="//pic.c-ctrip.com/h5/common/144.png" />
<meta content="all" name="robots" />
<meta name="robots" content="index,follow" />
<meta name="location" content="province=上海;city=上海" />

 <link href="//webresource.c-ctrip.com/ResHotelOnline/R8/search/css/pri_detail.css?releaseno=2018-09-20-02-02-00" rel="stylesheet" type="text/css" />
  <script type="text/javascript" charset="utf-8" async="" src="http://webresource.c-ctrip.com/code/ubt/_bfa.min.js?v=20188_21.js"></script><script src="//webresource.c-ctrip.com/ResHotelOnline/R8/search/js.min/raphael.js?releaseno=2018-09-20-02-02-00" type="text/javascript"></script>
<style>
.J_bp
{
margin-right: -1.5px;
margin-left:1.5px;
display: inline;
}
svg { margin: 0; display: inline;}
vml,rvml { margin: 0; display: inline;}
</style>
<style>
.gl-mask {
    position: fixed;
    _position: absolute;
    background:rgba(0,0,0,0.5);
    filter: progid:DXImageTransform.Microsoft.gradient(startcolorstr=#7F000000,endcolorstr=#7F000000);
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: 30;
}

.gl-mask-content {
    position: absolute !important;
    display: block;
    background-color: white;
    left: 50%; top: 50%;
    margin-left: -429px;
}

.gl-hidden {
    display: none;
}
stylebold { font-weight:bold; }
</style>
<script charset="UTF-8" type="text/javascript" src="//webresource.c-ctrip.com/ares2/infosec/captcha/~2.5.0/default/js/captcha.min.js?expires=1d"></script><script charset="UTF-8" type="text/javascript" src="//webresource.c-ctrip.com/ares2/basebiz/countryCode/~1.1.4/default/country.online.js"></script><script charset="UTF-8" type="text/javascript" src="//webresource.c-ctrip.com/ares2/basebiz/accountsresource/~0.0.6/default/js/module/realname.min.js?expires=1d"></script><link href="//webresource.c-ctrip.com/ResCRMOnline/R6/member/common/css/login_popup_new.css?20150305" rel="stylesheet" type="text/css" /><script type="text/javascript" async="" src="https://accounts.ctrip.com/member/ajax/AjaxGetCookie.ashx?jsonp=BuildHTML&amp;r=0.3348465360617803&amp;encoding=0"></script><script type="text/javascript" src="http://webresource.c-ctrip.com/ResUnionOnline/R3/float/qCode.min.js"></script><script type="text/javascript" src="http://webresource.c-ctrip.com/ResUnionOnline/R3/float/yUtil.min.js"></script><script type="text/javascript" src="http://webresource.c-ctrip.com/ResUnionOnline/R3/float/floating_normal.min.js?20180921"></script><link type="text/css" rel="stylesheet" href="//webresource.c-ctrip.com/ResUnionOnline/R3/float/css/pc_flaot.css" /><noscript><div style="display: inline;"><img width="1" height="1" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/1066331136/?value=0&amp;label=cG9hCIyRngMQgNi7_AM&amp;guid=ON&amp;script=0" style="border: none;" /></div></noscript><script type="text/javascript" id="conversion_google" src="//www.googleadservices.com/pagead/conversion_async.js"></script><script type="text/javascript">if(window.google_trackConversion){window.google_trackConversion({google_conversion_id: 1066331136, google_custom_params: {"hrental_id":"428365","hrental_totalvalue":"0","hrental_pagetype":"offerdetail"},google_remarketing_only: true})};</script><script src="https://googleads.g.doubleclick.net/pagead/viewthroughconversion/1066331136/?random=1537517661689&amp;cv=9&amp;fst=1537517661689&amp;num=1&amp;guid=ON&amp;resp=GooglemKTybQhCsO&amp;u_h=864&amp;u_w=1536&amp;u_ah=824&amp;u_aw=1536&amp;u_cd=24&amp;u_his=2&amp;u_tz=480&amp;u_java=false&amp;u_nplug=3&amp;u_nmime=4&amp;data=hrental_id%3D428365%3Bhrental_totalvalue%3D0%3Bhrental_pagetype%3Dofferdetail&amp;sendb=1&amp;frm=0&amp;url=http%3A%2F%2Fhotels.ctrip.com%2Fhotel%2F428365.html&amp;tiba=%E4%B8%8A%E6%B5%B7%E5%B0%8F%E5%8D%97%E5%9B%BD%E8%8A%B1%E5%9B%AD%E9%85%92%E5%BA%97%E9%A2%84%E8%AE%A2%E4%BB%B7%E6%A0%BC%2C%E8%81%94%E7%B3%BB%E7%94%B5%E8%AF%9D%5C%E4%BD%8D%E7%BD%AE%E5%9C%B0%E5%9D%80%E3%80%90%E6%90%BA%E7%A8%8B%E9%85%92%E5%BA%97%E3%80%91&amp;async=1&amp;rfmt=3&amp;fmt=4"></script></head>

<body id="mainbody" itemscope="" itemtype="//schema.org/WebPage"><iframe scrolling="no" frameborder="0" src="http://cms.gtags.net/w?a=9" style="width: 1px; height: 1px; position: fixed; left: 0px; top: 0px; margin: 0px; padding: 0px; z-index: 2147483647;"></iframe><container style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px; z-index: 100;"><div id="_dropBoxTemp_" style="display: none;"></div></container>
<link rel="canonical" href="http://hotels.ctrip.com/hotel/428365.html" />
<link href="" rel="Stylesheet" type="text/css" id="oldIeCss" />

    <div id="jsContainer" class="jsContainer" style="height:0">
                                <textarea id="jsSaveStatus" style="display:none;"></textarea>
                                <div id="tuna_alert" style="display:none;position:absolute;z-index:999;overflow:hidden;"></div>
                                <div id="tuna_jmpinfo" style="visibility:hidden;position:absolute;z-index:120;"></div>
                                <div style="position: var absolute;top:0; z-index: 120;display:none" id="tuna_calendar" class="tuna_calendar"></div>
                                </div> 
    <input type="hidden" id="CorrelationId" name="CorrelationId" value="127919519883468016" /><link href="//webresource.c-ctrip.com/ResCRMOnline/R1/pageheader/css/PageHeader_v2.css?temp=1536663141" rel="stylesheet" /><div class="cui_hd_cont">
  <div id="cui_hd" class="cui_hd"><input type="hidden" id="_searchboxNo_" value="ws_www20140409" /><input type="hidden" id="_newHeaderFlag_" value="true" /><div class="ctriplogo"><a title="携程旅行网" href="http://www.ctrip.com">携程旅行网</a></div>
    <div class="nav-bar">
      <ul class="language">
        <li><a href="http://www.ctrip.com/" rel="nofollow" class="selected" id="cui_lang_cn" onmouseover="this.className= 'selected language_current';document.getElementById('cui_lang_list').parentNode.style.display='block';" onmouseout="this.className= 'selected';document.getElementById('cui_lang_list').parentNode.style.display='none';"><span><em class="ico-global"></em>Language<b class="arrow"></b></span></a><div class="language_wrap drowndrop" style="display: none;" onmouseover="document.getElementById('cui_lang_cn').className= 'selected language_current';this.style.display='block';" onmouseout="document.getElementById('cui_lang_cn').className= 'selected';this.style.display='none';">
            <ul class="language_list" id="cui_lang_list">
              <li class="active"><a id="ctrip_cn" class="language_big5" href="//www.ctrip.com">简体中文</a></li>
              <li><a id="ctrip_eng" class="language_en" href="https://www.trip.com/?locale=en_US">English (United States)</a></li>
              <li><a id="ctrip_uk" class="language_gb" href="https://uk.trip.com/?locale=en_gb">English (United Kingdom)</a></li>
              <li><a id="ctrip_hk" class="language_hk" href="http://hk.trip.com/?locale=zh_hk">繁體中文 (香港)</a></li>
              <li><a id="ctrip_hk_en" class="language_hk" href="https://hk.trip.com/?locale=en_hk">English(Hong Kong)</a></li>
              <li><a id="ctrip_korea" class="language_korea" href="https://kr.trip.com/?locale=ko_KR">韩语版</a></li>
              <li><a id="ctrip_jap" class="language_jap" href="https://jp.trip.com/?locale=ja_JP">日语版</a></li>
              <li><a id="ctrip_sg" class="language_sg" href="https://sg.trip.com/?locale=en_SG">English (Singapore)</a></li>
              <li><a id="ctrip_au" class="language_au" href="https://au.trip.com/?locale=en_au">English (Australia)</a></li>
              <li><a id="ctrip_de" class="language_de" href="https://de.trip.com/?locale=de_DE">Deutsch</a></li>
              <li><a id="ctrip_fr" class="language_fr" href="https://fr.trip.com/?locale=fr_FR">Français</a></li>
              <li><a id="ctrip_es" class="language_es" href="https://es.trip.com/?locale=es_ES">Español</a></li>
              <li><a id="ctrip_it" class="language_it" href="https://it.trip.com/?locale=it_IT">Italiano</a></li>
              <li class="last"><a id="ctrip_ru" class="language_ru" href="https://ru.trip.com/?locale=ru_RU">Русский</a></li>
              <li><a id="ctrip_th" class="language_th" href="https://th.trip.com/?locale=th_TH">泰国站</a></li>
              <li><a id="ctrip_id" class="language_id" href="https://id.trip.com/?locale=id_ID">Bahasa Indonesia</a></li>
              <li><a id="ctrip_my" class="language_my" href="https://my.trip.com/?locale=ms_MY">Bahasa Malaysia</a></li>
              <li><a id="ctrip_my_en" class="language_my" href="https://my.trip.com/?locale=en_my">English (Malaysia)</a></li>
            </ul>
          </div>
        </li>
      </ul>
      <ul class="cui_service">
        <li><a target="_blank" rel="nofollow" href="http://kefu.ctrip.com">客服中心</a></li>
      </ul>
      <ul class="cui_service service_1180">
        <li id="cui_service_cn">
        <a class="service_tel"><span>境内：<em class="service_telnum">400-830-6666</em><b class="arrow"></b></span></a><div class="service_wrap drowndrop"><ul class="service_list"><li><dl><dd><span style="color:#999">（或）</span><em>400-820-6666</em></dd><dd>香港（中国）：<em>+ 852-3069-9966</em></dd><dd>境外：<em>+ 86-21-3406-4888</em></dd></dl></li></ul></div></li>
      </ul>
      <ul class="cui_wireless" id="head_float_level">
        <li><a href="http://app.ctrip.com" class="wireless wireless_link" target="_blank" rel="nofollow" id="linkid"><i class="cui_ico_app"></i></a><div id="head_float_box_app" class="cui_wireless_box" style="display: none;"><i class="cui_ico_chatarrow" style="right:40px;"></i><div class="cui_wireless_inbox">
              <dl class="cui_wireless_type">
                <dt>手机扫码快速下载</dt>
                <dd><img src="//pic.c-ctrip.com/platform/online/home/er_ctrip_app.jpg" alt="" /></dd>
              </dl><a href="http://app.ctrip.com" class="cui_link_app">携程旅行手机版<i>&gt;</i></a></div>
          </div>
        </li>
        <li><a href="##" class="wireless wireless_nolink" id="nolinkid"><i class="cui_ico_wechat cui_ico_wechat_gif"></i></a><div id="head_float_box_weixin" class="cui_wireless_box" style="display: none;"><i class="cui_ico_chatarrow"></i><div class="cui_wireless_inbox">
              <dl class="cui_wireless_type">
                <dt>携程订阅号:helloctrip</dt>
                <dd><img src="//pic.c-ctrip.com/platform/online/home/er_ctrip_wechat.jpg" alt="" /></dd>
              </dl>扫一扫,领旅行福利</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</div>
<div id="cui_nav">
  <div class="base_nav">
    <ul id="cui_nav_ul" class="cui_nav cui_content">
      <li id="cui_c_ph_hp"><a id="c_ph_hp" class="cui_nav_non" href="http://www.ctrip.com/">首页</a></li>
      <li class="divider "></li>
      <li id="cui_nav_hotel" class="cui_nav_current"><a id="nav_hotel" class="cui_nav_has" href="http://hotels.ctrip.com/">酒店<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_hotel" class="cui_sub_nav">
            <li id="ul_c_ph_hotel_h"><a id="c_ph_hotel_h" class="cui_sub_current" href="http://hotels.ctrip.com/">国内酒店</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_hoteli_h"><a id="c_ph_hoteli_h" href="http://hotels.ctrip.com/international/">海外酒店</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_apartment_h"><a id="c_ph_apartment_h" href="http://hotels.ctrip.com/apartment">海外民宿+短租</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_tuan_h"><a id="c_ph_tuan_h" href="http://tuan.ctrip.com">团购</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_hotsale_h"><a id="c_ph_hotsale_h" href="http://hotels.ctrip.com/hotsale">特价酒店</a></li>
            <li class="divider " style=""></li>
            <li id="ul_c_ph_tujia_h"><a id="c_ph_tujia_h" style="" rel="nofollow" href="http://hotels.ctrip.com/tujia/">途家公寓</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_taocanj_h"><a id="c_ph_taocanj_h" href="http://taocan.ctrip.com/sh/HotelDefault.aspx?fluxentrance=10405&amp;FromMenu=hotel">酒店+景点</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_inn_h"><a id="c_ph_inn_h" href="http://inn.ctrip.com">客栈民宿</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_meetingroom_h"><a id="c_ph_meetingroom_h" href="http://meeting.ctrip.com/?channel=0#ctm_ref=mtg_meetingroom_2dh">团队房•长住房</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_meeting_h"><a id="c_ph_meeting_h" href="http://meeting.ctrip.com/?channel=1#ctm_ref=mtg_meeting_2dh">会议</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://my.ctrip.com/Home/Order/HotelOrderList.aspx"><i class="cui-icon-hotel"></i>酒店订单 &gt;</a></div>
      </li>
      <li class="divider "></li>
      <li id="cui_nav_vac"><a id="nav_vac" class="cui_nav_has" href="http://vacations.ctrip.com/">旅游<span class="label-cn" id="ACT_Label_97" style="display:none"><em>十一游</em><i class="triangle"></i></span><i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_vac" class="cui_sub_nav">
            <li id="ul_c_ph_vacations_v"><a id="c_ph_vacations_v" href="http://vacations.ctrip.com/">旅游首页<span class="label-cn" id="ACT_Label_101" style=""><em>199游周边</em><i class="triangle"></i></span></a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_around_v"><a id="c_ph_around_v" href="http://weekend.ctrip.com/around/">周末游</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_vacationsd_v"><a id="c_ph_vacationsd_v" href="http://vacations.ctrip.com/grouptravel/">跟团游</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_taocan_v"><a id="c_ph_taocan_v" href="http://taocan.ctrip.com/">自由行</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_cruise_v"><a id="c_ph_cruise_v" href="http://cruise.ctrip.com/">邮轮</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_taocanj_v"><a id="c_ph_taocanj_v" href="http://taocan.ctrip.com/sh/">酒店+景点</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_huodong_v"><a id="c_ph_huodong_v" href="http://huodong.ctrip.com/">当地玩乐</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_zhutiyou_v"><a id="c_ph_zhutiyou_v" href="http://vacations.ctrip.com/themetravel/">主题游</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_baotuan_v"><a id="c_ph_baotuan_v" href="http://vacations.ctrip.com/dingzhi">定制旅行</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_youxue_v"><a id="c_ph_youxue_v" href="http://vacations.ctrip.com/youxue">游学</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_visa_v"><a id="c_ph_visa_v" href="http://vacations.ctrip.com/visa">签证</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_mice_v"><a id="c_ph_mice_v" href="http://mice.ctrip.com">企业会奖</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_hh_v"><a id="c_ph_hh_v" target="_blank" rel="nofollow" href="http://www.hhtravel.com/#ctm_ref=hh_ct_thp_nav">高端游</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_golf_v"><a id="c_ph_golf_v" href="http://fun.iwanoutdoor.com/">爱玩户外</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_insurance_v"><a id="c_ph_insurance_v" href="http://vacations.ctrip.com/insurance">保险</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_deals_v"><a id="c_ph_deals_v" href="http://vacations.ctrip.com/deals">特卖汇</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://my.ctrip.com/Home/Order/PkgOrderList.aspx"><i class="cui-icon-vacations"></i>旅游订单 &gt;</a></div>
      </li>
      <li class="divider divider_spec"></li>
      <li id="cui_nav_gentuan"><a id="nav_gentuan" class="cui_nav_non" dividerclass="divider_spec" href="http://vacations.ctrip.com/grouptravel">跟团游</a></li>
      <li class="divider "></li>
      <li id="cui_nav_flight"><a id="nav_flight" class="cui_nav_has" href="https://flights.ctrip.com/">机票<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_flight" class="cui_sub_nav">
            <li id="ul_c_ph_flights_f"><a id="c_ph_flights_f" href="https://flights.ctrip.com">国内机票</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_flightsi_f"><a id="c_ph_flightsi_f" href="https://flights.ctrip.com/international/">国际•港澳台机票</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_fuzzy_f"><a id="c_ph_fuzzy_f" href="https://flights.ctrip.com/fuzzy/#ctm_ref=ctr_nav_flt_fz_pgs">特价机票</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_taocan_f"><a id="c_ph_taocan_f" href="http://taocan.ctrip.com">机+酒</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_flightstoolbox_f"><a id="c_ph_flightstoolbox_f" href="http://flights.ctrip.com/actualtime">航班动态</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_bookseat_f"><a id="c_ph_bookseat_f" rel="nofollow" href="https://flights.ctrip.com/domestic/checkinseat/index">值机选座</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_flightorderlist_f"><a id="c_ph_flightorderlist_f" rel="nofollow" href="https://my.ctrip.com/Home/Order/FlightOrderList.aspx">退票改签</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_airportguides_f"><a id="c_ph_airportguides_f" rel="nofollow" href="https://flights.ctrip.com/booking/airport-guides.html">机场攻略</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_airbus_f"><a id="c_ph_airbus_f" href="http://airbus.ctrip.com/#ctm_ref=arb_hp_flt_nang">机场巴士</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://my.ctrip.com/Home/Order/FlightOrderList.aspx"><i class="cui-icon-flight"></i>机票订单 &gt;</a></div>
      </li>
      <li class="divider "></li>
      <li id="cui_nav_trains"><a id="nav_trains" class="cui_nav_has" href="http://trains.ctrip.com">火车<span class="label-cn" id="ACT_Label_100" style=""><em>抢票</em><i class="triangle"></i></span><i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_trains" class="cui_sub_nav">
            <li id="ul_c_ph_train_t"><a id="c_ph_train_t" href="http://trains.ctrip.com">国内火车票</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_traino_t"><a id="c_ph_traino_t" href="http://rails.ctrip.com">国际•港台火车票</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://my.ctrip.com/Home/Order/RailwayOrderList.aspx"><i class="cui-icon-train"></i>火车票订单 &gt;</a></div>
      </li>
      <li class="divider "></li>
      <li id="cui_nav_destination"><a id="nav_destination" class="cui_nav_has" href="http://bus.ctrip.com/">汽车票<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_destination" class="cui_sub_nav">
            <li id="ul_c_ph_bus_t"><a id="c_ph_bus_t" href="http://bus.ctrip.com/">汽车票</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_airbus_t"><a id="c_ph_airbus_t" href="http://airbus.ctrip.com/#ctm_ref=arb_hp_bus_nang">机场巴士</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_ship_t"><a id="c_ph_ship_t" href="http://bus.ctrip.com/ship/">船票</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_yacht_t"><a id="c_ph_yacht_t" target="_blank" rel="nofollow" href="http://yacht.ctrip.com/">游艇帆船</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_daozy_t"><a id="c_ph_daozy_t" href="http://pages.c-ctrip.com/bus/xicui/201803/dzy/html/pc.html">到站游</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://my.ctrip.com/Home/Order/QicheOrderlist.aspx"><i class="cui-icon-bus"></i>汽车票订单 &gt;</a></div>
      </li>
      <li class="divider "></li>
      <li id="cui_nav_car"><a id="nav_car" class="cui_nav_has" href="http://car.ctrip.com/#ctm_ref=chp_var_txt">用车<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_car" class="cui_sub_nav">
            <li id="ul_c_ph_car_c"><a id="c_ph_car_c" href="http://car.ctrip.com/#ctm_ref=chp_var_txt">用车首页</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_hwzj_c"><a id="c_ph_hwzj_c" href="http://car.ctrip.com/hwzijia#ctm_ref=chp_var_txt">境外租车</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_hwdaijia_c"><a id="c_ph_hwdaijia_c" href="http://car.ctrip.com/hwdaijia#ctm_ref=chp_var_txt">境外接送机</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_hwrizu_c"><a id="c_ph_hwrizu_c" href="http://car.ctrip.com/line/index">境外包车</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_zj_c"><a id="c_ph_zj_c" href="http://car.ctrip.com/zijia#ctm_ref=chp_var_txt">国内租车</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_daijia_c"><a id="c_ph_daijia_c" href="http://car.ctrip.com/daijia#ctm_ref=chp_var_txt">国内接送机/火车</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_rizu_c"><a id="c_ph_rizu_c" href="http://car.ctrip.com/idayweb">国内包车</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://my.ctrip.com/Home/Order/CarOrderList.aspx"><i class="cui-icon-car"></i>用车订单 &gt;</a></div>
      </li>
      <li class="divider "></li>
      <li id="cui_nav_ticket"><a id="nav_ticket" class="cui_nav_has" href="http://piao.ctrip.com/">门票<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_ticket" class="cui_sub_nav">
            <li id="ul_c_ph_piao_p"><a id="c_ph_piao_p" href="http://piao.ctrip.com/?clear=t#ctm_ref=tkt_home_tab_inland">境内门票</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_piaooversea_p"><a id="c_ph_piaooversea_p" href="http://piao.ctrip.com/oversea#ctm_ref=tkt_home_tab_oversea">出境•港澳台门票</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_huodong_p"><a id="c_ph_huodong_p" href="http://huodong.ctrip.com#ctm_ref=ctr_hp_ttd">当地玩乐</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_wifi_p"><a id="c_ph_wifi_p" href="http://huodong.ctrip.com/wifi#ctm_ref=ctr_hp_wifi">出境WiFi•电话卡</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_around_p"><a id="c_ph_around_p" href="http://you.ctrip.com/around#ctm_ref=gs-990123-290801-0-02-M001|0|0">周末游</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_disney_p"><a id="c_ph_disney_p" href="http://pages.c-ctrip.com/ttd/manu/201712/changlong/online/index.html">长隆</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_park_p"><a id="c_ph_park_p" href="http://parking.ctrip.com">机场停车</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://my.ctrip.com/Home/Order/LocalUnionOrderList.aspx"><i class="cui-icon-ticket"></i>门票玩乐订单 &gt;</a></div>
      </li>
      <li class="divider "></li>
      <li id="cui_nav_tuan"><a id="nav_tuan" class="cui_nav_has" href="http://tuan.ctrip.com">团购<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_tuan" class="cui_sub_nav">
            <li id="ul_c_ph_tuan_tu"><a id="c_ph_tuan_tu" href="http://tuan.ctrip.com">团购首页</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_tuanhotel_tu"><a id="c_ph_tuanhotel_tu" href="http://tuan.ctrip.com/hotel/">酒店</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_tuanticket_tu"><a id="c_ph_tuanticket_tu" href="http://tuan.ctrip.com/ticket/">门票</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_tuantravel_tu"><a id="c_ph_tuantravel_tu" href="http://tuan.ctrip.com/travel/">旅游</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_tuanlife_tu"><a id="c_ph_tuanlife_tu" href="http://tuan.ctrip.com/life/">美食</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://my.ctrip.com/Home/Order/GroupOrderList.aspx"><i class="cui-icon-tuan"></i>团购订单 &gt;</a></div>
      </li>
      <li class="divider "></li>
      <li id="cui_c_ph_you"><a id="c_ph_you" class="cui_nav_non" href="http://you.ctrip.com/">攻略</a></li>
      <li class="divider "></li>
      <li id="cui_nav_g"><a id="nav_g" class="cui_nav_has" href="http://g.ctrip.com/">全球购<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_g" class="cui_sub_nav">
            <li id="ul_c_ph_mdg_g"><a id="c_ph_mdg_g" href="http://g.ctrip.com/">名店购</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_ts_g"><a id="c_ph_ts_g" href="http://tax.ctrip.com/?bid=2&amp;cid=1&amp;pid=1">退税</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_ylth_g"><a id="c_ph_ylth_g" href="http://g.ctrip.com/gsmarketingactive/unionpay?ctm_ref=M_gw_3home_paypal_cl">银联特惠</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_skjl_g"><a id="c_ph_skjl_g" href="http://card.ctrip.com/#ctm_ref=ctr_bid_0_cid_1_pid_1">万千赏</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_forex_g"><a id="c_ph_forex_g" href="http://forex.ctrip.com/?bid=62&amp;1=1">外币兑换</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://forex.ctrip.com/order/list/"><i class="cui-icon-foreign"></i>外币兑换订单 &gt;</a></div>
      </li>
      <li class="divider "></li>
      <li id="cui_nav_lpk"><a id="nav_lpk" class="cui_nav_has" href="http://lipin.ctrip.com">礼品卡<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_lpk" class="cui_sub_nav">
            <li id="ul_c_ph_lipin_l"><a id="c_ph_lipin_l" href="http://lipin.ctrip.com">礼品卡首页</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_xcb_l"><a id="c_ph_xcb_l" href="http://lipin.ctrip.com/xcb">礼品卡福袋</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_lipincorp_l"><a id="c_ph_lipincorp_l" href="http://jr.ctrip.com/cms/PC-1220">企业购卡</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_ckzm_l"><a id="c_ph_ckzm_l" href="http://jr.ctrip.com/deposit/deposit/index">存款证明</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_dhq_l"><a id="c_ph_dhq_l" href="http://lipin.ctrip.com/voucher">兑换券</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_forexlipin_l"><a id="c_ph_forexlipin_l" href="http://forex.ctrip.com/?bid=12&amp;1=1">外币兑换</a></li>
          </ul><a class="cui_ico_order" rel="nofollow" href="http://my.ctrip.com/Home/Order/TicketOrderList.aspx"><i class="cui-icon-card"></i>礼品卡订单 &gt;</a></div>
      </li>
      <li class="divider "></li>
      <li id="cui_nav_sl"><a id="nav_sl" class="cui_nav_has" href="http://ct.ctrip.com/#ctm_ref=xcct">商旅<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_sl" class="cui_sub_nav">
            <li id="ul_c_ph_slsy_s"><a id="c_ph_slsy_s" href="http://ct.ctrip.com/#ctm_ref=xcct">商旅首页</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_chl_s"><a id="c_ph_chl_s" href="http://ct.ctrip.com/crptravel/default/landing#ctm_ref=xcpt">企业差旅平台</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_hj_s"><a id="c_ph_hj_s" href="http://mice.ctrip.com">会议旅游</a></li>
          </ul>
        </div>
      </li>
      <li class="divider divider_spec"></li>
      <li id="cui_nav_cruise"><a id="nav_cruise" class="cui_nav_non" dividerclass="divider_spec" href="http://cruise.ctrip.com">邮轮</a></li>
      <li class="divider "></li>
      <li id="cui_nav_more"><a id="nav_more" class="cui_nav_has" rel="nofollow" href="http://mall.ctrip.com">更多<i class="cui_ico_triangle"></i><span class="point"></span></a><div class="cui_subnav_wrap">
          <ul id="ul_nav_more" class="cui_sub_nav">
            <li id="ul_c_ph_ypsc_m"><a id="c_ph_ypsc_m" href="http://mall.ctrip.com">优品商城</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_sjhy_m"><a id="c_ph_sjhy_m" href="http://pages.ctrip.com/marketing/2017/07/svip/index.html?pushcode=act_svip_pc33&amp;qrcode=act_svip_pc37">超级会员</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_cards_m"><a id="c_ph_cards_m" rel="nofollow" href="http://cards.ctrip.com">合作卡</a></li>
            <li class="divider "></li>
            <li id="ul_c_ph_xcyd_m"><a id="c_ph_xcyd_m" href="https://sport.ctrip.com/">携程运动</a></li>
          </ul>
        </div>
      </li>
      <li id="loginDivLi" class="cui_nav_myctrip cui_content">
        
        <ul class="cui_myctrip_log" style="display: block;" id="ulCTMinMC">
          <li class="userLogin" id="div_User"><a rel="nofollow" id="c_ph_login" class="cui_links_login" href="https://passport.ctrip.com/user/login?BackUrl=http%3A%2F%2Fhotels.ctrip.com%2Fhotel%2F428365.html">登录</a><span>|</span><a rel="nofollow" id="c_ph_register" href="https://passport.ctrip.com/user/reg/home" class="cui_links_reg">注册</a></li>
          <li class="myctrip" style="margin-top:0;clear:left;"><span id="div_MyCtrip"><a rel="nofollow" id="c_ph_myhome" href="http://my.ctrip.com/home/myinfo.aspx#ctm_ref=ssc_hp_myctrip_a" class="cui_myctrip_status">我的携程<b class="arrow"></b></a></span><ul class="cui_account cui_account_login" id="loginDiv" style="display:none;">
              <li>
                <div id="div_Loginbtn"><input type="button" onclick="DoLogin()" id="myctripButton" class="basebtns_01" value="登录" /></div>
              </li>
              <li class="cui_account_info"><a rel="nofollow" href="http://my.ctrip.com/home/Order/AllOrder.aspx#ctm_ref=ssc_hp_myctrip_allorders_a">全部订单</a></li>
              <li><a rel="nofollow" class="gray" href="https://passport.ctrip.com/user/member/fastOrder#ctm_ref=ssc_hp_myctrip_phoneorders_a">手机号查订单</a></li>
            </ul>
          </li>
          <li class="message" id="div_MyCTMessages"></li>
        </ul>
      </li>
    </ul>
  </div>
  <div id="nav_bh" class="cui_nav_behind" style="display:none;height:0px;"></div>
</div>
<div id="ActConfig_ID" style="display:none">[{"id":"1","onlinetime":"2016/07/01 00:00:00$2016/08/01 00:00:00"},{"id":"3","onlinetime":"2016/04/12 00:00:00$2016/07/01 00:00:00"},{"id":"4","onlinetime":"2016/04/12 00:00:00$2016/07/01 00:00:00"},{"id":"5","onlinetime":"2016/06/01 00:00:00$2016/06/26 00:00:00"},{"id":"6","onlinetime":"2016/04/12 00:00:00$2016/07/01 00:00:00"},{"id":"7","onlinetime":"2016/06/26 00:00:00$2016/07/18 00:00:00"},{"id":"8","onlinetime":"2016/07/18 00:00:00$2016/08/09 00:00:00"},{"id":"9","onlinetime":"2016/06/17 00:00:00$2016/08/31 00:00:00"},{"id":"12","onlinetime":"2016/07/06 00:00:00$2016/08/06 00:00:00"},{"id":"13","onlinetime":"2016/08/09 00:00:00$2016/08/30 23:59:59"},{"id":"14","onlinetime":"2016/07/27 17:30:14$2016/08/27 23:59:59"},{"id":"16","onlinetime":"2016/08/31 00:00:00$2016/09/30 23:59:59"},{"id":"17","onlinetime":"2016/09/15 00:00:00$2016/09/30 23:59:59"},{"id":"18","onlinetime":"2016/09/05 00:00:00$2016/09/16 23:59:59"},{"id":"19","onlinetime":"2016/09/19 00:00:00$2016/09/23 23:59:59"},{"id":"20","onlinetime":"2016/10/01 00:00:00$2016/10/30 23:59:59"},{"id":"21","onlinetime":"2017/06/23 00:00:00$2099/12/31 23:59:59"},{"id":"22","onlinetime":"2016/09/26 00:00:00$2016/10/26 23:59:59"},{"id":"23","onlinetime":"2016/10/18 00:00:00$2016/10/30 23:59:59"},{"id":"24","onlinetime":"2016/11/01 00:00:00$2016/12/01 23:59:59"},{"id":"25","onlinetime":"2016/11/01 00:00:00$2016/12/01 23:59:59"},{"id":"26","onlinetime":"2016/11/01 00:00:00$2016/11/11 23:59:59"},{"id":"27","onlinetime":"2016/10/18 00:00:00$2016/10/30 23:59:59"},{"id":"28","onlinetime":"2016/12/13 00:00:00$2017/02/20 23:59:59"},{"id":"29","onlinetime":"2016/12/28 17:28:32$2017/01/28 23:59:59"},{"id":"30","onlinetime":"2016/12/01 00:00:00$2016/12/12 23:59:59"},{"id":"31","onlinetime":"2016/12/02 00:00:00$2016/12/12 23:59:59"},{"id":"32","onlinetime":"2016/12/13 17:33:15$2017/01/13 23:59:59"},{"id":"33","onlinetime":"2016/12/22 11:19:01$2017/12/22 11:19:03"},{"id":"34","onlinetime":"2016/12/22 11:19:01$2017/12/22 11:19:03"},{"id":"35","onlinetime":"2017/02/16 14:19:45$2017/03/15 23:59:59"},{"id":"36","onlinetime":"2017/03/17 00:00:00$2017/03/31 23:59:59"},{"id":"37","onlinetime":"2017/03/17 00:00:00$2017/03/31 23:59:59"},{"id":"38","onlinetime":"2017/03/01 00:00:00$2017/04/01 23:59:59"},{"id":"39","onlinetime":"2017/03/01 00:00:00$2017/04/01 22:59:59"},{"id":"40","onlinetime":"2017/04/01 00:00:00$2017/04/21 23:59:59"},{"id":"41","onlinetime":"2017/04/12 00:00:00$2017/05/12 23:59:59"},{"id":"42","onlinetime":"2017/04/22 00:00:00$2017/05/15 23:59:59"},{"id":"43","onlinetime":"2017/04/22 00:00:00$2017/05/15 23:59:59"},{"id":"44","onlinetime":"2017/05/22 00:00:00$2017/06/22 23:59:59"},{"id":"45","onlinetime":"2017/05/22 00:00:00$2017/05/29 23:59:59"},{"id":"46","onlinetime":"2017/06/01 00:00:00$2017/07/01 23:59:59"},{"id":"47","onlinetime":"2017/07/20 00:00:00$2017/08/19 23:59:59"},{"id":"48","onlinetime":"2017/09/01 15:00:00$2017/09/30 15:00:00"},{"id":"49","onlinetime":"2017/10/01 00:00:00$2017/10/19 23:59:59"},{"id":"50","onlinetime":"2017/10/01 00:00:00$2017/10/19 23:59:59"},{"id":"51","onlinetime":"2017/08/18 00:00:00$2017/08/31 23:59:59"},{"id":"52","onlinetime":"2017/08/18 00:00:00$2017/09/18 23:59:59"},{"id":"53","onlinetime":"2017/08/18 00:00:00$2017/09/17 23:59:59"},{"id":"54","onlinetime":"2017/09/01 00:00:00$2017/09/29 23:59:59"},{"id":"55","onlinetime":"2017/11/12 00:00:00$2017/12/12 23:59:59"},{"id":"56","onlinetime":"2017/10/20 00:00:00$2017/11/11 23:59:59"},{"id":"57","onlinetime":"2017/11/02 00:00:00$2017/11/12 00:00:00"},{"id":"58","onlinetime":"2018/03/16 00:00:00$2018/04/08 23:59:59"},{"id":"59","onlinetime":"2018/03/16 00:00:00$2018/04/08 23:59:59"},{"id":"60","onlinetime":"2017/11/27 00:00:00$2017/12/27 23:59:59"},{"id":"61","onlinetime":"2017/11/27 00:00:00$2017/12/27 23:59:59"},{"id":"62","onlinetime":"2018/01/04 15:00:00$2018/01/17 23:59:59"},{"id":"63","onlinetime":"2018/01/18 00:00:00$2018/02/18 23:59:59"},{"id":"64","onlinetime":"2017/12/21 16:01:03$2018/01/21 23:59:59"},{"id":"65","onlinetime":"2018/01/18 15:31:34$2018/02/18 23:59:59"},{"id":"66","onlinetime":"2018/03/05 00:00:00$2018/03/15 00:00:00"},{"id":"67","onlinetime":"2018/03/16 00:00:00$2018/04/08 00:00:00"},{"id":"68","onlinetime":"2018/03/09 00:00:00$2018/04/09 23:59:59"},{"id":"69","onlinetime":"2018/04/09 00:00:00$2018/05/08 23:59:59"},{"id":"70","onlinetime":"2018/04/08 10:16:57$2018/05/04 00:00:00"},{"id":"71","onlinetime":"2018/04/08 10:17:46$2018/05/04 00:00:00"},{"id":"72","onlinetime":"2018/04/19 00:00:00$2018/05/02 23:59:59"},{"id":"73","onlinetime":"2018/05/04 00:00:00$2018/05/16 23:59:59"},{"id":"74","onlinetime":"2018/05/02 00:00:00$2018/05/16 23:59:59"},{"id":"75","onlinetime":"2018/05/28 17:25:35$2018/06/28 23:59:59"},{"id":"76","onlinetime":"2018/05/28 17:26:43$2018/06/28 23:59:59"},{"id":"77","onlinetime":"2018/06/06 17:12:22$2018/07/02 23:59:59"},{"id":"78","onlinetime":"2018/06/07 09:37:02$2018/07/06 23:59:59"},{"id":"79","onlinetime":"2018/06/12 13:18:44$2018/06/30 23:59:59"},{"id":"80","onlinetime":"2018/06/12 13:18:44$2018/06/30 23:59:59"},{"id":"81","onlinetime":"2018/07/02 00:00:00$2018/08/08 23:59:59"},{"id":"82","onlinetime":"2018/07/02 00:00:00$2018/08/08 23:59:59"},{"id":"83","onlinetime":"2018/06/28 10:39:45$2018/08/31 23:59:59"},{"id":"84","onlinetime":"2018/08/09 00:00:00$2018/08/31 23:59:59"},{"id":"85","onlinetime":"2018/06/30 00:00:00$2018/08/31 23:59:59"},{"id":"86","onlinetime":"2018/07/03 17:33:54$2018/07/31 23:59:59"},{"id":"87","onlinetime":"2018/08/09 00:00:00$2018/08/31 23:59:59"},{"id":"88","onlinetime":"2018/06/28 10:39:45$2018/08/31 23:59:59"},{"id":"89","onlinetime":"2018/07/02 00:00:00$2018/08/08 23:59:59"},{"id":"90","onlinetime":"2018/08/15 00:00:00$2018/09/12 23:59:59"},{"id":"92","onlinetime":"2018/08/22 00:00:00$2018/08/29 00:00:00"},{"id":"93","onlinetime":"2018/09/01 00:00:00$2018/09/09 23:59:59"},{"id":"94","onlinetime":"2018/10/08 00:00:00$2018/10/26 23:59:59"},{"id":"95","onlinetime":"2018/08/09 00:00:00$2018/08/31 23:59:59"},{"id":"96","onlinetime":"2018/09/01 00:00:00$2018/09/09 23:59:59"},{"id":"97","onlinetime":"2018/09/12 00:00:00$2018/09/15 23:59:59"},{"id":"98","onlinetime":"2018/09/12 00:00:00$2018/09/15 23:59:59"},{"id":"99","onlinetime":"2018/09/10 00:00:00$2018/09/12 23:59:59"},{"id":"100","onlinetime":"2018/09/16 00:00:00$2018/10/07 23:59:59"},{"id":"101","onlinetime":"2018/09/12 00:00:00$2018/10/10 23:59:59"},{"id":"c_ph_tujia_h","onlinetime":"2018/01/24 18:00:00$2018/12/31 23:59:59"},{"id":"c_ph_lipinplus_l","onlinetime":"2017/04/21 10:38:46$2017/04/28 00:00:00"}]</div><input type="hidden" id="popfloating_isshow" value="0" /><input type="hidden" id="siteDomainHeadFloat" value="ctrip" /><input type="hidden" id="bsType" value="0" /><input type="hidden" id="formatTel" value="[{'formatTelNum':'400-830-6666','prefix':'境内：','sortIndex':'1','standardTelNum':'4008306666','suffix':''},{'formatTelNum':'400-820-6666','prefix':'（或）','sortIndex':'2','standardTelNum':'4008206666','suffix':''},{'formatTelNum':'+ 852-3069-9966','prefix':'香港（中国）：','sortIndex':'3','standardTelNum':'85230699966','suffix':''},{'formatTelNum':'+ 86-21-3406-4888','prefix':'境外：','sortIndex':'4','standardTelNum':'34064888','suffix':''}]" /><script>
;window.replace=function(){return ''};window.replace=function(){return""};
!function(){window.replace=function(){return""};(function(){var h=document,c=function(a){return h.getElementById(a)},k=null,l=null,m=0,d=[c("cui_nav_hotel"),c("cui_nav_vac"),c("cui_nav_flight"),c("cui_nav_trains"),c("cui_nav_destination"),c("cui_nav_car"),c("cui_nav_ticket"),c("cui_nav_tuan"),c("cui_nav_g"),c("cui_nav_lpk"),c("cui_nav_sl"),c("cui_nav_more")],g={onmouseenter:function(a,b){(h.all?a.onmouseenter=b:a.onmouseover=function(a){(null==a.relatedTarget?b():this!==a.relatedTarget&amp;&amp;20!=this.compareDocumentPosition(a.relatedTarget)&amp;&amp;
b())})},onmouseout:function(a,b){(h.all?a.onmouseleave=b:a.onmouseout=function(a){(null==a.relatedTarget?b():this!==a.relatedTarget&amp;&amp;20!=this.compareDocumentPosition(a.relatedTarget)&amp;&amp;b())})},addEvent:function(a,b,f){(a.addEventListener?a.addEventListener(b,f,!1):(a.attachEvent?a.attachEvent("on"+b,f):a["on"+b]=f))}},e={setTime:function(){g.onmouseenter(c("cui_nav"),function(){setTimeout(function(){m=150},30)});g.onmouseout(c("cui_nav"),function(){m=0})},initEvent:function(){for(var a=0,b=d.length;b&gt;a;a++)(function(){var b=
a;g.onmouseenter(d[b],function(){e.interFn(d[b])});g.onmouseout(d[b],function(){e.outerFn(d[b])})})(a)},reset:function(){for(var a=0,b=d.length;b&gt;a;a++)d[a].className=(-1&lt;d[a].className.indexOf("cui_nav_current")?"cui_nav_current":"")},padReset:function(a){for(var b=0,f=d.length;f&gt;b;b++)(-1&lt;d[b].className.indexOf("cui_nav_current")?d[b].className="cui_nav_current":b!==a&amp;&amp;(d[b].className=""))},interFn:function(a){for(var b=document.getElementById("cui_nav").getElementsByTagName("li"),f="",d=0;d&lt;b.length;d++)b[d].className.match((/cui_nav_current/))&amp;&amp;
(f=b[d]);null!=l&amp;&amp;(clearTimeout(l),l=null);k=setTimeout(function(){e.reset();(-1&lt;a.className.indexOf("cui_nav_current")?f.className="cui_nav_current":(a.className="cui_nav_o",f.className="cui_nav_current cui_nav_unhover"))},m)},outerFn:function(a){for(var b=document.getElementById("cui_nav").getElementsByTagName("li"),d="",c=0;c&lt;b.length;c++)b[c].className.match((/cui_nav_current/))&amp;&amp;(d=b[c]);null!=k&amp;&amp;(clearTimeout(k),k=null);l=setTimeout(function(){e.reset();(-1&lt;a.className.indexOf("cui_nav_current")?
d.className="cui_nav_current":(a.className="",d.className="cui_nav_current"))},250)},initMobile:function(){for(var a=0,b=d.length;b&gt;a;a++)(function(){var b=a,c=d[b].getElementsByTagName("A")[0];c.href="###";c.onmousedown=function(){e.padReset(b);-1===d[b].className.indexOf("cui_nav_current")&amp;&amp;((-1&lt;d[b].className.indexOf("cui_nav_o")?(d[b].className="",document.getElementsByClassName("cui_nav_current")[0].className="cui_nav_current",c.style.visibility="hidden",setTimeout(function(){c.style.visibility=
"visible"},10)):(d[b].className="cui_nav_o",document.getElementsByClassName("cui_nav_current")[0].className="cui_nav_current",document.getElementsByClassName("cui_nav_current")[0].className+=" cui_nav_unhover")))}})(a)},contains:function(a){for(var b=0,c=d.length;c&gt;b;b++)if(0&lt;d[b].compareDocumentPosition(a)-19)return!0;return!1}};c("headStyleId")&amp;&amp;c("headStyleId").parentNode.removeChild(c("headStyleId"));((/ip(hone|od)|ipad/i).test(navigator.userAgent)?(e.initMobile(),g.addEvent(h.body,"click",function(a){e.contains(a.target||
a.srcElement)||e.reset()})):(e.setTime(),e.initEvent()))})()}();
</script>
    <form name="aspnetForm" method="post" action="/Domestic/ShowHotelList.aspx?isvalid=0" id="aspnetForm">
<div>
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTE0NTQ1MTQ4NDBkZA65emF93gZZSRdefqRgr+oGHiYkvaKFDuKtN2XZTSgc" />
</div>

<div>

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="1C6CB54E" />
</div>  
            <input type="hidden" id="J_ServerDate" value="2018-09-21" />
            
    <div id="base_bd">
    <!--右侧底部正在浏览人数-->
    <div id="divViewCount" class="bottom_box" style="position: fixed; bottom: 10px; right: 45px; padding: 0px 15px 0px 25px; line-height: 40px; height: 40px;">
	    有<span id="spanVisitCount">7</span>位客人正在浏览该酒店<a rel="nofollow" id="closeViewCount" href="javascript:void(0);"></a>		
    </div>
    <!--右侧底部正在浏览人数end-->




        <div class="path_bar2" itemprop="breadcrumb">
        <!--打印-收藏-已收藏 -->
        <div class="float_right">   
		    <a href="javascript:;" id="ctl00_MainContentPlaceHolder_lnkCollected" style="display:none" class="ico_faved">已收藏</a>
            
            <a class="ico_correction" href="//my.ctrip.com/uxp/Community/CommunityAdvice.aspx?productType=3&amp;categoryid=65&amp;sourceid=2&amp;hotelid=428365" target="_blank">信息纠错</a>
		    <a class="ico_print" rel="nofollow" href="javascript:print()">打印</a>
        </div>
        <!--酒店导航&&SEO页面的显示 -->
        <a href="/" title="酒店预订">酒店预订</a> &gt; <a href="//hotels.ctrip.com/hotel/Shanghai2" data-dopost="T" title="上海酒店">上海酒店</a> &gt; <a href="//hotels.ctrip.com/hotel/shanghai2/location121" data-dopost="T" title="杨浦区">杨浦区</a> &gt; <h1>上海小南国花园酒店</h1>
    </div>
    
<div class="search_part" id="searchForm">
目的地 <input id="txtCity" name="cityName" type="text" autocomplete="on" class="input_txt input_txtShort" value="上海" _cqnotice="中文/拼音" />
	入住 <input id="txtCheckIn" name="StartTime" class="input_txt input_txtShort" autocomplete="off" type="text" value="2018-09-21" _cqnotice="yyyy-mm-dd" />
	退房 <input id="txtCheckOut" name="DepTime" class="input_txt input_txtShort" autocomplete="off" type="text" value="2018-09-22" _cqnotice="yyyy-mm-dd" />
	
	房间数
	<div id="J_roomCountDiv" class="n_gst n_gstRoom">
		<input id="J_roomCount" type="text" class="n_gst_v" value="1间" readonly="" />
		<i id="J_roomCount_i" class="n_gst_tri"></i>
		<div class="n_gst_p">
			<ul id="J_roomCountList" class="n_gst_num">
			<li>1间</li><li>2间</li><li>3间</li><li>4间</li><li>5间</li><li>6间</li><li>7间</li><li>8间</li><li>9间</li><li>10间</li></ul>
		</div>
	</div>
	住客数 
	<div id="J_RoomGuestInfoDiv" class="n_gst n_gstPeople">
	<input id="J_RoomGuestInfoTxt" type="text" class="n_gst_v" readonly="true" value="1成人" />
	<i id="J_RoomGuestInfoTxt_i" class="n_gst_tri"></i>
	<div class="n_gst_p">
		<ul class="n_gst_list">
			<li class="n_gst_list_opt">
				成人<span class="n_gst_age">18岁及以上</span>
				<span id="J_AdultCount" class="number_control"><span class="number_reduce number_disable"><i class="icon_numreduce"></i></span><input type="text" class="number_input" readonly="" value="1" /><span class="number_plus"><i class="icon_numplus"></i></span></span>
			</li>
			<li class="n_gst_list_opt">
				儿童<span class="n_gst_age">0-17岁</span>
				<span id="J_ChildCount" class="number_control"><span class="number_reduce number_disable"><i class="icon_numreduce"></i></span><input type="text" class="number_input" readonly="" value="0" /><span class="number_plus"><i class="icon_numplus"></i></span></span>
			</li>
		</ul>
		<!-- 儿童人数大于0时显示 -->
		<div id="J_childageValDiv" class="n_gst_childs" style="display: none;">
			<dl class="n_gst_childs_dl">
				<dt>儿童年龄（<span class="J_today"></span>当天）</dt>
				<dd><select class="J_childageVal" id="J_childageVal0" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal1" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal2" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal3" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal4" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal5" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal6" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal7" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal8" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
			</dl>
			<!-- 默认不显示，按需求提示 -->
			<div class="n_gst_childs_tips" style="display:none;">请选择儿童年龄</div>
		</div>
		<div class="n_gst_ft">
			<a id="J_RoomGuestInfoBtnOK" class="n_gst_btn">确定</a>
			<a id="J_RoomGuestInfoBtnCancel" class="n_gst_btncancel">取消</a>
		</div>
	</div>
	</div>
<span data-role="jmp" class="ui_tips_help" data-params="{'options':{'type':'jmp_table','template':'$jmp_table','content':{'txt':'&lt;div class=&quot;jmp_bd&quot;&gt;18周岁及以上为成人。&lt;br/&gt;0-17周岁儿童请参照各酒店入住政策。&lt;/div&gt;'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'hotelDesc'}}"></span>
<input type="hidden" name="RoomGuestCount" id="J_RoomGuestCount" value="1,1,0" />
	
	关键词 <input id="txtKeyword" name="txtKeyword" type="text" autocomplete="on" class="input_txt input_txtLong" _cqnotice="（选填）酒店名/地标/商圈" maxlength="50" placeholder="（选填）酒店名/地标/商圈" />
<input type="button" class="btn_search" value="查看其他酒店" id="btnSearch" />
</div>   
    
      
    <div class="main_detail_wrapper ">
        
            <div id="divDetailMain" class="detail_main detail_main_no_tips">
            

<div class="forward" style="height:1px; width:1px; overflow:hidden">
<img src="//dimg11.c-ctrip.com/images/hotel/373000/372135/c3028fa548b34dd883e187498a1fe26e_R_300_225.jpg" height="1px" width="1px" class="pic1" /><img src="//dimg12.c-ctrip.com/images/200q0u000000jie0g6D8A_R_300_225.jpg" height="1px" width="1px" class="pic2" /><img src="//dimg10.c-ctrip.com/images/200a0k000000budbx4780_R_300_225.jpg" height="1px" width="1px" class="pic3" /><img src="//dimg13.c-ctrip.com/images/200d0k000000buf428360_R_130_130.jpg" height="1px" width="1px" class="pic4" /><img src="//dimg12.c-ctrip.com/images/200u080000003329oEE89_R_130_130.jpg" height="1px" width="1px" class="pic5" /><img src="//dimg10.c-ctrip.com/images/200i0u000000jagom2525_R_130_130.jpg" height="1px" width="1px" class="pic6" /><img src="//dimg11.c-ctrip.com/images/hotel/373000/372135/0dbac627e8fb47ffb8fb8c3d45430946_R_300_225.jpg" height="1px" width="1px" class="pic7" /><img src="//dimg12.c-ctrip.com/images/200q0k000000br7oeE7E6_R_130_130.jpg" height="1px" width="1px" class="pic8" /><img src="//dimg12.c-ctrip.com/images/200p0k000000bpqnfD8D2_R_130_130.jpg" height="1px" width="1px" class="pic9" />
</div>


	<div class="htl_info" id="J_htl_info">
        

		<div class="name" itemtype="//schema.org/Hotel">
            <h2 class="cn_n" itemprop="name"><span class="label_selection">精选</span> 上海小南国花园酒店</h2>
            <h2 class="en_n">WH Ming Hotel Shanghai</h2>
            <span id="ctl00_MainContentPlaceHolder_commonHead_span_hotel_medal" data-role="title" class="medal hotel_strategymedal" title="携程战略合作酒店，拥有优质服务、优良品质及优惠房价，供携程会员专享预订" rstar="6" cpr="0"></span>
            
            <span class="medal ico_quality_gold" title="确认订单更快速，入住过程更顺利，携程服务品质认证。" style="display: inline-block;" id="J_ServiceScoreIcon">品质保障</span>
        </div>
        
		<div class="grade">
            <span id="ctl00_MainContentPlaceHolder_commonHead_imgStar" class="hotel_stars05" title="国家旅游局评定为五星级"></span>
            <div class="special_label"><i class="i_label">休闲度假</i><i class="i_label">亲子酒店</i><i class="i_label">浪漫情侣</i><i class="i_label">商务出行</i><i class="i_label">地铁周边</i><i class="i_orange">环境不错</i> <i class="i_orange">亲子</i></div>
            
        </div>
		<div class="adress" itemprop="address" itemscope="" itemtype="//schema.org/PostalAddress">
            <span id="ctl00_MainContentPlaceHolder_commonHead_lnkCity" target="_blank" itemprop="addressLocality">上海</span> 
            <span id="ctl00_MainContentPlaceHolder_commonHead_lnkLocation" target="_blank">杨浦区</span> 
            <span id="ctl00_MainContentPlaceHolder_commonHead_lbAddress" itemprop="streetAddress">佳木斯路777号</span>
             <span id="ctl00_MainContentPlaceHolder_commonHead_lnkRoadCross" target="_blank">，近营口路。</span>
            【
            <a id="ctl00_MainContentPlaceHolder_commonHead_lnkMapZone" class="detail_add_area" data-dopost="T" href="//hotels.ctrip.com/hotel/Shanghai2/zone368" target="_blank">江湾、五角场商业区</a>
            <a id="ctl00_MainContentPlaceHolder_commonHead_lnkMapZone2" class="detail_add_area" data-dopost="T" href="//hotels.ctrip.com/hotel/Shanghai2/zone871" target="_blank">吴淞口国际邮轮港</a>
            】
            <span class="adress_icon">
            <span id="id_address_icon">            
            </span>
            </span>
        </div>
		<div class="icon_list">
            <a id="linkViewMap" class="icon_list_map view_map" data-hotelid="428365" href="/map/428365.html">交通地图</a><a id="linkViewSoso" href="javascript:;" data-hotelid="428365" class="icon_list_map view_street">周边街景</a>
            <i class="icons-facility32" title="公共区域免费WIFI" data-fid="120" data-role="title"></i><i class="icons-facility03" title="停车场" data-fid="100" data-role="title"></i><i class="icons-facility13" title="餐厅" data-fid="1" data-role="title"></i><i class="icons-facility28" title="接机服务" data-fid="105" data-role="title"></i><i class="icons-facility15" title="游泳池" data-fid="29" data-role="title"></i><i class="icons-facility14" title="健身房" data-fid="42" data-role="title"></i>
            <span id="id_fav_btn">
                <a rel="nofollow" title="收藏酒店" data-type="I" data-id="428365" id="fav428365" data-favid="0" onclick="DoFavHotel(this, event);" href="javascript:void(0);" class="ico_unfavorite">收藏</a>
            </span>
        </div>
	</div>


    


	<div id="topPicList" class="htl_pic">
        <meta itemprop="image" content="//dimg11.c-ctrip.com/images/hotel/373000/372135/c3028fa548b34dd883e187498a1fe26e_R_550_412.jpg" />
		<div class="pic1"><div data-index="0" pid="8061815" style="background-image:url(//dimg11.c-ctrip.com/images/hotel/373000/372135/c3028fa548b34dd883e187498a1fe26e_R_300_225.jpg);" _src="//dimg11.c-ctrip.com/images/hotel/373000/372135/c3028fa548b34dd883e187498a1fe26e_R_550_412.jpg"></div></div><div class="pic2"><div data-index="1" pid="9807428" style="background-image:url(//dimg12.c-ctrip.com/images/200q0u000000jie0g6D8A_R_300_225.jpg);" _src="//dimg12.c-ctrip.com/images/200q0u000000jie0g6D8A_R_550_412.jpg"></div></div><div class="pic3"><div data-index="2" pid="9508373" style="background-image:url(//dimg10.c-ctrip.com/images/200a0k000000budbx4780_R_300_225.jpg);" _src="//dimg10.c-ctrip.com/images/200a0k000000budbx4780_R_550_412.jpg"></div></div><div class="pic4"><div data-index="3" pid="9508411" style="background-image:url(//dimg13.c-ctrip.com/images/200d0k000000buf428360_R_130_130.jpg);" _src="//dimg13.c-ctrip.com/images/200d0k000000buf428360_R_550_412.jpg"></div></div><div class="pic5"><div data-index="4" pid="9807362" style="background-image:url(//dimg12.c-ctrip.com/images/200u080000003329oEE89_R_130_130.jpg);" _src="//dimg12.c-ctrip.com/images/200u080000003329oEE89_R_550_412.jpg"></div></div><div class="pic6"><div data-index="5" pid="289178310" style="background-image:url(//dimg10.c-ctrip.com/images/200i0u000000jagom2525_R_130_130.jpg);" _src="//dimg10.c-ctrip.com/images/200i0u000000jagom2525_R_550_412.jpg"></div></div><div class="pic7"><div data-index="6" pid="9811459" style="background-image:url(//dimg11.c-ctrip.com/images/hotel/373000/372135/0dbac627e8fb47ffb8fb8c3d45430946_R_300_225.jpg);" _src="//dimg11.c-ctrip.com/images/hotel/373000/372135/0dbac627e8fb47ffb8fb8c3d45430946_R_550_412.jpg"></div></div><div class="pic8"><div data-index="7" pid="189065381" style="background-image:url(//dimg12.c-ctrip.com/images/200q0k000000br7oeE7E6_R_130_130.jpg);" _src="//dimg12.c-ctrip.com/images/200q0k000000br7oeE7E6_R_550_412.jpg"></div></div><div class="pic9"><div data-index="8" pid="27635828" style="background-image:url(//dimg12.c-ctrip.com/images/200p0k000000bpqnfD8D2_R_130_130.jpg);" _src="//dimg12.c-ctrip.com/images/200p0k000000bpqnfD8D2_R_550_412.jpg"></div></div><p class="pop_link"><a name="needTraceCode" data-index="1" id="view_allpic" class="all_pic" href="/pic/428365.html">酒店图片共有179张</a></p>
	</div>
    
                
            <div class="ad_box"><div class="coupon_ad_box ad_box_item"><a href="javascript:;" class="close" onclick="hiddenAdvertise('coupon_ad_box');"></a><div class="coupon_ad coupon_ad_one">  <div class="coupon_ad_title"></div><a href="//hotels.ctrip.com/events/shanzhuxinkepcfaquanx1pc">闪住新客最高立减20，免押金/免查房/先住后付</a></div></div><div class="bannerLogin" id="J_bannerLogin"><span class="bannerLogin-btn">去登录</span><span class="bannerLogin-txt"><i class="ico-face"></i>登录账户·享受返现等更多优惠</span></div></div>


            <div id="bookingoverTip" class="tips_unresult hidden"><b></b>房型已订完，建议您更改入住时间或选择其他酒店。</div>
               
            
<div class="integral3" id="J_integralIcon" style="display:none"></div>
<div><a rel="nofollow" name="book" id="book" href="javascript:void(0);"></a></div>
<div class="hotel_tabs_box" id="J_room_list_tabs" style="background-color: rgb(255, 255, 255); z-index: 10;">
    
    <a rel="nofollow" id="lnkBook" class="book_btn hidden" onclick="window.scrollBy(0,document.getElementById('book').getBoundingClientRect().top);return false;" href="javascript:void(0);">立即预订</a>
    
    <ul class="hotel_tabs layoutfix">
        <li class="current fn-hotel-list" data-to="book"><a href="javascript:void(0);">房型列表</a></li>
        <li class="fn-shx-dp" style="" data-to="book"><a href="javascript:void(0);">优惠套餐</a></li>
        <li class="fn-meeting-list" style="" data-to="book"><a href="javascript:void(0);">会厅列表</a></li>
        
            <!--非满房推荐视图，非相册视图-->
            
                <li id="bookTab" data-to="id_detail_arrow"><a href="javascript:void(0);">酒店详情</a></li>
                
			    <li id="commentTab" data-to="id_comment_arrow"><a href="javascript:void(0);">酒店点评(6518)</a></li>
                
    </ul>
</div>
<iframe frameborder="0" class="IFR-SHDPX" scrolling="no" fakesrc="//taocan.ctrip.com/SH/HotelDPSearch.aspx?shxCheckInDate=2018-09-21&amp;shxCheckOutDate=2018-09-22&amp;shxCityId=2&amp;shxHotelId=428365&amp;shxHotelName=&amp;shxLatitude=31.2985534667969&amp;shxLongitude=121.539833068848" style="display: none;"></iframe><div id="id_room_select_box" class="room_select_box">
<div class="J_fullTipWrapper"></div>
<div class="date_change_box2">
    <div class="left">
        <p class="title hidden">您可以尝试修改入住退房日期</p>
        <div class="date_form">
            <div class="date_form_inputs">
	            <div class="date_form_label">
	            入住
                <input type="text" value="2018-09-21" autocomplete="off" mod_calendar_rangestart="#" mod_calendar_focusnext="true" mod_notice_tip="yyyy-mm-dd" mod="notice|calendar" class="input_txt" name="cc_txtCheckIn" id="cc_txtCheckIn" _cqnotice="yyyy-mm-dd" />
	            </div>
	            <div class="date_form_line"></div>
	            <div class="date_form_label">
	            退房
                <input type="text" value="2018-09-22" autocomplete="off" mod_calendar_rangestart="#" mod_calendar_focusnext="true" mod_notice_tip="yyyy-mm-dd" mod="notice|calendar" class="input_txt" name="cc_txtCheckOut" id="cc_txtCheckOut" _cqnotice="yyyy-mm-dd" />
	            </div>
            </div>

			
			<div class="date_form_selects">
					房间数
					<div id="J_roomCountDiv_Detail" class="n_gst n_gstRoom">
						<input id="J_roomCount_Detail" type="text" class="n_gst_v" readonly="" value="1间" />
						<i id="J_roomCount_Detail_i" class="n_gst_tri"></i>
						<div class="n_gst_p">
							<ul id="J_roomCountList_Detail" class="n_gst_num">
							<li>1间</li><li>2间</li><li>3间</li><li>4间</li><li>5间</li><li>6间</li><li>7间</li><li>8间</li><li>9间</li><li>10间</li></ul>
						</div>
					</div>
				</div>

				<div class="date_form_selects">
					住客数
<div id="J_RoomGuestInfoDiv_Detail" class="n_gst n_gstPeople">
	<input id="J_RoomGuestInfoTxt_Detail" type="text" class="n_gst_v" readonly="true" value="1成人" />
	<i id="J_RoomGuestInfoTxt_i_Detail" class="n_gst_tri"></i>
	<div class="n_gst_p">
		<!-- 快捷选项 -->
		<ul class="n_gst_list">
			<li class="n_gst_list_opt">
				成人<span class="n_gst_age">18岁及以上</span>
				<!-- 按钮不可用时，添加number_disable -->
				<span id="J_AdultCount_Detail" class="number_control"><span class="number_reduce number_disable"><i class="icon_numreduce"></i></span><input type="text" class="number_input" readonly="" value="1" /><span class="number_plus"><i class="icon_numplus"></i></span></span>
			</li>
			<li class="n_gst_list_opt">
				儿童<span class="n_gst_age">0-17岁</span>
				<span id="J_ChildCount_Detail" class="number_control"><span class="number_reduce number_disable"><i class="icon_numreduce"></i></span><input type="text" class="number_input" readonly="" value="0" /><span class="number_plus"><i class="icon_numplus"></i></span></span>
			</li>
		</ul>
		<!-- 儿童人数大于0时显示 -->
		<div id="J_childageValDiv_Detail" class="n_gst_childs" style="display:none;">
			<dl class="n_gst_childs_dl">
				<dt>儿童年龄（<span class="J_today"></span>当天）</dt>
				<dd><select class="J_childageVal" id="J_childageVal_Detail0" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal_Detail1" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal_Detail2" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal_Detail3" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal_Detail4" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal_Detail5" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal_Detail6" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal_Detail7" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
				<dd><select class="J_childageVal" id="J_childageVal_Detail8" style="display: none;"><option value="0">&lt;1岁</option><option value="1">1岁</option><option value="2">2岁</option><option value="3">3岁</option><option value="4">4岁</option><option value="5">5岁</option><option value="6">6岁</option><option value="7">7岁</option><option value="8">8岁</option><option value="9">9岁</option><option value="10">10岁</option><option value="11">11岁</option><option value="12">12岁</option><option value="13">13岁</option><option value="14">14岁</option><option value="15">15岁</option><option value="16">16岁</option><option value="17">17岁</option></select></dd>
			</dl>
			<!-- 默认不显示，按需求提示 -->
			<div class="n_gst_childs_tips" style="display:none;">请选择儿童年龄</div>
		</div>
		<div class="n_gst_ft">
			<a id="J_RoomGuestInfoBtnOK_Detail" class="n_gst_btn">确定</a>
			<a id="J_RoomGuestInfoBtnCancel_Detail" class="n_gst_btncancel">取消</a>
		</div>
	</div>
</div>
<span data-role="jmp" class="ui_tips_help" data-params="{'options':{'type':'jmp_table','template':'$jmp_table','content':{'txt':'&lt;div class=&quot;jmp_bd&quot;&gt;18周岁及以上为成人。&lt;br/&gt;0-17周岁儿童请参照各酒店入住政策。&lt;/div&gt;'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'hotelDesc'}}"></span>
<input type="hidden" id="J_RoomGuestCount_Detail" value="1,1,0" />
			</div>
			


            <a href="javascript:void(0);" id="changeBtn" class="btn">重新搜索</a>
        </div>
    </div>

    <div class="right">
        <ul class="c_sort" id="J_HorizontalPriceAndCoupon">
            <li class="c_sort_links_multiple c_sort_price" style="z-index:3;" id="J_price_range">
                <a href="javascript:;" class="c_sort_links "><label class="lb_text">价格</label><i class="icon_links_dropdown"></i></a>
                <div class="multiple_menu hidden">
                    <a href="javascript:;" class="choosed J_price_item J_price_click" id="J_price_nolimit">不限</a>
                    <a href="javascript:;" class="J_price_item J_price_click " data-range="0-149"><dfn>¥</dfn>150以下</a>
                    <a href="javascript:;" class="J_price_item J_price_click " data-range="150-300"><dfn>¥</dfn>150-300</a>
                    <a href="javascript:;" class="J_price_item J_price_click " data-range="300-450"><dfn>¥</dfn>300-450</a>
                    <a href="javascript:;" class="J_price_item J_price_click " data-range="450-600"><dfn>¥</dfn>450-600</a>
                    <a href="javascript:;" class="J_price_item J_price_click " data-range="601-2147483647"><dfn>¥</dfn>600以上</a>
                    <a href="javascript:;" class="custom_range J_price_item">
                        <input class="input_range J_price_item" id="J_price_min" type="text" value="" />
                        -
                        <input class="input_range J_price_item" id="J_price_max" type="text" value="" />
                        <input value="确定" class="btn_range J_price_item J_price_click" id="J_price_range_btn" type="button" />
                    </a>
                </div>
            </li>
            <li class="c_sort_links_multiple c_sort_coupon" id="J_Coupon">
                <a href="javascript:;" class="c_sort_links">可用优惠券<i class="icon_links_dropdown"></i></a>
            <div id="J_CouponList" class="available_coupon_pop hidden"><p class="status_unlogin"><a id="J_LoginForCoupon" href="javascript:">登录</a> 即可查看可用的优惠券</p></div></li>

            <li class="c_sort_links_multiple c_sort_promotionf" id="J_promotionf" data-default="">
                <a href="javascript:;" class="c_sort_links"><label class="lb_text" data-default="促销">促销</label><i class="icon_links_dropdown"></i></a>
                <div id="J_promotionf_div" style="width:150px;" class="multiple_menu hidden"><a href="javascript:;" class="J_prom_item J_prom_click choosed">    不限    </a><a href="javascript:;" class="J_prom_item J_prom_click" data-id="all"> 全部促销优惠 </a><a href="javascript:;" class="J_prom_item J_prom_click" data-id="2"> 天天特价 </a><a href="javascript:;" class="J_prom_item J_prom_click" data-id="3"> 门店新客 </a><a href="javascript:;" class="J_prom_item J_prom_click" data-id="4"> 每日特惠 </a><a href="javascript:;" class="J_prom_item J_prom_click" data-id="23"> 出行特惠 </a><a href="javascript:;" class="J_prom_item J_prom_click" data-id="24"> 开业特惠 </a></div>
            </li>

        </ul>
    </div>

</div>

    <div class="sort_box2 J_HorizontalVersionFilter" style="z-index:1;">
        <div class="sort_type" id="J_HorizontalVersionBed">
            <span class="sort_title">床型</span>
            <div class="sort_list">
                <a href="javascript:;" data-type="bed" data-value="1" class="sort_item ">大床</a>
                <a href="javascript:;" data-type="bed" data-value="2" class="sort_item ">双床</a>
                <a href="javascript:;" data-type="triple" data-value="1" class="sort_item ">三人/家庭房</a>
            </div>
        </div>
        <div class="sort_type" id="J_HorizontalVersionBF">
            <span class="sort_title">早餐</span>
            <div class="sort_list">
                <a href="javascript:;" data-type="bf" data-value="1,2,4" class="sort_item ">含早餐</a>
                <a href="javascript:;" data-type="bf" data-value="2" class="sort_item ">单份早餐</a>
                <a href="javascript:;" data-type="bf" data-value="1" class="sort_item ">双份早餐</a>
            </div>
        </div>
        <div class="sort_type" id="J_HorizontalVersionNetwork">
            <span class="sort_title">宽带</span>
            <div class="sort_list">
                <a href="javascript:;" data-type="network" data-value="1" class="sort_item ">免费WIFI上网</a>
                <a href="javascript:;" data-type="network" data-value="2" class="sort_item ">免费有线宽带</a>
            </div>
        </div>
        <div class="sort_type" id="J_HorizontalVersionPay">
            <span class="sort_title">支付方式</span>
            <div class="sort_list">
                <a href="javascript:;" data-type="pay" data-value="1,2" class="sort_item ">到店付款</a>
                <a href="javascript:;" data-type="pay" data-value="3" class="sort_item ">在线付款</a>
                <a href="javascript:;" data-type="pay" data-value="4" class="sort_item ">闪住</a>
            </div>
        </div>
        <div class="sort_type" id="J_HorizontalVersionOther">
            <span class="sort_title">其他</span>
            <div class="sort_list">
                <a href="javascript:;" data-type="policy" data-value="1" class="sort_item ">可免费取消</a>
                <a href="javascript:;" data-type="ctrip" data-value="1" class="sort_item ">携程自营</a>
                <a href="javascript:;" data-type="reserve" data-value="1" class="sort_item ">可订</a>
                <a href="javascript:;" data-type="confirm" data-value="1" class="sort_item ">立即确认</a>
                <a href="javascript:;" data-type="addbed" data-value="1" class="sort_item ">可加床</a>
                <a href="javascript:;" data-type="hotelinvoice" data-value="1" class="sort_item " "="">增值税专用发票</a>
                <a href="javascript:;" data-type="hourroom" data-value="1" class="sort_item ">钟点房</a>
                
                <a href="javascript:;" data-type="CtripService" data-value="4" class="sort_item ">亲子主题房</a>
             </div>
        </div>
        <div class="btn_clear sort_btn hidden">
            <a href="javascript:;">清除所有筛选</a>
        </div>
    </div>

<div id="hotelRoomBox" class="">


<div class="htl_room_table J_roomTable">
<table border="0" cellspacing="0" cellpadding="0" summary="详情页酒店房型列表" id="J_RoomListTbl">
<tbody><tr>
<th class="col1" style="padding-left:10px;">房型</th>
<th class="col2"></th>
<th class="col3">床型</th>
<th class="col4">早餐</th>
<th class="col5">宽带</th>
<th class="col_person">入住人数</th>
<th class="col_policy">政策</th>
<th class="col6">房价（含服务费）</th>
<th class="col7">
</th>
</tr>

<tr id="J_hourNoResult" class="hidden"></tr>




<tr class="tr-recommend last_room" expand="" brid="693192" guid="e46b90c1-cd1a-4403-a1de-0d55e2dba859" data-disable="0">




<td class="room_type td693192" data-baseroomid="693192" data-masterbasicroomid="693192" data-hotelid="428365" id="693192" rowspan="1" data-roomlist="69643394," data-idlist="69643394PPGuessFav,">
<div class="tr-recommend-flag"><i class="tr-recommend-flag-ico"></i>为您推荐</div>
<a id="roomRepeater_ctl00_subRoomRepeater_ctl00_linkImage" class="pic J_show_room_detail" rel="nofollow" onclick="HotelRoom.onNameNewClick(this)" href="javascript:void(0);"><img id="roomRepeater_ctl00_subRoomRepeater_ctl00_imageRoomImg" _src="//dimg10.c-ctrip.com/images/20090k000000by9qf64E8_R_300_225.jpg" src="//dimg10.c-ctrip.com/images/20090k000000by9qf64E8_R_130_130.jpg" style="border-width:0px;" /></a>
<a rel="nofollow" class="room_unfold J_show_room_detail" href="javascript:void(0);" onclick="HotelRoom.onNameNewClick(this)">
    豪华湖景房<b style="color: #B9B9B9;font-weight: normal;">x</b>1间
    <br />
    
    
    
     <span>查看详情</span>
    
</a>
    
    
</td><td class="child_name " data-ctrip="1" data-hotelinvoice="1" data-price="699" data-bed="1|2" data-policy="3" data-bf="3" data-network="1|2" data-roomid="69643394PPGuessFav" data-baseroominfo="{&quot;RoomUrl&quot;:&quot;//dimg10.c-ctrip.com/images/20090k000000by9qf64E8_R_300_225.jpg&quot;,&quot;RoomID&quot;:693192,&quot;RoomName&quot;:&quot;豪华湖景房&quot;,&quot;BaseRoomInfo&quot;:&quot;45平方米&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;7-19层&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;不可吸烟&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;1张2米特大床 或 2张1.2米单人床&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;2人&quot;,&quot;ConvenientFacilities&quot;:null,&quot;MediaTechnology&quot;:null,&quot;FoodBeverages&quot;:null,&quot;Bathroom&quot;:null,&quot;OutdoorsViews&quot;:null,&quot;ServicesOthers&quot;:null,&quot;PriceNum&quot;:7,&quot;LowPrice&quot;:699.0,&quot;RoomTotalNum&quot;:1}" data-baseroomname="豪华湖景房" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="col4">无早</td>
<td class="col5"><span id="roomRepeater_ctl00_subRoomRepeater_ctl00_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>699</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl00_subRoomRepeater_ctl00_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl00_subRoomRepeater_ctl00_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69643394,0,0.0,699,PP,0,0.0,0,T,大/双,0,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69643394&quot;,&quot;basicroomid&quot;:&quot;693192&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;1&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69643394&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;1&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;1&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69643394&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=699&amp;isLowestRoom=1&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="clicked hidden">
<td colspan="9">
<div id="rdn693192">
	<a class="c_close j_detail_close" href="javascript:void(0)">×</a>
	<div class="hrd-title">
        豪华湖景房
        
	</div>
	<div class="hrd-info">
		<div class="hrd-info-pic" data-baseroomvrimage="" style="overflow: hidden">
            
		    <span class="prev" style="display:none"><b></b></span><span class="next" style=" "><b></b></span><div style="width:300%" class="J_slider_box_in" data-page="3"><ul><li><img src="//dimg10.c-ctrip.com/images/20090k000000by9qf64E8_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/20020j000000aixwcDB8C_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg12.c-ctrip.com/images/hotel/373000/372135/1b5013a1601c4bf89d8d4754793dc150_R_300_225.jpg" width="300" height="225" alt="" /></li></ul></div>
		</div>
		<div class="hrd-info-base">
            <ul class="hrd-info-base-list">
				<itemtemplate><li><span class="t">建筑面积:</span>45平方米</li></itemtemplate><itemtemplate><li><span class="t">楼层:</span>7-19层</li></itemtemplate><itemtemplate><li><span class="t">床型：</span>1张2米特大床 或 2张1.2米单人床</li></itemtemplate><itemtemplate><li><span class="t">窗户：</span>有窗</li></itemtemplate><itemtemplate><li><span class="t">可加床：</span>RMB 230/床/间夜</li></itemtemplate><itemtemplate><li><span class="t">无烟：</span>不可吸烟</li></itemtemplate>
            </ul>
			<p class="hrd-info-base-describe">客人预订豪华湖景房时请备注具体需求信息（预订大床还是双床），以便酒店提供更好的服务。</p>
        </div>
	</div>
	<div class="hrd-allfac">
        <div class="hrd-allfac-title">所有房型设施</div>
		<ul class="hrd-allfac-list">
            
                    <li>
                        <span class="t">
                            便利设施:
                        </span>
                        雨伞、书桌、多种规格电源插座、房内保险箱、空调、衣柜/衣橱、针线包、220V电压插座、遮光窗帘、自动窗帘、<span class="base_txtgray">沙发</span>、开夜床、电子秤、房间内高速上网、客房WIFI覆盖、客房WIFI覆盖<span class="text_green">免费</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            媒体科技：
                        </span>
                        国内长途电话、国际长途电话、有线频道、液晶电视机、iPod音乐基座、电话
                    </li>
                    
                    <li>
                        <span class="t">
                            食品饮品：
                        </span>
                        电热水壶、咖啡壶/茶壶、<span class="text_green">免费</span>瓶装水、迷你吧、小冰箱、<span class="base_txtgray">咖啡机</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            浴室：
                        </span>
                        拖鞋、浴室化妆放大镜、24小时热水、<span class="text_green">免费</span>洗漱用品(6样以上)、浴衣、浴缸、独立淋浴间、吹风机、洗浴间电视、淋浴
                    </li>
                    
                    <li>
                        <span class="t">
                            室外景观：
                        </span>
                        城景、湖景、花园景、享有风景
                    </li>
                    
                    <li>
                        <span class="t">
                            其他：
                        </span>
                        <span class="base_txtgray">连通房</span>、唤醒服务、语音留言、欢迎礼品
                    </li>
                    
                    <li>
                        <span class="t">
                            (灰色文字表示此房型部分房间有此设备) 
                        </span>
                        
                    </li>
                    
		</ul>
	</div>    
    
</div>    

</td>
</tr>

<tr><td colspan="9" class="classify-hd">符合条件的房型</td></tr>


<tr class="" expand="" brid="693192" guid="8a3191db-8d89-44fd-ac69-db8e61cc89b1" data-disable="0">




<td class="room_type td693192" data-baseroomid="693192" data-masterbasicroomid="693192" data-hotelid="428365" id="693192" rowspan="8" data-roomlist="69643394,4417042,73575856,211949554,69643397,69643397,2948177,202226980," data-idlist="69643394PP,4417042FG,73575856PP,211949554FG,69643397PP1001021205,69643397PP,2948177FG,202226980PP,">

<a id="roomRepeater_ctl01_subRoomRepeater_ctl00_linkImage" class="pic J_show_room_detail" rel="nofollow" onclick="HotelRoom.onNameNewClick(this)" href="javascript:void(0);"><img id="roomRepeater_ctl01_subRoomRepeater_ctl00_imageRoomImg" _src="//dimg10.c-ctrip.com/images/20090k000000by9qf64E8_R_300_225.jpg" src="//dimg10.c-ctrip.com/images/20090k000000by9qf64E8_R_130_130.jpg" style="border-width:0px;" /></a>
<a rel="nofollow" class="room_unfold J_show_room_detail" href="javascript:void(0);" onclick="HotelRoom.onNameNewClick(this)">
    豪华湖景房
    <br />
    
    
    
     <span>查看详情</span>
    
</a>
    
    
</td><td class="child_name " data-firstmap="69643394PP,4417042PP,73575856PP,211949554PP,69643397PP,69643397PP,2948177PP,202226980PP," data-ctrip="1" data-hotelinvoice="1" data-price="699" data-bed="1|2" data-policy="3" data-bf="3" data-network="1|2" data-roomid="69643394PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="col4">无早</td>
<td class="col5"><span id="roomRepeater_ctl01_subRoomRepeater_ctl00_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>699</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl01_subRoomRepeater_ctl00_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl01_subRoomRepeater_ctl00_lblSuperPrice" class="super_price">立即确认超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69643394,0,0.0,699,PP,0,0.0,0,T,大/双,0,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69643394&quot;,&quot;basicroomid&quot;:&quot;693192&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;1&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69643394&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;1&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69643394&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=699&amp;isLowestRoom=1&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693192" guid="a176fab5-bcc0-4ee6-ba64-30f7213f2754" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="715" data-bed="1|2" data-policy="3" data-bf="3" data-network="1|2" data-roomid="4417042FG" data-reserve="1" data-pay="2">
<span class="room_type_name">(限时促销)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="col4">无早</td>
<td class="col5"><span id="roomRepeater_ctl01_subRoomRepeater_ctl01_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>715</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl01_subRoomRepeater_ctl01_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl01_subRoomRepeater_ctl01_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="4417042,0,0.0,715,FG,0.0,0.0,0,T,大/双,0,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;4417042&quot;,&quot;basicroomid&quot;:&quot;693192&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;4417042&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=4417042&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=715&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693192" guid="086ac5b0-d100-4a0f-8352-9670ff4f77fe" data-disable="0">


<td class="child_name " data-ctrip="1" data-hotelinvoice="1" data-price="793" data-bed="1|2" data-policy="3" data-bf="2" data-network="1|2" data-roomid="73575856PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(限量特惠)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天单早</td>
<td class="col5"><span id="roomRepeater_ctl01_subRoomRepeater_ctl02_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>793</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl01_subRoomRepeater_ctl02_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl01_subRoomRepeater_ctl02_lblSuperPrice" class="super_price">单早超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="73575856,0,0.0,793,PP,0,0.0,0,T,大/双,1,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;73575856&quot;,&quot;basicroomid&quot;:&quot;693192&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;73575856&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=73575856&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=793&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693192" guid="9fd98e35-0461-45d7-9c45-5fc9d16b086a" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="810" data-bed="1|2" data-policy="3" data-bf="2" data-network="1|2" data-roomid="211949554FG" data-reserve="1" data-pay="2">
<span class="room_type_name">标准价</span>

<input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天单早</td>
<td class="col5"><span id="roomRepeater_ctl01_subRoomRepeater_ctl03_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>810</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl01_subRoomRepeater_ctl03_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl01_subRoomRepeater_ctl03_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="211949554,0,0.0,810,FG,0.0,0.0,0,T,大/双,1,不可取消,T,T,F,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;211949554&quot;,&quot;basicroomid&quot;:&quot;693192&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;211949554&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=211949554&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=810&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693192" guid="a1af3876-45f8-4a11-afe6-2d7b5f7a9eea" data-disable="0">


<td class="child_name " data-hotelinvoice="1" data-price="878" data-bed="1" data-policy="3" data-bf="1" data-network="1|2" data-roomid="69643397PP1001021205" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购)（大床）</span>

<input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl01_subRoomRepeater_ctl04_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>878</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl01_subRoomRepeater_ctl04_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl01_subRoomRepeater_ctl04_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69643397,1001021205,0.0,878,PP,0,0.0,0,F,大床,2,不可取消,F,T,F,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69643397&quot;,&quot;basicroomid&quot;:&quot;693192&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;1&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;大双床&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;1001021205&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69643397&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;1001021205&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69643397&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=1001021205&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=878&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693192" guid="86b8acd1-c3ba-454a-8385-f7d7b04ccfb3" data-disable="0">


<td class="child_name " data-ctrip="1" data-hotelinvoice="1" data-price="878" data-bed="1|2" data-policy="3" data-bf="1" data-network="1|2" data-roomid="69643397PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl01_subRoomRepeater_ctl05_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>878</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl01_subRoomRepeater_ctl05_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl01_subRoomRepeater_ctl05_lblSuperPrice" class="super_price">双早超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69643397,0,0.0,878,PP,0,0.0,0,T,大/双,2,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69643397&quot;,&quot;basicroomid&quot;:&quot;693192&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69643397&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69643397&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=878&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693192" guid="49a52834-d023-4127-b2af-6ce09b2a6c0d" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="895" data-bed="1|2" data-policy="3" data-bf="1" data-network="1|2" data-roomid="2948177FG" data-reserve="1" data-pay="2">
<span class="room_type_name">(限时促销)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl01_subRoomRepeater_ctl06_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>895</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl01_subRoomRepeater_ctl06_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl01_subRoomRepeater_ctl06_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="2948177,0,0.0,895,FG,0.0,0.0,0,T,大/双,2,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;2948177&quot;,&quot;basicroomid&quot;:&quot;693192&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;2948177&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=2948177&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=895&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded last_room" expand="" brid="693192" guid="896de03c-330d-4e85-a3d3-fd07fcff6e9b" data-disable="0">


<td class="child_name " data-ctrip="1" data-hotelinvoice="1" data-price="1072" data-bed="1|2" data-policy="3" data-bf="3" data-network="1|2" data-roomid="202226980PP" data-baseroominfo="{&quot;RoomUrl&quot;:&quot;//dimg10.c-ctrip.com/images/20090k000000by9qf64E8_R_300_225.jpg&quot;,&quot;RoomID&quot;:693192,&quot;RoomName&quot;:&quot;豪华湖景房&quot;,&quot;BaseRoomInfo&quot;:&quot;45平方米&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;7-19层&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;不可吸烟&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;1张2米特大床 或 2张1.2米单人床&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;2人&quot;,&quot;ConvenientFacilities&quot;:null,&quot;MediaTechnology&quot;:null,&quot;FoodBeverages&quot;:null,&quot;Bathroom&quot;:null,&quot;OutdoorsViews&quot;:null,&quot;ServicesOthers&quot;:null,&quot;PriceNum&quot;:7,&quot;LowPrice&quot;:699.0,&quot;RoomTotalNum&quot;:8}" data-baseroomname="豪华湖景房" data-reserve="0" data-pay="3">
<span class="room_type_name">(花间月中秋)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'每日含价值228元花间月月饼礼盒一份','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="col4">无早</td>
<td class="col5"><span id="roomRepeater_ctl01_subRoomRepeater_ctl07_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1072</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl01_subRoomRepeater_ctl07_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl01_subRoomRepeater_ctl07_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span><a id="roomRepeater_ctl01_subRoomRepeater_ctl07_lkBookingButton" class="btns_base22 btns_base22_dis" data-order="202226980,0,0.0,1072,PP,0,0.0,0,F,大/双,0,不可取消,F,F,T,F,428365,1700870," href="javascript:void(0)\"><div class="btns_base22_main">订完</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a></span>


<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="clicked hidden">
<td colspan="9">
<div id="rdn693192">
	<a class="c_close j_detail_close" href="javascript:void(0)">×</a>
	<div class="hrd-title">
        豪华湖景房
        
	</div>
	<div class="hrd-info">
		<div class="hrd-info-pic" data-baseroomvrimage="" style="overflow: hidden">
            
		    <span class="prev" style="display:none"><b></b></span><span class="next" style=" "><b></b></span><div style="width:300%" class="J_slider_box_in" data-page="3"><ul><li><img src="//dimg10.c-ctrip.com/images/20090k000000by9qf64E8_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/20020j000000aixwcDB8C_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg12.c-ctrip.com/images/hotel/373000/372135/1b5013a1601c4bf89d8d4754793dc150_R_300_225.jpg" width="300" height="225" alt="" /></li></ul></div>
		</div>
		<div class="hrd-info-base">
            <ul class="hrd-info-base-list">
				<itemtemplate><li><span class="t">建筑面积:</span>45平方米</li></itemtemplate><itemtemplate><li><span class="t">楼层:</span>7-19层</li></itemtemplate><itemtemplate><li><span class="t">床型：</span>1张2米特大床 或 2张1.2米单人床</li></itemtemplate><itemtemplate><li><span class="t">窗户：</span>有窗</li></itemtemplate><itemtemplate><li><span class="t">可加床：</span>RMB 230/床/间夜</li></itemtemplate><itemtemplate><li><span class="t">无烟：</span>不可吸烟</li></itemtemplate>
            </ul>
			<p class="hrd-info-base-describe">客人预订豪华湖景房时请备注具体需求信息（预订大床还是双床），以便酒店提供更好的服务。</p>
        </div>
	</div>
	<div class="hrd-allfac">
        <div class="hrd-allfac-title">所有房型设施</div>
		<ul class="hrd-allfac-list">
            
                    <li>
                        <span class="t">
                            便利设施:
                        </span>
                        雨伞、书桌、多种规格电源插座、房内保险箱、空调、衣柜/衣橱、针线包、220V电压插座、遮光窗帘、自动窗帘、<span class="base_txtgray">沙发</span>、开夜床、电子秤、房间内高速上网、客房WIFI覆盖、客房WIFI覆盖<span class="text_green">免费</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            媒体科技：
                        </span>
                        国内长途电话、国际长途电话、有线频道、液晶电视机、iPod音乐基座、电话
                    </li>
                    
                    <li>
                        <span class="t">
                            食品饮品：
                        </span>
                        电热水壶、咖啡壶/茶壶、<span class="text_green">免费</span>瓶装水、迷你吧、小冰箱、<span class="base_txtgray">咖啡机</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            浴室：
                        </span>
                        拖鞋、浴室化妆放大镜、24小时热水、<span class="text_green">免费</span>洗漱用品(6样以上)、浴衣、浴缸、独立淋浴间、吹风机、洗浴间电视、淋浴
                    </li>
                    
                    <li>
                        <span class="t">
                            室外景观：
                        </span>
                        城景、湖景、花园景、享有风景
                    </li>
                    
                    <li>
                        <span class="t">
                            其他：
                        </span>
                        <span class="base_txtgray">连通房</span>、唤醒服务、语音留言、欢迎礼品
                    </li>
                    
                    <li>
                        <span class="t">
                            (灰色文字表示此房型部分房间有此设备) 
                        </span>
                        
                    </li>
                    
		</ul>
	</div>    
    
</div>    

</td>
</tr>




<tr class="" expand="" brid="693190" guid="7dcd5e76-f875-448f-aee6-46214d71a382" data-disable="0">




<td class="room_type td693190" data-baseroomid="693190" data-masterbasicroomid="693190" data-hotelid="428365" id="693190" rowspan="7" data-roomlist="69565417,69565361,73575861,69565418,69565418,69565363,2160243," data-idlist="69565417PP,69565361FG,73575861PP,69565418PP,69565418PP1001021205,69565363FG,2160243FG,">

<a id="roomRepeater_ctl02_subRoomRepeater_ctl00_linkImage" class="pic J_show_room_detail" rel="nofollow" onclick="HotelRoom.onNameNewClick(this)" href="javascript:void(0);"><img id="roomRepeater_ctl02_subRoomRepeater_ctl00_imageRoomImg" _src="//dimg11.c-ctrip.com/images/hotel/373000/372135/0dbac627e8fb47ffb8fb8c3d45430946_R_300_225.jpg" src="//dimg11.c-ctrip.com/images/hotel/373000/372135/0dbac627e8fb47ffb8fb8c3d45430946_R_130_130.jpg" style="border-width:0px;" /></a>
<a rel="nofollow" class="room_unfold J_show_room_detail" href="javascript:void(0);" onclick="HotelRoom.onNameNewClick(this)">
    至尊湖景房
    <br />
    
    
    
     <span>查看详情</span>
    
</a>
    
    
</td><td class="child_name " data-firstmap="69565417PP,69565361PP,73575861PP,69565418PP,69565418PP,69565363PP,2160243PP," data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1176" data-bed="1|2" data-policy="3" data-bf="3" data-network="1|2" data-roomid="69565417PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购.)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="col4">无早</td>
<td class="col5"><span id="roomRepeater_ctl02_subRoomRepeater_ctl00_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1176</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl02_subRoomRepeater_ctl00_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl02_subRoomRepeater_ctl00_lblSuperPrice" class="super_price">立即确认超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565417,0,0.0,1176,PP,0,0.0,0,T,大/双,0,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565417&quot;,&quot;basicroomid&quot;:&quot;693190&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;1&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565417&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565417&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1176&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693190" guid="fe1440b9-0b54-4b7a-ab76-107531fa0f22" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1200" data-bed="1|2" data-policy="3" data-bf="3" data-network="1|2" data-roomid="69565361FG" data-reserve="1" data-pay="2">
<span class="room_type_name">(限时促销)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="col4">无早</td>
<td class="col5"><span id="roomRepeater_ctl02_subRoomRepeater_ctl01_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1200</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl02_subRoomRepeater_ctl01_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl02_subRoomRepeater_ctl01_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565361,0,0.0,1200,FG,0.0,0.0,0,T,大/双,0,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565361&quot;,&quot;basicroomid&quot;:&quot;693190&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565361&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565361&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1200&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693190" guid="5253bf0c-941c-461f-b85e-d737fb3507e3" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1279" data-bed="1|2" data-policy="3" data-bf="2" data-network="1|2" data-roomid="73575861PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(限量特惠)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天单早</td>
<td class="col5"><span id="roomRepeater_ctl02_subRoomRepeater_ctl02_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1279</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl02_subRoomRepeater_ctl02_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl02_subRoomRepeater_ctl02_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="73575861,0,0.0,1279,PP,0,0.0,0,T,大/双,1,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;73575861&quot;,&quot;basicroomid&quot;:&quot;693190&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;73575861&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=73575861&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1279&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693190" guid="c27d9519-72f8-48eb-a1a2-567834532123" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1339" data-bed="1|2" data-policy="3" data-bf="1" data-network="1|2" data-roomid="69565418PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购.)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl02_subRoomRepeater_ctl03_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1339</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl02_subRoomRepeater_ctl03_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl02_subRoomRepeater_ctl03_lblSuperPrice" class="super_price">双早超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565418,0,0.0,1339,PP,0,0.0,0,T,大/双,2,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565418&quot;,&quot;basicroomid&quot;:&quot;693190&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565418&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565418&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1339&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693190" guid="d995cd9a-de62-4eb6-b750-6f21abfa945e" data-disable="0">


<td class="child_name " data-addbed="1" data-hotelinvoice="1" data-price="1339" data-bed="1" data-policy="3" data-bf="1" data-network="1|2" data-roomid="69565418PP1001021205" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购.)（大床）</span>

<input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl02_subRoomRepeater_ctl04_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1339</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl02_subRoomRepeater_ctl04_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl02_subRoomRepeater_ctl04_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565418,1001021205,0.0,1339,PP,0,0.0,0,F,大床,2,不可取消,F,T,F,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565418&quot;,&quot;basicroomid&quot;:&quot;693190&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;1&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;大双床&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;1001021205&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565418&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;1001021205&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565418&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=1001021205&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1339&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693190" guid="3fb02907-5454-4463-969d-cfa353a79de8" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1368" data-bed="1|2" data-policy="3" data-bf="1" data-network="1|2" data-roomid="69565363FG" data-reserve="1" data-pay="2">
<span class="room_type_name">(限时促销)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl02_subRoomRepeater_ctl05_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1368</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl02_subRoomRepeater_ctl05_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl02_subRoomRepeater_ctl05_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565363,0,0.0,1368,FG,0.0,0.0,0,T,大/双,2,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565363&quot;,&quot;basicroomid&quot;:&quot;693190&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565363&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565363&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1368&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded last_room" expand="" brid="693190" guid="a69e9d61-61ac-455d-b652-ac75a094a1a2" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1480" data-bed="1|2" data-policy="3" data-bf="1" data-network="1|2" data-roomid="2160243FG" data-baseroominfo="{&quot;RoomUrl&quot;:&quot;//dimg11.c-ctrip.com/images/hotel/373000/372135/0dbac627e8fb47ffb8fb8c3d45430946_R_300_225.jpg&quot;,&quot;RoomID&quot;:693190,&quot;RoomName&quot;:&quot;至尊湖景房&quot;,&quot;BaseRoomInfo&quot;:&quot;65平方米&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;7-23层&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;不可吸烟&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;1张2米特大床 或 2张1.2米单人床&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;2人&quot;,&quot;ConvenientFacilities&quot;:null,&quot;MediaTechnology&quot;:null,&quot;FoodBeverages&quot;:null,&quot;Bathroom&quot;:null,&quot;OutdoorsViews&quot;:null,&quot;ServicesOthers&quot;:null,&quot;PriceNum&quot;:7,&quot;LowPrice&quot;:1176.0,&quot;RoomTotalNum&quot;:7}" data-baseroomname="至尊湖景房" data-reserve="1" data-pay="2">
<span class="room_type_name">标准价</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl02_subRoomRepeater_ctl06_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1480</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl02_subRoomRepeater_ctl06_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl02_subRoomRepeater_ctl06_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="2160243,0,0.0,1480,FG,0.0,0.0,0,T,大/双,2,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;2160243&quot;,&quot;basicroomid&quot;:&quot;693190&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;7&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;2160243&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=2160243&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1480&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="clicked hidden">
<td colspan="9">
<div id="rdn693190">
	<a class="c_close j_detail_close" href="javascript:void(0)">×</a>
	<div class="hrd-title">
        至尊湖景房
        
	</div>
	<div class="hrd-info">
		<div class="hrd-info-pic" data-baseroomvrimage="" style="overflow: hidden">
            
		    <span class="prev" style="display:none"><b></b></span><span class="next" style=" "><b></b></span><div style="width:200%" class="J_slider_box_in" data-page="2"><ul><li><img src="//dimg11.c-ctrip.com/images/hotel/373000/372135/0dbac627e8fb47ffb8fb8c3d45430946_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/fd/hotel/g4/M08/0F/03/CggYHFaoYmCAbhIIAACNOHyV2Qc971_R_300_225.jpg" width="300" height="225" alt="" /></li></ul></div>
		</div>
		<div class="hrd-info-base">
            <ul class="hrd-info-base-list">
				<itemtemplate><li><span class="t">建筑面积:</span>65平方米</li></itemtemplate><itemtemplate><li><span class="t">楼层:</span>7-23层</li></itemtemplate><itemtemplate><li><span class="t">床型：</span>1张2米特大床 或 2张1.2米单人床</li></itemtemplate><itemtemplate><li><span class="t">窗户：</span>有窗</li></itemtemplate><itemtemplate><li><span class="t">可加床：</span>RMB 230/床/间夜</li></itemtemplate><itemtemplate><li><span class="t">无烟：</span>不可吸烟</li></itemtemplate>
            </ul>
			<p class="hrd-info-base-describe">客人预订至尊湖景房时请备注具体需求信息（预订大床还是双床），以便酒店提供更好的服务。部分房型带柱子。</p>
        </div>
	</div>
	<div class="hrd-allfac">
        <div class="hrd-allfac-title">所有房型设施</div>
		<ul class="hrd-allfac-list">
            
                    <li>
                        <span class="t">
                            便利设施:
                        </span>
                        雨伞、书桌、多种规格电源插座、房内保险箱、空调、衣柜/衣橱、针线包、220V电压插座、遮光窗帘、自动窗帘、<span class="base_txtgray">沙发</span>、开夜床、电子秤、房间内高速上网、客房WIFI覆盖、客房WIFI覆盖<span class="text_green">免费</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            媒体科技：
                        </span>
                        国内长途电话、国际长途电话、有线频道、液晶电视机、iPod音乐基座、电话
                    </li>
                    
                    <li>
                        <span class="t">
                            食品饮品：
                        </span>
                        电热水壶、咖啡壶/茶壶、<span class="text_green">免费</span>瓶装水、迷你吧、小冰箱、<span class="base_txtgray">咖啡机</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            浴室：
                        </span>
                        拖鞋、浴室化妆放大镜、24小时热水、<span class="text_green">免费</span>洗漱用品(6样以上)、浴衣、浴缸、独立淋浴间、吹风机、洗浴间电视、淋浴
                    </li>
                    
                    <li>
                        <span class="t">
                            室外景观：
                        </span>
                        城景、湖景、花园景、享有风景
                    </li>
                    
                    <li>
                        <span class="t">
                            其他：
                        </span>
                        <span class="base_txtgray">连通房</span>、唤醒服务、语音留言、欢迎礼品
                    </li>
                    
                    <li>
                        <span class="t">
                            (灰色文字表示此房型部分房间有此设备) 
                        </span>
                        
                    </li>
                    
		</ul>
	</div>    
    
</div>    

</td>
</tr>




<tr class="" expand="" brid="693188" guid="9f647010-739f-4781-a1b7-49609d87445d" data-disable="0">




<td class="room_type td693188" data-baseroomid="693188" data-masterbasicroomid="693188" data-hotelid="428365" id="693188" rowspan="5" data-roomlist="69565349,69565408,69565410,69565352,182899191," data-idlist="69565349FG,69565408PP,69565410PP,69565352FG,182899191FG,">

<a id="roomRepeater_ctl03_subRoomRepeater_ctl00_linkImage" class="pic J_show_room_detail" rel="nofollow" onclick="HotelRoom.onNameNewClick(this)" href="javascript:void(0);"><img id="roomRepeater_ctl03_subRoomRepeater_ctl00_imageRoomImg" _src="//dimg12.c-ctrip.com/images/200p0k000000bpqnfD8D2_R_300_225.jpg" src="//dimg12.c-ctrip.com/images/200p0k000000bpqnfD8D2_R_130_130.jpg" style="border-width:0px;" /></a>
<a rel="nofollow" class="room_unfold J_show_room_detail" href="javascript:void(0);" onclick="HotelRoom.onNameNewClick(this)">
    行政全湖景套房
    <br />
    
    
    
     <span>查看详情</span>
    
</a>
    
    
</td><td class="child_name " data-firstmap="69565349FG,69565408FG,69565410FG,69565352FG,182899191FG," data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="2480" data-bed="1" data-policy="3" data-bf="3" data-network="1|2" data-roomid="69565349FG" data-reserve="1" data-pay="2">
<span class="room_type_name">(限时促销)</span>

<span class="label_onsale_txt" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'活动房型每间每晚最高可减1240元&lt;br/&gt;1、仅适用于活动期间且带有“金秋特惠”活动标签的酒店产品；&#10;&#10;2、如订单修改时优惠政策发生变动，则以最新的优惠政策为准；&#10;&#10;3、如出现恶意下单、利用程序漏洞等作弊行为，携程有权取消您本次活动订单；&#10;&#10;4、携程旅行网在法律允许范围内对本活动拥有最终解释权。'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">金秋特惠</span><span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="col4">无早</td>
<td class="col5"><span id="roomRepeater_ctl03_subRoomRepeater_ctl00_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><div class="hlist_item_price2_sec" style="color:#333;"><dfn>¥</dfn><span>2480</span></div><span class="base_price"><dfn>¥</dfn>1240</span><div class="text-grayMiddle"><span>促销优惠减1240</span></div></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl03_subRoomRepeater_ctl00_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl03_subRoomRepeater_ctl00_lblSuperPrice" class="super_price">立即确认超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565349,0,0.0,1240,FG,0.0,0.0,0,T,大床,0,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565349&quot;,&quot;basicroomid&quot;:&quot;693188&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;4&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565349&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;1240&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565349&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=2480&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last">仅剩2间</div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693188" guid="23307346-f37a-4f69-937b-4416d1eedeff" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1858" data-bed="1" data-policy="3" data-bf="3" data-network="1|2" data-roomid="69565408PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购.)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="col4">无早</td>
<td class="col5"><span id="roomRepeater_ctl03_subRoomRepeater_ctl01_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1858</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl03_subRoomRepeater_ctl01_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl03_subRoomRepeater_ctl01_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565408,0,0.0,1858,PP,0,0.0,0,T,大床,0,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565408&quot;,&quot;basicroomid&quot;:&quot;693188&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;4&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;2&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565408&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565408&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1858&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last">房量紧张</div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693188" guid="eeeec033-288d-4230-a2a7-da178547bfb2" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1948" data-bed="1" data-policy="3" data-bf="1" data-network="1|2" data-roomid="69565410PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购.)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl03_subRoomRepeater_ctl02_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1948</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl03_subRoomRepeater_ctl02_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl03_subRoomRepeater_ctl02_lblSuperPrice" class="super_price">双早超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565410,0,0.0,1948,PP,0,0.0,0,T,大床,2,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565410&quot;,&quot;basicroomid&quot;:&quot;693188&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;4&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565410&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565410&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1948&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last">房量紧张</div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="693188" guid="0e319da7-a6ae-45d2-93d2-7256bbf336d5" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1988" data-bed="1" data-policy="3" data-bf="1" data-network="1|2" data-roomid="69565352FG" data-reserve="1" data-pay="2">
<span class="room_type_name">(限时促销)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl03_subRoomRepeater_ctl03_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1988</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl03_subRoomRepeater_ctl03_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl03_subRoomRepeater_ctl03_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565352,0,0.0,1988,FG,0.0,0.0,0,T,大床,2,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565352&quot;,&quot;basicroomid&quot;:&quot;693188&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;4&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565352&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565352&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1988&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last">房量紧张</div>
</div>
</td>
</tr>


<tr class="unexpanded last_room" expand="" brid="693188" guid="2277d51f-fbe8-41c4-a193-bed6c77b4c36" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="2180" data-bed="1" data-policy="3" data-bf="1" data-network="1|2" data-roomid="182899191FG" data-baseroominfo="{&quot;RoomUrl&quot;:&quot;//dimg12.c-ctrip.com/images/200p0k000000bpqnfD8D2_R_300_225.jpg&quot;,&quot;RoomID&quot;:693188,&quot;RoomName&quot;:&quot;行政全湖景套房&quot;,&quot;BaseRoomInfo&quot;:&quot;90平方米&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;20-25层&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;不可吸烟&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;1张2米特大床&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;2人&quot;,&quot;ConvenientFacilities&quot;:null,&quot;MediaTechnology&quot;:null,&quot;FoodBeverages&quot;:null,&quot;Bathroom&quot;:null,&quot;OutdoorsViews&quot;:null,&quot;ServicesOthers&quot;:null,&quot;PriceNum&quot;:4,&quot;LowPrice&quot;:1240.0,&quot;RoomTotalNum&quot;:5}" data-baseroomname="行政全湖景套房" data-reserve="0" data-pay="2">
<span class="room_type_name">标准价</span>

<input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl03_subRoomRepeater_ctl04_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>2180</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl03_subRoomRepeater_ctl04_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl03_subRoomRepeater_ctl04_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span><a id="roomRepeater_ctl03_subRoomRepeater_ctl04_lkBookingButton" class="btns_base22 btns_base22_dis" data-order="182899191,0,0.0,2180,FG,0.0,0.0,0,F,大床,2,不可取消,T,F,F,F,428365,372135," href="javascript:void(0)\"><div class="btns_base22_main">订完</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a></span>


<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="clicked hidden">
<td colspan="9">
<div id="rdn693188">
	<a class="c_close j_detail_close" href="javascript:void(0)">×</a>
	<div class="hrd-title">
        行政全湖景套房
        
	</div>
	<div class="hrd-info">
		<div class="hrd-info-pic" data-baseroomvrimage="" style="overflow: hidden">
            
		    <span class="prev" style="display:none"><b></b></span><span class="next" style=" "><b></b></span><div style="width:300%" class="J_slider_box_in" data-page="3"><ul><li><img src="//dimg12.c-ctrip.com/images/200p0k000000bpqnfD8D2_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg10.c-ctrip.com/images/200j0k000000bqohcF110_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg11.c-ctrip.com/images/200504000000018vf368F_R_300_225.jpg" width="300" height="225" alt="" /></li></ul></div>
		</div>
		<div class="hrd-info-base">
            <ul class="hrd-info-base-list">
				<itemtemplate><li><span class="t">建筑面积:</span>90平方米</li></itemtemplate><itemtemplate><li><span class="t">楼层:</span>20-25层</li></itemtemplate><itemtemplate><li><span class="t">床型：</span>1张2米特大床</li></itemtemplate><itemtemplate><li><span class="t">窗户：</span>有窗</li></itemtemplate><itemtemplate><li><span class="t">可加床：</span>RMB 230/床/间夜</li></itemtemplate><itemtemplate><li><span class="t">无烟：</span>不可吸烟</li></itemtemplate>
            </ul>
			<p class="hrd-info-base-describe"></p>
        </div>
	</div>
	<div class="hrd-allfac">
        <div class="hrd-allfac-title">所有房型设施</div>
		<ul class="hrd-allfac-list">
            
                    <li>
                        <span class="t">
                            便利设施:
                        </span>
                        雨伞、书桌、多种规格电源插座、房内保险箱、空调、衣柜/衣橱、针线包、220V电压插座、遮光窗帘、自动窗帘、<span class="base_txtgray">沙发</span>、开夜床、电子秤、房间内高速上网、客房WIFI覆盖、客房WIFI覆盖<span class="text_green">免费</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            媒体科技：
                        </span>
                        国内长途电话、国际长途电话、有线频道、液晶电视机、iPod音乐基座、电话
                    </li>
                    
                    <li>
                        <span class="t">
                            食品饮品：
                        </span>
                        电热水壶、咖啡壶/茶壶、<span class="text_green">免费</span>瓶装水、迷你吧、小冰箱、<span class="base_txtgray">咖啡机</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            浴室：
                        </span>
                        拖鞋、浴室化妆放大镜、24小时热水、<span class="text_green">免费</span>洗漱用品(6样以上)、浴衣、浴缸、独立淋浴间、吹风机、洗浴间电视、淋浴
                    </li>
                    
                    <li>
                        <span class="t">
                            室外景观：
                        </span>
                        城景、湖景、花园景、享有风景
                    </li>
                    
                    <li>
                        <span class="t">
                            其他：
                        </span>
                        <span class="base_txtgray">连通房</span>、唤醒服务、语音留言、欢迎礼品
                    </li>
                    
                    <li>
                        <span class="t">
                            (灰色文字表示此房型部分房间有此设备) 
                        </span>
                        
                    </li>
                    
		</ul>
	</div>    
    
</div>    

</td>
</tr>




<tr class="" expand="" brid="35340716" guid="51c8018f-b6e8-489e-91a4-55dffc1b6e23" data-disable="0">




<td class="room_type td35340716" data-baseroomid="35340716" data-masterbasicroomid="35340716" data-hotelid="428365" id="35340716" rowspan="3" data-roomlist="69565413,69565354,69565413," data-idlist="69565413PP,69565354FG,69565413PP1001031205,">

<a id="roomRepeater_ctl04_subRoomRepeater_ctl00_linkImage" class="pic J_show_room_detail" rel="nofollow" onclick="HotelRoom.onNameNewClick(this)" href="javascript:void(0);"><img id="roomRepeater_ctl04_subRoomRepeater_ctl00_imageRoomImg" _src="//dimg10.c-ctrip.com/images/200i0u000000jagom2525_R_300_225.jpg" src="//dimg10.c-ctrip.com/images/200i0u000000jagom2525_R_130_130.jpg" style="border-width:0px;" /></a>
<a rel="nofollow" class="room_unfold J_show_room_detail" href="javascript:void(0);" onclick="HotelRoom.onNameNewClick(this)">
    亲子家庭房
    <br />
    
    
    
     <span>查看详情</span>
    
</a>
    
    
</td><td class="child_name " data-firstmap="69565413PP,69565354PP,69565413PP," data-triple="1" data-ctrip="1" data-hotelinvoice="1" data-price="1556" data-bed="1|2" data-policy="3" data-bf="4" data-network="1|2" data-roomid="69565413PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(帐篷童趣)(限时抢购)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'童趣帐篷、全套儿童洗浴床上用品等精心主题布置，趣味十足； &lt;br /&gt;宝贝享用 “聪少甜品”特别订制甜品一份； &lt;br /&gt;无限畅玩儿童乐园； &lt;br /&gt;宝贝获得一次与五星级大厨学做美食机会；&lt;br /&gt;宝贝获得一次酒店开心农场体验活动的机会 &lt;br /&gt;入住首晚全家享用5款精致小食礼包； &lt;br /&gt;住店期间可经贵宾专属通道带宝宝前往黄兴公园开展野趣活动：&lt;br /&gt;挖沙、钓鱼、写生、寻宝等游戏；&lt;br /&gt;全家欢享自助晚餐一次（限三位成人），烤肉、小南国中餐特别出品的地道上海美食，款款让您味蕾放纵。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天三早</td>
<td class="col5"><span id="roomRepeater_ctl04_subRoomRepeater_ctl00_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住3人" class="htl_room_person03"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1556</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl04_subRoomRepeater_ctl00_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl04_subRoomRepeater_ctl00_lblSuperPrice" class="super_price">立即确认超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565413,0,0.0,1556,PP,0,0.0,0,T,大/双,3,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565413&quot;,&quot;basicroomid&quot;:&quot;35340716&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;3&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;2&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565413&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565413&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1556&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="unexpanded" expand="" brid="35340716" guid="c416aaf2-9775-4010-afd0-9a1f2664765b" data-disable="0">


<td class="child_name " data-triple="1" data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="1588" data-bed="1|2" data-policy="3" data-bf="4" data-network="1|2" data-roomid="69565354FG" data-reserve="1" data-pay="2">
<span class="room_type_name">(限时促销)(帐篷童趣)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'童趣帐篷、全套儿童洗浴床上用品等精心主题布置，趣味十足；&lt;br /&gt;宝贝获赠 “聪少甜品”特别订制甜品一份 无限畅玩儿童乐园；&lt;br /&gt;宝贝获得一次与五星级大厨学做美食机会；&lt;br /&gt;宝贝获得一次酒店开心农场体验活动得机会。&lt;br /&gt;入住首晚全家享用5款精致小食礼包；&lt;br /&gt;住店期间可经贵宾专属通道带宝宝前往黄兴公园开展野趣活动：挖沙、钓鱼、写生、寻宝等游戏； &lt;br /&gt;全家欢享自助晚餐一次（限三位成人），烤肉、小南国中餐特别出品的地道上海美食，款款让您味蕾放纵','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大/双</td>
<td class="text_green col4">每天三早</td>
<td class="col5"><span id="roomRepeater_ctl04_subRoomRepeater_ctl01_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住3人" class="htl_room_person03"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1588</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl04_subRoomRepeater_ctl01_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl04_subRoomRepeater_ctl01_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565354,0,0.0,1588,FG,0.0,0.0,0,T,大/双,3,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565354&quot;,&quot;basicroomid&quot;:&quot;35340716&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;3&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565354&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565354&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1588&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last">房量紧张</div>
</div>
</td>
</tr>


<tr class="unexpanded last_room" expand="" brid="35340716" guid="4233997b-9c8c-4774-80b8-c77db12c6c84" data-disable="0">


<td class="child_name " data-triple="1" data-hotelinvoice="1" data-price="1556" data-bed="1" data-policy="3" data-bf="4" data-network="1|2" data-roomid="69565413PP1001031205" data-baseroominfo="{&quot;RoomUrl&quot;:&quot;//dimg10.c-ctrip.com/images/200i0u000000jagom2525_R_300_225.jpg&quot;,&quot;RoomID&quot;:35340716,&quot;RoomName&quot;:&quot;亲子家庭房&quot;,&quot;BaseRoomInfo&quot;:&quot;65平方米&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;7,20-25层&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;不可吸烟&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;1张2米特大床 或 2张1.1米小型双人床&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;3人&quot;,&quot;ConvenientFacilities&quot;:null,&quot;MediaTechnology&quot;:null,&quot;FoodBeverages&quot;:null,&quot;Bathroom&quot;:null,&quot;OutdoorsViews&quot;:null,&quot;ServicesOthers&quot;:null,&quot;PriceNum&quot;:3,&quot;LowPrice&quot;:1556.0,&quot;RoomTotalNum&quot;:3}" data-baseroomname="亲子家庭房" data-reserve="1" data-pay="3">
<span class="room_type_name">(帐篷童趣)(限时抢购)（大床）</span>

<input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="text_green col4">每天三早</td>
<td class="col5"><span id="roomRepeater_ctl04_subRoomRepeater_ctl02_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住3人" class="htl_room_person03"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>1556</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl04_subRoomRepeater_ctl02_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl04_subRoomRepeater_ctl02_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565413,1001031205,0.0,1556,PP,0,0.0,0,F,大床,3,不可取消,F,T,F,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565413&quot;,&quot;basicroomid&quot;:&quot;35340716&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;3&quot;,&quot;roomctype&quot;:&quot;1&quot;,&quot;lowerprice&quot;:&quot;2&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;大双床&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;1001031205&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565413&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;1001031205&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565413&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=1001031205&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=1556&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last"></div>
</div>
</td>
</tr>


<tr class="clicked hidden">
<td colspan="9">
<div id="rdn35340716">
	<a class="c_close j_detail_close" href="javascript:void(0)">×</a>
	<div class="hrd-title">
        亲子家庭房
        
	</div>
	<div class="hrd-info">
		<div class="hrd-info-pic" data-baseroomvrimage="" style="overflow: hidden">
            
		    <span class="prev" style="display:none"><b></b></span><span class="next" style=" "><b></b></span><div style="width:1400%" class="J_slider_box_in" data-page="14"><ul><li><img src="//dimg10.c-ctrip.com/images/200i0u000000jagom2525_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg10.c-ctrip.com/images/200w0u000000jhogeF03B_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg11.c-ctrip.com/images/200j0f0000007b0zfFDAA_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/20030f0000007ek2oF079_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg11.c-ctrip.com/images/200s0u000000jiiqi7D26_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg12.c-ctrip.com/images/20040f0000007ex5a8BB8_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg11.c-ctrip.com/images/200i0u000000jagtw3A79_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg12.c-ctrip.com/images/200j0u000000jb5vqDA4F_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/20050f0000007ksv1DD7A_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg12.c-ctrip.com/images/200d0f0000007kmylDB26_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg11.c-ctrip.com/images/200g0f0000007kn7b84A8_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg11.c-ctrip.com/images/20070f0000007kphjFAC8_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/200u0f0000007ej6eD476_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/20050f0000007emc1E8FD_R_300_225.jpg" width="300" height="225" alt="" /></li></ul></div>
		</div>
		<div class="hrd-info-base">
            <ul class="hrd-info-base-list">
				<itemtemplate><li><span class="t">建筑面积:</span>65平方米</li></itemtemplate><itemtemplate><li><span class="t">楼层:</span>7,20-25层</li></itemtemplate><itemtemplate><li><span class="t">床型：</span>1张2米特大床 或 2张1.1米小型双人床</li></itemtemplate><itemtemplate><li><span class="t">窗户：</span>有窗</li></itemtemplate><itemtemplate><li><span class="t">可加床：</span>不可加床</li></itemtemplate><itemtemplate><li><span class="t">无烟：</span>不可吸烟</li></itemtemplate>
            </ul>
			<p class="hrd-info-base-describe"></p>
        </div>
	</div>
	<div class="hrd-allfac">
        <div class="hrd-allfac-title">所有房型设施</div>
		<ul class="hrd-allfac-list">
            
                    <li>
                        <span class="t">
                            便利设施:
                        </span>
                        雨伞、书桌、多种规格电源插座、房内保险箱、空调、衣柜/衣橱、针线包、220V电压插座、遮光窗帘、自动窗帘、开夜床、电子秤、房间内高速上网、客房WIFI覆盖、客房WIFI覆盖<span class="text_green">免费</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            媒体科技：
                        </span>
                        国内长途电话、国际长途电话、有线频道、液晶电视机、iPod音乐基座、电话
                    </li>
                    
                    <li>
                        <span class="t">
                            食品饮品：
                        </span>
                        电热水壶、咖啡壶/茶壶、<span class="text_green">免费</span>瓶装水、迷你吧、小冰箱
                    </li>
                    
                    <li>
                        <span class="t">
                            浴室：
                        </span>
                        拖鞋、浴室化妆放大镜、24小时热水、<span class="text_green">免费</span>洗漱用品(6样以上)、浴衣、浴缸、独立淋浴间、吹风机、洗浴间电视、淋浴
                    </li>
                    
                    <li>
                        <span class="t">
                            室外景观：
                        </span>
                        城景、湖景、花园景、享有风景
                    </li>
                    
                    <li>
                        <span class="t">
                            其他：
                        </span>
                        唤醒服务、语音留言、欢迎礼品
                    </li>
                    
		</ul>
	</div>    
    
</div>    

</td>
</tr>




<tr class="" expand="" brid="35340805" guid="bbe92e5b-cf23-4ba7-95bd-74088b042cdd" data-disable="0">




<td class="room_type td35340805" data-baseroomid="35340805" data-masterbasicroomid="35340805" data-hotelid="428365" id="35340805" rowspan="2" data-roomlist="69647146,69565359," data-idlist="69647146PP,69565359FG,">

<a id="roomRepeater_ctl05_subRoomRepeater_ctl00_linkImage" class="pic J_show_room_detail" rel="nofollow" onclick="HotelRoom.onNameNewClick(this)" href="javascript:void(0);"><img id="roomRepeater_ctl05_subRoomRepeater_ctl00_imageRoomImg" _src="//dimg10.c-ctrip.com/images/200o0f0000007ejjwD5E8_R_300_225.jpg" src="//dimg10.c-ctrip.com/images/200o0f0000007ejjwD5E8_R_130_130.jpg" style="border-width:0px;" /></a>
<a rel="nofollow" class="room_unfold J_show_room_detail" href="javascript:void(0);" onclick="HotelRoom.onNameNewClick(this)">
    亲子家庭套房
    <br />
    
    
    
     <span>查看详情</span>
    
</a>
    
    
</td><td class="child_name " data-firstmap="69647146PP,69565359PP," data-ctrip="1" data-hotelinvoice="1" data-price="2239" data-bed="4" data-policy="3" data-bf="4" data-network="1" data-roomid="69647146PP" data-reserve="1" data-pay="3">
<span class="room_type_name">(帐篷童趣)(限时抢购.)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'童趣帐篷、全套儿童洗浴床上用品等精心主题布置，趣味十足； &lt;br /&gt;宝贝可享用 “聪少甜品”特别订制甜品一份； &lt;br /&gt;无限畅玩儿童乐园； &lt;br /&gt;宝贝获得一次与五星级大厨学做美食机会； &lt;br /&gt;宝贝获得一次酒店开心农场体验活动得机会&lt;br /&gt;入住首晚全家享用5款精致小食礼包； &lt;br /&gt;住店期间可经贵宾专属通道带宝宝前往黄兴公园开展野趣活动：挖沙、钓鱼、写生、寻宝等游戏； &lt;br /&gt;全家欢享自助晚餐一次（限四位成人），烤肉、小南国中餐特别出品的地道上海美食，款款让您味蕾放纵。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">多床</td>
<td class="text_green col4">每天四早</td>
<td class="col5"><span id="roomRepeater_ctl05_subRoomRepeater_ctl00_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间无线宽带免费。'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">无线免费</span></td>
<td class="col_person"><span title="每间最多入住4人" class="htl_room_persons">×4</span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>2239</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl05_subRoomRepeater_ctl00_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl05_subRoomRepeater_ctl00_lblSuperPrice" class="super_price">立即确认超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69647146,0,0.0,2239,PP,0,0.0,0,T,多床,4,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69647146&quot;,&quot;basicroomid&quot;:&quot;35340805&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;2&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;1&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69647146&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69647146&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=2239&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last">房量紧张</div>
</div>
</td>
</tr>


<tr class="unexpanded last_room" expand="" brid="35340805" guid="cbca0963-a6d9-45d9-a8d7-05fbfcdf01b0" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="2288" data-bed="4" data-policy="3" data-bf="4" data-network="1" data-roomid="69565359FG" data-baseroominfo="{&quot;RoomUrl&quot;:&quot;//dimg10.c-ctrip.com/images/200o0f0000007ejjwD5E8_R_300_225.jpg&quot;,&quot;RoomID&quot;:35340805,&quot;RoomName&quot;:&quot;亲子家庭套房&quot;,&quot;BaseRoomInfo&quot;:&quot;90平方米&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;20-25层&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;不可吸烟&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;1张1.2米沙发床 和 1张2米特大床&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;4人&quot;,&quot;ConvenientFacilities&quot;:null,&quot;MediaTechnology&quot;:null,&quot;FoodBeverages&quot;:null,&quot;Bathroom&quot;:null,&quot;OutdoorsViews&quot;:null,&quot;ServicesOthers&quot;:null,&quot;PriceNum&quot;:2,&quot;LowPrice&quot;:2239.0,&quot;RoomTotalNum&quot;:2}" data-baseroomname="亲子家庭套房" data-reserve="1" data-pay="2">
<span class="room_type_name">(限时促销)(帐篷童趣)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'全家欢享自助晚餐一次（限四位成人），烤肉、小南国中餐特别出品的地道上海美食，款款让您味蕾放纵&lt;br /&gt; 童趣帐篷、全套儿童洗浴床上用品等精心主题布置，趣味十足&lt;br /&gt; 宝贝获赠 “聪少甜品”特别订制甜品一份&lt;br /&gt;无限畅玩儿童乐园&lt;br /&gt;宝贝获得一次与五星级大厨学做美食机会&lt;br /&gt;宝贝获得一次酒店开心农场体验活动得机会&lt;br /&gt;入住首晚全家享用5款精致小食礼包&lt;br /&gt;住店期间，可经贵宾专属通道带宝宝前往黄兴公园开展野趣活动：挖沙、钓鱼、写生、寻宝等游戏','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">多床</td>
<td class="text_green col4">每天四早</td>
<td class="col5"><span id="roomRepeater_ctl05_subRoomRepeater_ctl01_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间无线宽带免费。'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">无线免费</span></td>
<td class="col_person"><span title="每间最多入住4人" class="htl_room_persons">×4</span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>2288</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl05_subRoomRepeater_ctl01_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl05_subRoomRepeater_ctl01_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="69565359,0,0.0,2288,FG,0.0,0.0,0,T,多床,4,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;69565359&quot;,&quot;basicroomid&quot;:&quot;35340805&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;2&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;69565359&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=69565359&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=2288&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last">房量紧张</div>
</div>
</td>
</tr>


<tr class="clicked hidden">
<td colspan="9">
<div id="rdn35340805">
	<a class="c_close j_detail_close" href="javascript:void(0)">×</a>
	<div class="hrd-title">
        亲子家庭套房
        
	</div>
	<div class="hrd-info">
		<div class="hrd-info-pic" data-baseroomvrimage="" style="overflow: hidden">
            
		    <span class="prev" style="display:none"><b></b></span><span class="next" style=" "><b></b></span><div style="width:1400%" class="J_slider_box_in" data-page="14"><ul><li><img src="//dimg10.c-ctrip.com/images/200o0f0000007ejjwD5E8_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg12.c-ctrip.com/images/200s0f0000007eklb4158_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg11.c-ctrip.com/images/200s0u000000jiiqi7D26_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg11.c-ctrip.com/images/200i0u000000jagtw3A79_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg12.c-ctrip.com/images/200j0u000000jb5vqDA4F_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg10.c-ctrip.com/images/200i0f0000007eimp251A_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg11.c-ctrip.com/images/20030f0000007kos6D50A_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/200g0f0000007knbcDF3F_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/200d0f0000007kn2o5191_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg10.c-ctrip.com/images/20060f0000007eizk5359_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg10.c-ctrip.com/images/20050f0000007ksz58A8D_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/200r0f0000007ek1y9D27_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg12.c-ctrip.com/images/20080f0000007eisfA00C_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg10.c-ctrip.com/images/200n0f0000007ejbt9B43_R_300_225.jpg" width="300" height="225" alt="" /></li></ul></div>
		</div>
		<div class="hrd-info-base">
            <ul class="hrd-info-base-list">
				<itemtemplate><li><span class="t">建筑面积:</span>90平方米</li></itemtemplate><itemtemplate><li><span class="t">楼层:</span>20-25层</li></itemtemplate><itemtemplate><li><span class="t">床型：</span>1张1.2米沙发床 和 1张2米特大床</li></itemtemplate><itemtemplate><li><span class="t">窗户：</span>有窗</li></itemtemplate><itemtemplate><li><span class="t">可加床：</span>不可加床</li></itemtemplate><itemtemplate><li><span class="t">无烟：</span>不可吸烟</li></itemtemplate>
            </ul>
			<p class="hrd-info-base-describe">精心布置的沙发床/母子床，小青蛙牙刷套装，米老鼠漱口杯，原木增高凳，托马斯等可爱主题床品，环保儿童帐篷，主题益智玩具，儿童浴盆浴袍，儿童绘本书籍，儿童烹饪、礼仪等课程体验、黄兴公园挖沙写生等活动。</p>
        </div>
	</div>
	<div class="hrd-allfac">
        <div class="hrd-allfac-title">所有房型设施</div>
		<ul class="hrd-allfac-list">
            
                    <li>
                        <span class="t">
                            便利设施:
                        </span>
                        雨伞、书桌、多种规格电源插座、房内保险箱、空调、衣柜/衣橱、针线包、220V电压插座、遮光窗帘、自动窗帘、开夜床、电子秤、房间内高速上网、客房WIFI覆盖、客房WIFI覆盖<span class="text_green">免费</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            媒体科技：
                        </span>
                        国内长途电话、国际长途电话、有线频道、液晶电视机、iPod音乐基座、电话
                    </li>
                    
                    <li>
                        <span class="t">
                            食品饮品：
                        </span>
                        电热水壶、咖啡壶/茶壶、<span class="text_green">免费</span>瓶装水、迷你吧、小冰箱
                    </li>
                    
                    <li>
                        <span class="t">
                            浴室：
                        </span>
                        拖鞋、浴室化妆放大镜、24小时热水、<span class="text_green">免费</span>洗漱用品(6样以上)、浴衣、浴缸、独立淋浴间、吹风机、洗浴间电视、淋浴
                    </li>
                    
                    <li>
                        <span class="t">
                            室外景观：
                        </span>
                        城景、湖景、花园景、享有风景
                    </li>
                    
                    <li>
                        <span class="t">
                            其他：
                        </span>
                        唤醒服务、语音留言、欢迎礼品
                    </li>
                    
		</ul>
	</div>    
    
</div>    

</td>
</tr>




<tr class="" expand="" brid="2210182" guid="98b6b749-fc1f-4055-806a-76c378dad421" data-disable="0">




<td class="room_type td2210182" data-baseroomid="2210182" data-masterbasicroomid="2210182" data-hotelid="428365" id="2210182" rowspan="2" data-roomlist="78143116,78143132," data-idlist="78143116FG,78143132PP,">

<a id="roomRepeater_ctl06_subRoomRepeater_ctl00_linkImage" class="pic J_show_room_detail" rel="nofollow" onclick="HotelRoom.onNameNewClick(this)" href="javascript:void(0);"><img id="roomRepeater_ctl06_subRoomRepeater_ctl00_imageRoomImg" _src="//dimg12.c-ctrip.com/images/200q0k000000br7oeE7E6_R_300_225.jpg" src="//dimg12.c-ctrip.com/images/200q0k000000br7oeE7E6_R_130_130.jpg" style="border-width:0px;" /></a>
<a rel="nofollow" class="room_unfold J_show_room_detail" href="javascript:void(0);" onclick="HotelRoom.onNameNewClick(this)">
    总统套房
    <br />
    
    
    
     <span>查看详情</span>
    
</a>
    
    
</td><td class="child_name " data-firstmap="78143116FG,78143132FG," data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="10880" data-bed="1" data-policy="3" data-bf="1" data-network="1|2" data-roomid="78143116FG" data-reserve="1" data-pay="2">
<span class="room_type_name">(限时促销)</span>

<span class="label_onsale_txt" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'活动房型每间每晚最高可减5440元&lt;br/&gt;1、仅适用于活动期间且带有“金秋特惠”活动标签的酒店产品；&#10;&#10;2、如订单修改时优惠政策发生变动，则以最新的优惠政策为准；&#10;&#10;3、如出现恶意下单、利用程序漏洞等作弊行为，携程有权取消您本次活动订单；&#10;&#10;4、携程旅行网在法律允许范围内对本活动拥有最终解释权。'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">金秋特惠</span><span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl06_subRoomRepeater_ctl00_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。若未按时入住，我们将扣除您全额或部分房费。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><div class="hlist_item_price2_sec" style="color:#333;"><dfn>¥</dfn><span>10880</span></div><span class="base_price"><dfn>¥</dfn>5440</span><div class="text-grayMiddle"><span>促销优惠减5440</span></div></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl06_subRoomRepeater_ctl00_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl06_subRoomRepeater_ctl00_lblSuperPrice" class="super_price">双早超值价</span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="78143116,0,0.0,5440,FG,0.0,0.0,0,T,大床,2,不可取消,T,T,T,F,428365,372135," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;78143116&quot;,&quot;basicroomid&quot;:&quot;2210182&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;2&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;0&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;78143116&quot;, &quot;payment&quot;:&quot;FG&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;5440&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=78143116&amp;Paymentterm=FG&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=10880&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin02"><span class="payment_txt" title="房量紧张需提供信用卡或积分担保">担保</span></div></a>
<div class="hotel_room_last">房量紧张</div>
</div>
</td>
</tr>


<tr class="unexpanded last_room" expand="" brid="2210182" guid="f26371cf-3b1f-490e-aad8-1f4f01716cfd" data-disable="0">


<td class="child_name " data-addbed="1" data-ctrip="1" data-hotelinvoice="1" data-price="5699" data-bed="1" data-policy="3" data-bf="1" data-network="1|2" data-roomid="78143132PP" data-baseroominfo="{&quot;RoomUrl&quot;:&quot;//dimg12.c-ctrip.com/images/200q0k000000br7oeE7E6_R_300_225.jpg&quot;,&quot;RoomID&quot;:2210182,&quot;RoomName&quot;:&quot;总统套房&quot;,&quot;BaseRoomInfo&quot;:&quot;360平方米&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;25层&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;不可吸烟&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;1张2米特大床&lt;span class=\&quot;line\&quot;&gt;|&lt;/span&gt;2人&quot;,&quot;ConvenientFacilities&quot;:null,&quot;MediaTechnology&quot;:null,&quot;FoodBeverages&quot;:null,&quot;Bathroom&quot;:null,&quot;OutdoorsViews&quot;:null,&quot;ServicesOthers&quot;:null,&quot;PriceNum&quot;:2,&quot;LowPrice&quot;:5440.0,&quot;RoomTotalNum&quot;:2}" data-baseroomname="总统套房" data-reserve="1" data-pay="3">
<span class="room_type_name">(限时抢购)</span>

<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempGift','content':{'gift':'T','giftinfo':'入住首日房内提供精致小食一份。','ShadowGift':'F','package':'F'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'gift'}}"><span class="label_onsale_orange" style="margin-right: 0px">礼</span></span><input type="hidden" id="spfrom" class="spfrom" value="-1" />












</td>
<td class="col3">大床</td>
<td class="text_green col4">每天双早</td>
<td class="col5"><span id="roomRepeater_ctl06_subRoomRepeater_ctl01_lblBroadnet" data-role="jmp" class="net_free" data-params="{'options':{'type':'jmp_table','template':'#jmpTempNet','content':{'txt':'全部房间有线宽带免费，全部房间无线宽带免费'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'net'}}">免费</span></td>
<td class="col_person"><span title="每间最多入住2人" class="htl_room_person02"> </span></td>
<td class="col_policy"><span class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCommon','content':{'txt':'订单一经确认，不可取消、修改。未入住或取消订单，全部或部分预付房费不予退还。如若您的旅程尚未确定，建议购买取消险哦~'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}">不可取消</span><span class="confirm_green">立即确认</span></td>
<td>
	<div><span class="base_price"><dfn>¥</dfn>5699</span></div>
	<p class="base_box">
		
		
	</p>
<p class="base_box">
    <span id="roomRepeater_ctl06_subRoomRepeater_ctl01_lblIcoVip" class="label_onsale_txt" style="border:none; cursor:default"></span>
</p>
	<p class="base_box"><span id="roomRepeater_ctl06_subRoomRepeater_ctl01_lblSuperPrice" class="super_price"></span></p>
</td>
<td class="col7">


<div class="book_type">
<span></span>

<a data-ismember="false" class="btns_base22 J_hotel_order" rel="nofollow" data-order="78143132,0,0.0,5699,PP,0,0.0,0,T,大床,2,不可取消,F,T,T,F,428365,1700870," tracekey="htl_mj_info" tracevalue="{&quot;hotelid&quot;:&quot;428365&quot;,&quot;roomid&quot;:&quot;78143132&quot;,&quot;basicroomid&quot;:&quot;2210182&quot;,&quot;checkin&quot;:&quot;2018-09-21&quot;,&quot;checkout&quot;:&quot;2018-09-22&quot;,&quot;roomsort&quot;:&quot;1&quot;,&quot;roomsum&quot;:&quot;2&quot;,&quot;roomctype&quot;:&quot;2&quot;,&quot;lowerprice&quot;:&quot;2&quot;,&quot;type&quot;:&quot;&quot;,&quot;agentname&quot;:&quot;&quot;,&quot;supplyid&quot;:&quot;0&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;cityid&quot;:&quot;2&quot;}" bookparam="{&quot;hotel&quot;:&quot;428365&quot;, &quot;room&quot;:&quot;78143132&quot;, &quot;payment&quot;:&quot;PP&quot;, &quot;StartDate&quot;:&quot;2018-09-21&quot;, &quot;DepDate&quot;:&quot;2018-09-22&quot;, &quot;useFG&quot;:&quot;F&quot;, &quot;swid&quot;:&quot;0&quot;, &quot;sctx&quot;:&quot;&quot;, &quot;defaultcoupon&quot;:&quot;&quot;, &quot;isLowestRoom&quot;:&quot;0&quot;, &quot;isTonightPromotion&quot;:&quot;0&quot;, &quot;roomNumbers&quot;:&quot;0&quot;, &quot;PPDSingleVal&quot;:&quot;0&quot;, &quot;returnurl&quot;:&quot;&quot;, &quot;ishotsale&quot;:&quot;&quot;, &quot;isPTXK&quot;:&quot;T&quot; }" href="/DomesticBook/InputNewOrder.aspx?hotelid=428365&amp;Room=78143132&amp;Paymentterm=PP&amp;StartDate=2018-09-21&amp;DepDate=2018-09-22&amp;requestTravelMoney=F&amp;usefg=F&amp;EDM=False&amp;swid=0&amp;sctx=&amp;defaultcoupon=&amp;&amp;operationtype=NEWHOTELORDER&amp;priceCx=5699&amp;isLowestRoom=0&amp;isTonightPromotion=0&amp;from=detail" onclick="window.HotelRoom.onOrderButtonClick(this);return false;"><div class="btns_base22_main">预订</div><div class="btns_base22_skin01"><span class="payment_txt" title="需预先支付房款">在线付</span></div></a>
<div class="hotel_room_last">仅剩1间</div>
</div>
</td>
</tr>


<tr class="clicked hidden">
<td colspan="9">
<div id="rdn2210182">
	<a class="c_close j_detail_close" href="javascript:void(0)">×</a>
	<div class="hrd-title">
        总统套房
        
	</div>
	<div class="hrd-info">
		<div class="hrd-info-pic" data-baseroomvrimage="" style="overflow: hidden">
            
		    <span class="prev" style="display:none"><b></b></span><span class="next" style=" "><b></b></span><div style="width:300%" class="J_slider_box_in" data-page="3"><ul><li><img src="//dimg12.c-ctrip.com/images/200q0k000000br7oeE7E6_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/200h0k000000br9b3E4B5_R_300_225.jpg" width="300" height="225" alt="" /></li></ul><ul><li><img src="//dimg13.c-ctrip.com/images/200p0i0000009a65e60B2_R_300_225.jpg" width="300" height="225" alt="" /></li></ul></div>
		</div>
		<div class="hrd-info-base">
            <ul class="hrd-info-base-list">
				<itemtemplate><li><span class="t">建筑面积:</span>360平方米</li></itemtemplate><itemtemplate><li><span class="t">楼层:</span>25层</li></itemtemplate><itemtemplate><li><span class="t">床型：</span>1张2米特大床</li></itemtemplate><itemtemplate><li><span class="t">窗户：</span>有窗</li></itemtemplate><itemtemplate><li><span class="t">可加床：</span>RMB 230/床/间夜</li></itemtemplate><itemtemplate><li><span class="t">无烟：</span>不可吸烟</li></itemtemplate>
            </ul>
			<p class="hrd-info-base-describe"></p>
        </div>
	</div>
	<div class="hrd-allfac">
        <div class="hrd-allfac-title">所有房型设施</div>
		<ul class="hrd-allfac-list">
            
                    <li>
                        <span class="t">
                            便利设施:
                        </span>
                        雨伞、书桌、多种规格电源插座、房内保险箱、空调、衣柜/衣橱、针线包、220V电压插座、遮光窗帘、自动窗帘、开夜床、电子秤、房间内高速上网、客房WIFI覆盖、客房WIFI覆盖<span class="text_green">免费</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            媒体科技：
                        </span>
                        国内长途电话、国际长途电话、有线频道、液晶电视机、iPod音乐基座、电话
                    </li>
                    
                    <li>
                        <span class="t">
                            食品饮品：
                        </span>
                        电热水壶、咖啡壶/茶壶、<span class="text_green">免费</span>瓶装水、迷你吧、小冰箱、<span class="base_txtgray">咖啡机</span>
                    </li>
                    
                    <li>
                        <span class="t">
                            浴室：
                        </span>
                        拖鞋、浴室化妆放大镜、24小时热水、<span class="text_green">免费</span>洗漱用品(6样以上)、浴衣、浴缸、独立淋浴间、吹风机、洗浴间电视、淋浴
                    </li>
                    
                    <li>
                        <span class="t">
                            室外景观：
                        </span>
                        城景、湖景、花园景、享有风景
                    </li>
                    
                    <li>
                        <span class="t">
                            其他：
                        </span>
                        唤醒服务、语音留言、欢迎礼品
                    </li>
                    
                    <li>
                        <span class="t">
                            (灰色文字表示此房型部分房间有此设备) 
                        </span>
                        
                    </li>
                    
		</ul>
	</div>    
    
</div>    

</td>
</tr>



</tbody></table>
</div>



<div class="htl_pic_pop detail_pic_box" style="display:none;" id="J_baseroomvr">
	<a href="javascript:void(0);" class="close">×</a>
    <div class="ctrip_360 ctrip_vr">
	    <div class="ctrip_360_bd">
		    <div class="ctrip_360_pic">
			    <div class="ctrip_360_pic_box">
				    <iframe style="width:100%;height:100%;" scrolling="no" frameborder="none" src="" name="J_baseroomvriframe" id="J_baseroomvriframe"></iframe>
			    </div>
                 <div class="ctrip_360_pic_btn">
				    <a href="javascript:;" class="btn_360 btn_play J_VRanimation"><i></i></a>
			    </div>
			    <div class="ctrip_360_tip">按住鼠标左键并上下左右拖动</div>
                <div class="ctrip_360_browser" style="display:none;">你的浏览器版本太低，请使用Chrome、FireFox、IE11以上版本的浏览器来观看VR图片。 </div>
		    </div>
		    <div class="ctrip_360_txt">
			    <a class="menu_360 menu_top menu_top_dis" href="javascript:;"></a>
			    <div class="ctrip_360_txt_list">
				    <ul class="ctrip_360_txt_cont">
				    </ul>
			    </div>
			    <a class="menu_360 menu_btm menu_btm_dis" href="javascript:;"></a>
		    </div>
	    </div>
    </div>
</div>

<script type="text/template" id="J_hourNoResultTpl">
&lt;td colspan="9" class="other_room_tips"&gt;&lt;i class="ico"&gt;&lt;/i&gt;&lt;p&gt;没有符合条件的房型，您可以减少当前筛选项或&lt;a id="J_ShowAllRoomList" href="javascript:void(0);"&gt;查看全部房型&lt;/a&gt;！&lt;/p&gt;&lt;/td&gt;
</script>
</div>
<div class="compare_extension hidden" id="J_CompareExtension"></div>
<div class="hotel_compare hidden" id="J_HotelCompare"></div>
    
</div>

<div id="J_meeting_list" class="room_select_box" style="display:none;">
  <div class="date_change_box2 mt_date_change">
    <div class="left">
      <p class="title hidden">您可以尝试修改入住退房日期</p>
      <div class="date_form">
        <div class="date_form_inputs">
          <div class="date_form_label">开始时间
            <input type="text" value="" autocomplete="off" mod_calendar_rangestart="#" mod_calendar_focusnext="true" mod_notice_tip="yyyy-mm-dd" mod="notice|calendar" class="input_txt inputSel" name="meetingCheckIn" id="meetingCheckIn" _cqnotice="yyyy-mm-dd" style="" />
          </div>
          <div class="date_form_line"></div>
          <div class="date_form_label">结束时间
            <input type="text" value="" autocomplete="off" mod_calendar_rangestart="#" mod_calendar_focusnext="true" mod_notice_tip="yyyy-mm-dd" mod="notice|calendar" class="input_txt inputSel" name="meetingCheckOut" id="meetingCheckOut" _cqnotice="yyyy-mm-dd" style="" />
          </div>
        </div>
        <a href="javascript:void(0);" id="meetingChangeBtn" class="btn">重新搜索</a>
      </div>
    </div>
  </div>
  <div id="J_meeting_box" class="">
    <div class="htl_room_table J_roomTable mt_tabel">
      <div class="room_list_loading" style="display:none;">给力加载中，请稍候......</div>
      <table border="0" cellspacing="0" cellpadding="0" summary="">
        <tbody>
        </tbody>
      </table>
      <div class="mt_pic">
        <a href="//meeting.ctrip.com/online/Customization.aspx#ctm_ref=hod_dl_tab_meet_chk2" id="J_MeetingCustomization" target="_self">
          <img src="//pic.c-ctrip.com/scenic_htl/meeting/mt_br.png" alt="" />
          <span>定制会议需求</span></a>
      </div>
    </div>
  </div>
</div>
<div class="mt_pic_info" id="J_meeting_detail" style="position: absolute;z-index:10;display:none;">

</div>
<div class="mt_date_box" id="J_meeting_choose_time" style="z-index:10;display:none;">
  
</div>
<script type="text/template" id="J_meeting_choose_tpl">
   &lt;h2&gt;&lt;span&gt;${Name}&lt;/span&gt; &lt;span class="base_price J_floor_price"&gt;&lt;dfn&gt;¥&lt;/dfn&gt;${MinPrice}&lt;em&gt; 起&lt;/em&gt;&lt;/span&gt;&lt;span class="base_price J_totle_price" style="display:none;"&gt;&lt;/span&gt;&lt;i&gt;&lt;/i&gt;&lt;/h2&gt;
   &lt;div class="mt_date_area"&gt;
     &lt;h3&gt;选择会议时段（可多选）&lt;/h3&gt;
     &lt;ul&gt;
      {{each(i, item) DayPriceList}}
       &lt;li&gt;
         &lt;span class="mt_date_li"&gt;${Date}&lt;/span&gt;
         &lt;span class='J_choose_time ${(InventoryMorning == 0 || MoriningPrice &lt;= 0) ? "gray" : ""}' data-price="${MoriningPrice}" data-clock="1"&gt;上午&lt;/span&gt;
         &lt;span class='J_choose_time ${(InventoryAfternoon == 0 || AfternoonPrice &lt;= 0) ? "gray" : ""}' data-price="${AfternoonPrice}" data-clock="2"&gt;下午&lt;/span&gt;
         &lt;span class='J_choose_time ${(InventoryMorning == 0 || Price &lt;= 0 || InventoryAfternoon == 0) ? "gray" : ""}' data-price="${Price}" data-clock="0"&gt;上下午&lt;/span&gt;
         &lt;span class='J_choose_time ${(InventoryEvening == 0 || EveningPrice &lt;= 0) ? "gray" : ""}' data-price="${EveningPrice}" data-clock="3"&gt;晚上&lt;/span&gt;
       &lt;/li&gt;
       {{/each}}
     &lt;/ul&gt;
     &lt;a class="mt_btn disabled" href="javascript:void(0);" data-booking="${MeetingRoomID}"&gt;立即预订&lt;/a&gt;
   &lt;/div&gt;
</script>
<script type="text/template" id="J_meeting_list_tpl">
&lt;tr&gt;
    &lt;th class="mt_hd wl1"&gt;会议厅名称&lt;/th&gt;
    &lt;th class="wl2"&gt;面积&lt;/th&gt;
    &lt;th class="wl2"&gt;最多容纳&lt;/th&gt;
    &lt;th class="wl2"&gt;剧场式&lt;/th&gt;
    &lt;th class="wl2"&gt;课桌式&lt;/th&gt;
    &lt;th class="wl2"&gt;宴会式&lt;/th&gt;
    &lt;th class="wl3"&gt;&lt;/th&gt;
    &lt;th class="wl4"&gt;&lt;/th&gt;
&lt;/tr&gt;
{{each(i, item) list}}
&lt;tr class="last_room" data-id="${MeetingRoomID}"&gt;
    &lt;td class="mt_hd"&gt;
        &lt;a class="mt_detail" href="javascript:void(0);"&gt;
        &lt;img src="${LogoUrl}" _src="${LogoBigUrl}" onerror="this.src='//pic.c-ctrip.com/hotels110127/hotel_example.jpg';this.onerror=null;"&gt;&lt;/a&gt;
        &lt;a class="meeting_title_box room_unfold" href="javascript:void(0);"&gt;
            &lt;p title="${Name}"&gt;${Name}&lt;/p&gt;
            &lt;span&gt;查看详情&lt;/span&gt;
            {{if HasPanoramaPicture}}
                &lt;i class="i720" data-id="${MeetingRoomID}"&gt;&lt;/i&gt;
            {{/if}}
        &lt;/a&gt;
    &lt;/td&gt;
    &lt;td&gt;${Area}&lt;/td&gt;
    &lt;td&gt;${MaxCapacity}&lt;/td&gt;
    &lt;td&gt;${TheaterCapacity}&lt;/td&gt;
    &lt;td&gt;${SchoolCapacity}&lt;/td&gt;
    &lt;td&gt;${DinnerCapacity}&lt;/td&gt;
    &lt;td&gt;
        &lt;p class="base_box"&gt;
        &lt;span class="base_price"&gt;
            {{if MinPrice &gt; 0}}
                {{if IsReferencePrice}}参考价&lt;br /&gt;{{/if}}
                &lt;dfn&gt;¥&lt;/dfn&gt;${MinPrice}
                &lt;em&gt;起&lt;/em&gt;&lt;/span&gt;
            {{else}}
            当天售完
            {{/if}}
        &lt;/p&gt;
    &lt;/td&gt;
    &lt;td&gt;
        {{if !IsReferencePrice &amp;&amp; MinPrice &gt; 0}}
        &lt;a class="btn_date" href="javascript:void(0);"&gt;选择时段&lt;/a&gt;
        {{/if}}
    &lt;/td&gt;
&lt;/tr&gt;
{{/each}}
</script>
<script type="text/template" id="J_meeting_detail_tpl">
&lt;h2&gt;${Name}&lt;i&gt;&lt;/i&gt;&lt;/h2&gt;
&lt;div class="mt_info"&gt;
    &lt;div class="mt_pic_area"&gt;
        &lt;a class="mt_prev" style="display:none;"&gt;&lt;i class="mt_i"&gt;&lt;/i&gt;&lt;/a&gt;
        {{if PictureList != null &amp;&amp; PictureList.length &gt; 1}}
        &lt;a class="mt_next"&gt;&lt;i class="mt_i"&gt;&lt;/i&gt;&lt;/a&gt;
        {{else}}
        &lt;a class="mt_next" style="display:none;"&gt;&lt;i class="mt_i"&gt;&lt;/i&gt;&lt;/a&gt;
        {{/if}}
        &lt;div style="width:${PictureList.length + "00%"}" class="J_meeting_pic_slide"&gt;
             {{each(i, item) PictureList}}
            &lt;ul&gt;
                &lt;li&gt;
                    &lt;img src="${item.BigUrl}" width="320" height="250" alt="" onerror="this.src='//pic.c-ctrip.com/hotels110127/hotel_example.jpg';this.onerror=null;"&gt;
                &lt;/li&gt;
            &lt;/ul&gt;
            {{/each}}
        &lt;/div&gt;
    &lt;/div&gt;
    &lt;div class="mt_info_l"&gt;
        &lt;span&gt;面积&amp;#58; ${Area}&lt;/span&gt;
        &lt;span&gt;层高&amp;#58; ${Height &gt; 0 ? (Height + "m") : "--"}&lt;/span&gt;
        &lt;span&gt;立柱&amp;#58; ${IsPillar == null ? "--" : (IsPillar ? "有" : "无")}&lt;/span&gt;
        {{if Floor &gt; 0}}&lt;span&gt;楼层&amp;#58; ${Floor}F&lt;/span&gt;{{/if}}
        &lt;span class="bk"&gt;容纳人数范围&amp;#58; ${MinCapacity}~${MaxCapacity}&lt;/span&gt;
        {{each(i, item) LayOutList}}
            {{if MaxCapacity &gt; 0}}
            &lt;span&gt;${LayoutName}&amp;#58; ${MaxCapacity}人&lt;/span&gt;
            {{/if}}
        {{/each}}
    &lt;/div&gt;
&lt;/div&gt;
</script>
<div class="htl_room_table">
    <div class="room_package_title J_OtherBuBaseRoom">更多团购/多间特惠/可选套餐优惠</div>
    <table cellspacing="0" cellpadding="0" border="0" summary="详情页酒店房型列表" class="table_room_package">
    <tbody>
	    <tr class="group_hotel J_GroupRoom hidden"></tr>
        <tr class="rooms_sales J_MeetingRooms"><td class="room_type"><img class="room_type_img" src="//dimg10.c-ctrip.com/images/200o0f0000007ejjwD5E8_R_130_130.jpg" _src="//dimg10.c-ctrip.com/images/200o0f0000007ejjwD5E8_R_300_225.jpg" /><div class="room_type_txt"><div class="room_type_txt_wrap"><p>多间优惠</p><p>长住优惠</p></div></div></td><td colspan="6"><div class="rooms_sales_main"><div class="column1">预订5间以上</div><div class="column2"><span class="sale_orange_txt">省心更省钱！</span><span class="label_onsale_redtxt"><i>立省</i><dfn>¥</dfn>1120</span></div></div><div class="rooms_sales_main"><div class="column1">长住10天以上</div><div class="column2"><span class="sale_orange_txt">省心更省钱！</span><span class="label_onsale_redtxt"><i>立省</i><dfn>¥</dfn>2240</span></div></div></td><td class="col7"><a class="btn_buy" target="_blank" href="http://meeting.ctrip.com/online/place/1063.html?checkin=2018-09-21&amp;checkout=2018-09-22&amp;ref=hoteldetailpage#ctm_ref=htl_detail_meeting_def_b">查看预订</a></td></tr>
	    <tr class="hotel_spot J_ShxDpSpot"><td class="hotel_spot_item1">优惠套餐</td><td colspan="5" class="room_type"><div><span class="icon_tag_hotel">酒店</span><p title="豪华湖景房(限时抢购)">豪华湖景房(限时抢购)</p><span> <strong>1</strong>晚</span></div><div><span class="icon_tag_ticket">门票</span><p title="东方明珠观光E票成人票">东方明珠观光E票成人票</p><span> <strong>2</strong>张</span></div></td><td><p><strong>  套餐价</strong></p><p><span class="base_price"> <dfn>￥</dfn>879</span></p></td><td><a id="SHXDP_buy_button" href="http://taocan.ctrip.com/SH/SSHLoading.aspx?cityId=2&amp;hotelid=428365&amp;hotelName=%e4%b8%8a%e6%b5%b7%e5%b0%8f%e5%8d%97%e5%9b%bd%e8%8a%b1%e5%9b%ad%e9%85%92%e5%ba%97&amp;roomid=69643394&amp;roomNum=1&amp;checkInDate=2018-09-21&amp;checkOutDate=2018-09-22&amp;PayType=PP&amp;HotelChannel=1&amp;ProductIds=1601149&amp;TicketIds=10735216&amp;TicketNames=%e4%b8%9c%e6%96%b9%e6%98%8e%e7%8f%a0%e8%a7%82%e5%85%89E%e7%a5%a8%e6%88%90%e4%ba%ba%e7%a5%a8&amp;UsePersons=1&amp;Quantitys=2&amp;ScenicSpotIds=762&amp;ScenicSpotNames=&amp;ScenicSpotDistances=7.5819&amp;FluxEntrance=50102&amp;DPSource=2&amp;SdpId=-2&amp;IsDiscount=1" onclick="return window.HotelRoom.onSpotHotel(this);" class="btn_buy spotOrderButton">立即预订</a></td></tr>
    </tbody>
    </table>
</div>
<div id="noPriceInfo"></div>
<div id="adviseHotel"></div>

<div class="hotel_info_comment" style="display:block;">
    <div id="AdviceHotelHasPrice2"></div>
</div>


<div id="J_htTips" class="htl_tips hidden"></div>
 
            <div id="ComboInfo"></div>
        
            <div><a rel="nofollow" id="id_detail_arrow" href="javascript:void(0);" style="height:0px;"></a></div>
            <div id="hotel_info_comment">
                <div class="hotel_info_comment detail_content" style="display:block;">
                    
<h2 class="detail_title">酒店介绍</h2>
<div id="htltags" class="htl_tags hidden">
    
</div>
<div class="special_label"><i class="i_label">休闲度假</i><i class="i_label">亲子酒店</i><i class="i_label">浪漫情侣</i><i class="i_label">商务出行</i><i class="i_label">地铁周边</i></div><div class="special_info"><ul><li><span class="t">【休闲度假】</span>酒店独揽60万平方米的都市绿洲黄兴公园，在房内，就可以将公园美景和碧波湖景尽收眼底。</li><li><span class="t">【亲子酒店】</span>宁静悠然的公园美景和碧波湖景尽收眼底，儿童乐园适合小朋友，闹中取静，家人休闲理想之所。</li></ul></div>
<div class="htl_room_txt text_3l" id="htlDes">
<p>
2012年开业  192间房  
<span id="J_realContact" data-real="电话021-25258888  &lt;a target='_blank' href='//my.ctrip.com/uxp/Community/CommunityAdvice.aspx?producttype=3&amp;categoryid=65'&gt;纠错&lt;/a&gt;" style="color:#0066cc;cursor:pointer;">联系方式</span>　　<br />
<span id="ctl00_MainContentPlaceHolder_hotelDetailInfo_lbDesc" itemprop="description">　　上海小南国花园酒店地处杨浦区，步行5分钟即可到达地铁8号线黄兴公园站，坐拥上海浦西市中心不可多得的自然生态环境，为客人提供大隐于市的度假体验。<br />　　<br />　　酒店独揽60万平方米的都市绿洲黄兴公园，百余间宽阔客房均采用落地景观大窗，宁静悠然的公园美景和碧波湖景尽收眼底。<br />　　<br />　　客房内采用世界品牌Frette芙蕾特与Pacific Coast派赛菲特床上用品、Sealy丝涟床垫以及L'Occitane欧舒丹沐浴用品，确保客人获得尊贵舒适的入住体验。<br />　　<br />　　酒店的钻石宴会厅面积达1200平方米，可同时容纳90桌宴席；此外，480平方米的红宝石宴会厅及4个多功能会议厅可满足多种形式的会议宴会。<br />　　<br />　　酒店还拥有在上海市区酒店内的婚礼教堂、5000平方米的非SPA中心和以声光影像科技讲述上海美食历史的非SPA–食光隧道、4家餐厅、酒吧，还有适合孩子玩耍的儿童乐园；是你闹中取静，带着家人度假休闲的理想之所。<br /></span>
</p>
</div>
<div class="introduce_all layoutfix "><a rel="nofollow" id="more" href="javascript:void(0);" class="show_unfold float_right">显示全部</a></div>
<script type="text/javascript" language="javascript">
    var lbDesc = document.getElementById("ctl00_MainContentPlaceHolder_hotelDetailInfo_lbDesc");
    if (lbDesc.offsetHeight &lt; 45) {//小于3行
        document.getElementById("more").style.visibility = "hidden";
    }

</script>


<h2 class="detail_title ">酒店设施</h2>
<div id="J_htl_facilities" class="htl_info_table ">
    <table>
        <tbody>
            <tr data-init="1" class=""><th>网络</th><td><ul class="facility_list"><li title="客房WIFI免费" data-rank="1" class=""><i class="icons-facility32"></i>客房WIFI<span class="green">免费</span><span class="i_sign hidden">*</span></li><li title="客房WIFI" data-rank="1" class=""><i class="icons-facility01"></i>客房WIFI<span class="i_sign hidden">*</span></li><li title="房间内高速上网" data-rank="1" class=""><i class="icons-facility38"></i>房间内高速上网<span class="i_sign hidden">*</span></li><li title="公共区WIFI免费" data-rank="1" class=""><i class="icons-facility32"></i>公共区WIFI<span class="green">免费</span><span class="i_sign hidden">*</span></li></ul></td></tr><tr data-init="1" class=""><th>交通设施</th><td><ul class="facility_list"><li title="免费停车场" data-rank="1" class=""><i class="icons-facility03"></i><span class="green">免费</span>停车场<span class="i_sign hidden">*</span></li></ul></td></tr><tr data-init="1" class=""><th>交通服务</th><td><ul class="facility_list"><li title="接机服务" data-rank="1" class=""><i class="icons-facility28"></i>接机服务<span class="i_sign hidden">*</span></li><li title="租车服务" data-rank="1" class=""><i class="icons-facility38"></i>租车服务<span class="i_sign hidden">*</span></li><li title="叫车服务" data-rank="1" class=""><i class="icons-facility38"></i>叫车服务<span class="i_sign hidden">*</span></li></ul></td></tr><tr data-init="1" class=""><th>儿童设施</th><td><ul class="facility_list"><li title="儿童乐园" data-rank="1" class=""><i class="icons-facility38"></i>儿童乐园<span class="i_sign hidden">*</span></li><li title="儿童俱乐部" data-rank="1" class=""><i class="icons-facility38"></i>儿童俱乐部<span class="i_sign hidden">*</span></li></ul></td></tr><tr data-init="1" class=""><th>休闲娱乐</th><td><ul class="facility_list"><li title="室内游泳池" data-rank="1" class=""><i class="icons-facility15"></i>室内游泳池<span class="i_sign hidden">*</span></li><li title="健身室" data-rank="1" class=""><i class="icons-facility14"></i>健身室<span class="i_sign hidden">*</span></li><li title="SPA" data-rank="1" class=""><i class="icons-facility18"></i>SPA<span class="i_sign hidden">*</span></li><li title="足浴" data-rank="1" class=""><i class="icons-facility38"></i>足浴<span class="i_sign hidden">*</span></li><li title="按摩室" data-rank="1" class=""><i class="icons-facility38"></i>按摩室<span class="i_sign hidden">*</span></li><li title="桑拿浴室" data-rank="1" class=""><i class="icons-facility38"></i>桑拿浴室<span class="i_sign hidden">*</span></li><li title="棋牌室" data-rank="1" class=""><i class="icons-facility38"></i>棋牌室<span class="i_sign hidden">*</span></li><li title="KTV" data-rank="1" class=""><i class="icons-facility38"></i>KTV<span class="i_sign hidden">*</span></li><li title="理发美容中心" data-rank="0" class="hidden"><i class="icons-facility38"></i>理发美容中心<span class="i_sign hidden">*</span></li></ul></td></tr><tr data-init="0" class="hidden"><th>前台服务</th><td><ul class="facility_list"><li title="行李寄存" data-rank="1" class=""><i class="icons-facility10"></i>行李寄存<span class="i_sign hidden">*</span></li><li title="24小时前台" data-rank="1" class=""><i class="icons-facility17"></i>24小时前台<span class="i_sign hidden">*</span></li><li title="24小时大堂经理" data-rank="1" class=""><i class="icons-facility38"></i>24小时大堂经理<span class="i_sign hidden">*</span></li><li title="专职行李员" data-rank="1" class=""><i class="icons-facility38"></i>专职行李员<span class="i_sign hidden">*</span></li><li title="礼宾服务" data-rank="1" class=""><i class="icons-facility38"></i>礼宾服务<span class="i_sign hidden">*</span></li><li title="免费旅游交通图" data-rank="1" class=""><i class="icons-facility06"></i><span class="green">免费</span>旅游交通图<span class="i_sign hidden">*</span></li><li title="叫醒服务" data-rank="1" class=""><i class="icons-facility38"></i>叫醒服务<span class="i_sign hidden">*</span></li><li title="邮政服务" data-rank="1" class=""><i class="icons-facility38"></i>邮政服务<span class="i_sign hidden">*</span></li><li title="前台保险柜" data-rank="0" class="hidden"><i class="icons-facility38"></i>前台保险柜<span class="i_sign hidden">*</span></li><li title="信用卡结算" data-rank="0" class="hidden"><i class="icons-facility38"></i>信用卡结算<span class="i_sign hidden">*</span></li><li title="快速办理入住" data-rank="0" class="hidden"><i class="icons-facility38"></i>快速办理入住<span class="i_sign hidden">*</span></li></ul></td></tr><tr data-init="0" class="hidden"><th>餐饮服务</th><td><ul class="facility_list"><li title="中餐厅" data-rank="1" class=""><i class="icons-facility30"></i>中餐厅<span class="i_sign hidden">*</span></li><li title="西餐厅" data-rank="1" class=""><i class="icons-facility13"></i>西餐厅<span class="i_sign hidden">*</span></li><li title="酒吧" data-rank="1" class=""><i class="icons-facility38"></i>酒吧<span class="i_sign hidden">*</span></li><li title="送餐服务" data-rank="1" class=""><i class="icons-facility38"></i>送餐服务<span class="i_sign hidden">*</span></li></ul></td></tr><tr data-init="0" class="hidden"><th>商务服务</th><td><ul class="facility_list"><li title="会议厅" data-rank="1" class=""><i class="icons-facility38"></i>会议厅<span class="i_sign hidden">*</span></li><li title="商务中心" data-rank="1" class=""><i class="icons-facility38"></i>商务中心<span class="i_sign hidden">*</span></li><li title="多功能厅" data-rank="1" class=""><i class="icons-facility38"></i>多功能厅<span class="i_sign hidden">*</span></li></ul></td></tr><tr data-init="0" class="hidden"><th>通用设施</th><td><ul class="facility_list"><li title="电梯" data-rank="1" class=""><i class="icons-facility38"></i>电梯<span class="i_sign hidden">*</span></li><li title="大堂吧" data-rank="1" class=""><i class="icons-facility38"></i>大堂吧<span class="i_sign hidden">*</span></li><li title="大堂免费报纸" data-rank="1" class=""><i class="icons-facility38"></i>大堂<span class="green">免费</span>报纸<span class="i_sign hidden">*</span></li><li title="无烟楼层" data-rank="1" class=""><i class="icons-facility12"></i>无烟楼层<span class="i_sign hidden">*</span></li><li title="所有场所严禁吸烟" data-rank="1" class=""><i class="icons-facility38"></i>所有场所严禁吸烟<span class="i_sign hidden">*</span></li><li title="自动取款机" data-rank="1" class=""><i class="icons-facility38"></i>自动取款机<span class="i_sign hidden">*</span></li><li title="公用区监控系统" data-rank="1" class=""><i class="icons-facility38"></i>公用区监控系统<span class="i_sign hidden">*</span></li><li title="残疾人客房" data-rank="1" class=""><i class="icons-facility38"></i>残疾人客房<span class="i_sign hidden">*</span></li></ul></td></tr><tr data-init="0" class="hidden"><th>其他服务</th><td><ul class="facility_list"><li title="外币兑换" data-rank="1" class=""><i class="icons-facility38"></i>外币兑换<span class="i_sign hidden">*</span></li><li title="礼品廊" data-rank="1" class=""><i class="icons-facility38"></i>礼品廊<span class="i_sign hidden">*</span></li><li title="鲜花店" data-rank="1" class=""><i class="icons-facility38"></i>鲜花店<span class="i_sign hidden">*</span></li><li title="医务室" data-rank="1" class=""><i class="icons-facility38"></i>医务室<span class="i_sign hidden">*</span></li><li title="婚宴服务" data-rank="1" class=""><i class="icons-facility38"></i>婚宴服务<span class="i_sign hidden">*</span></li><li title="洗衣服务" data-rank="1" class=""><i class="icons-facility39"></i>洗衣服务<span class="i_sign hidden">*</span></li><li title="干洗" data-rank="1" class=""><i class="icons-facility39"></i>干洗<span class="i_sign hidden">*</span></li><li title="熨衣服务" data-rank="1" class=""><i class="icons-facility38"></i>熨衣服务<span class="i_sign hidden">*</span></li></ul></td></tr><tr><td colspan="2"><div class="facility_btn"><a href="javascript:;" class="show_unfold" id="J_show_unfold">全部展开</a></div><div class="facility_btn hidden"><a href="javascript:;" class="show_fold" id="J_show_fold">收起</a></div></td></tr>
        </tbody>
    </table>
</div>


<h2 class="detail_title">酒店政策</h2>

<div class="htl_info_table">
	<table class="detail_extracontent">
		<tbody><tr><th>入住和离店</th><td>入住时间：15:00以后      离店时间：12:00以前</td></tr><tr><th>儿童政策</th><td><ul class="policy_list_new"><li><span class="dot">•</span>酒店允许携带儿童入住</li></ul><ul class="policy_list_new"><li style="white-space:normal;"><span class="dot">•</span>每间客房最多容纳1名儿童，和成人共用现有床铺。</li></ul><table class="childpolicy_new"><tbody><tr><th>1.2米以下</th><td>使用现有床铺<span class="green">免费</span>，<span class="green">含儿童早餐。</span></td></tr><tr><th>1.2米以上</th><td>使用现有床铺<span class="green">免费</span>，不含儿童早餐。</td></tr></tbody></table><ul class="policy_list_new"><li style="white-space:normal;"><span class="dot">•</span>不接受18岁以下客人在无监护人陪同的情况下入住</li></ul></td></tr><tr><th>膳食安排</th><td>自助早餐 RMB 193</td></tr><tr><th>宠物</th><td>不可携带宠物。</td></tr>
        
		<tr>
			<th>可用支付方式</th>
			<td>
				<div class="detail_extracontent layoutfix">
                    <div class="card_cont_img">
                        
					    <span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'$jmp_table','content':{'txt':'&lt;div class=&quot;jmp_bd&quot;&gt;境外发行信用卡 -- 万事达(Master)&lt;/div&gt;'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500}}}" class="card_master"><i></i></span>
<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'$jmp_table','content':{'txt':'&lt;div class=&quot;jmp_bd&quot;&gt;境外发行信用卡 -- 威士(VISA)'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500}}}" class="card_visa"><i></i></span>
<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'$jmp_table','content':{'txt':'&lt;div class=&quot;jmp_bd&quot;&gt;境外发行信用卡 -- 运通(AMEX)'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500}}}" class="card_amex"><i></i></span>
<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'$jmp_table','content':{'txt':'&lt;div class=&quot;jmp_bd&quot;&gt;境外发行信用卡 -- 大来(Diners Club)'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500}}}" class="card_diners"><i></i></span>
<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'$jmp_table','content':{'txt':'&lt;div class=&quot;jmp_bd&quot;&gt;境外发行信用卡 -- JCB'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500}}}" class="card_jcb"><i></i></span>
<span data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'$jmp_table','content':{'txt':'&lt;div class=&quot;jmp_bd&quot;&gt;国内发行银联卡'},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500}}}" class="card_unionpay"><i></i></span>
	
                    </div>  
				</div>
                
			</td>
		</tr>	
        						
	</tbody></table>
</div>
<h2 class="detail_title">周边设施</h2>
<div class="htl_info_table">

    <table>
	    <tbody>
		    <tr class="">
			    <th>餐饮</th>
			    <td><ul class="detail_extracontent"><li>小南国花园酒店ADD西餐厅</li><li>红宝石宴会厅</li><li>小南国花园酒店AdD餐厅</li><li>小南国花园酒店·婚宴</li><li>小南国花园酒店</li></ul></td>
		    </tr>
		    <tr class="">
			    <th>购物</th>
			    <td><ul class="detail_extracontent"><li>联华(佳龙店)</li><li>杨浦商贸延吉商业中心</li><li>乐语通讯(靖宇东路店)</li><li>联华(洋洋店)</li><li>如海购物中心(安图店)</li></ul></td>
		    </tr>
		    <tr class="hidden">
			    <th class="border_none">娱乐</th>
			    <td class="border_none"><ul class="detail_extracontent"></ul></td>
		    </tr>
		    <tr class="">
			    <th>地铁站</th>
			    <td><ul class="detail_extracontent"><li>黄兴公园</li><li>延吉中路</li><li>黄兴公园站</li><li>延吉中路站</li><li>翔殷路站</li></ul></td>
		    </tr>
		    <tr class="">
			    <th>景点</th>
			    <td><ul class="detail_extracontent"><li>国际会议中心</li><li>杨浦公园</li></ul></td>
		    </tr>
	    </tbody>
    </table>

</div>
<div><a rel="nofollow" id="id_comment_arrow" href="javascript:void(0);" style="height:0px;"></a></div>
<h2 class="detail_title">住客点评</h2>
<div id="comment_loading" class="comment_loading" style="display:none;"><i></i>点评载入中</div>
<div id="commentList" class="hotel_info_comment" style="display:block" ;"=""><div class="detail_cmt_box"><div class="comment_tab_main"><div id="divCtripComment" class="comment_tab_list"><div class="comment_sumary_box"><p class="real_man">点评均来自真实入住客人！</p><div class="comment_total_score"><span class="big_c"><span class="b" style="width:130px;"></span></span><span class="hotel_level">很好</span><span class="score"><span class="n">4.7</span> / 5分</span><span class="rec"><span class="n">97%</span>用户推荐</span></div><div class="bar_score"><p>位置<span class="score">4.7</span></p><p>设施<span class="score">4.7</span></p><p>服务<span class="score">4.6</span></p><p>卫生<span class="score">4.7</span></p></div><div class="bar_search_box" id="J_bar_search_box"><div class="bar_search"><input class="bar_search_btn" type="button" value="搜索" id="J_searchResultBtn" /><input type="text" placeholder="搜索点评关键字" class="bar_search_input inputSel" autocomplete="off" autocorrect="off" autocapitalize="off" value="" id="J_searchInput" maxlength="20" /></div><div class="bar_search_result hidden" id="J_searchResultTag">搜索“<span class="highlight"></span>”的结果<p class="del" id="J_searchResultDel">×</p></div></div></div><div class="comment_box_bar_new clearfix"><div class="bar_left"><a href="/hotel/dianping/428365.html" class="tab_current" name="needTraceCode"><span id="All_Comment">全部(6518)</span></a><a href="/hotel/dianping/428365_p1t2.html" class="" name="needTraceCode"><span id="No_Recoment" commentparam="&amp;commentType=2">差评(167)</span></a><a href="/hotel/dianping/428365.html" class="" name="needTraceCode"><span id="HasImage" commentparam="&amp;commentType=3">有图片(701)</span></a></div><div class="bar_right"><select data-type="orderby" class="select_sort" style="width:120px;"><option value="2" selected="">热门排序</option><option value="1">入住时间排序</option></select><select data-type="userType" class="select_ctrip" style="width: 120px;"><option value="-1" selected="">全部出游类型</option><option value="10">商务出差(2450)</option><option value="40">朋友出游(523)</option><option value="70">情侣出游(779)</option><option value="30">家庭亲子(1594)</option><option value="50">独自出行(291)</option><option value="60">代人预订(351)</option><option value="0">其他(530)</option></select><select name="roomname" class="select_room" style="width:120px;"><option value="" selected="">全部房型</option><option value="亲子家庭房">亲子家庭房(226)</option><option value="至尊湖景房">至尊湖景房(342)</option><option value="总统套房">总统套房(1)</option><option value="豪华湖景房">豪华湖景房(5554)</option><option value="亲子家庭套房">亲子家庭套房(34)</option><option value="行政全湖景套房">行政全湖景套房(77)</option></select></div></div><div class="comment_detail_list"><div class="comment_block J_asyncCmt" data-cid="237608153" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="1" data-img-count="9" data-arrivcitycount="0" data-comhotcount="0" data-userfulcount="0" data-isuserself="False"><img src="//pic.c-ctrip.com/common/pic_default_avatar.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>1***0</span></p><p class="level_new"></p><p class="num">点评总数 1<br />上传图片 9</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:5.0"><span class="b" style="width:80px;"></span></span><span class="score"><span class="n">5.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760880" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_family"></i>家庭亲子</span></p><div class="comment_txt"><div class="J_commentDetail">带孩子到新华医院看病，住在这里是最好的选择，离新华只有三站地铁。干净卫生房间够大，酒店用品是欧舒丹的。
订的是湖景房，视野很好，我在携程订的时候没有选择大床还是双床，到了前台说要双床，但是只有大床了，前台的小姑娘很热情的给升级了房间。
26楼的西餐口味尚可，只是不明白为什么要消费者承担税费？
小南国中餐厅点了它的名菜，花雕蒸鲥鱼，388元，以为会很鲜美，但是略失望，不是新鲜的鱼，是腌制过的，肉已不鲜嫩，有点柴，再加上花雕酒，真的好咸，如果这个菜作为小南国名菜，绝对需要改进。
糖醋小排孩子很爱吃。
酒店其他都不错，下次来还住这里。
还有，洗手间地漏确实像很多人评价的那样，有异味，需改进。</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230v0v000000jz2m7BBE8_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230v0v000000jz2m7BBE8_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230k0v000000js7e3BFC7_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230k0v000000js7e3BFC7_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230u0v000000jnzw86ED6_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230u0v000000jnzw86ED6_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/23020v000000jv3sh4925_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/23020v000000jv3sh4925_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230l0v000000jo6ttA884_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230l0v000000jo6ttA884_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/23050v000000jqj4sA6F7_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/23050v000000jqj4sA6F7_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/23080v000000jo7wm75A0_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/23080v000000jo7wm75A0_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230p0v000000jn5nhA4BB_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230p0v000000jn5nhA4BB_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/23090v000000jqff45772_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/23090v000000jqff45772_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-11</span></p><a class="useful useful_voted" data-voted="6" data-cid="237608153" href="javascript:void(0);">有用<span class="n">(6)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="236148692" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="1" data-img-count="9" data-arrivcitycount="3" data-comhotcount="1" data-userfulcount="8" data-isuserself="False"><img src="//pic.c-ctrip.com/common/pic_default_avatar.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>l***1</span></p><p class="level_new"></p><p class="num">点评总数 1<br />被点有用 8<br />上传图片 9</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:4.0"><span class="b" style="width:74px;"></span></span><span class="score"><span class="n">4.8</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="38424158" data-baseroomname="亲子家庭房">亲子家庭房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_family"></i>家庭亲子</span></p><div class="comment_txt"><div class="J_commentDetail">去魔都亲子酒店真的小南国是首选。周围环境好，而且设施完善，很能省心。我们是当天下午两天到达的，那天房间满房，我们运气好，被升级到了亲子套房，多等待的一个小时打扫时间也很值得。房间超级大，落地窗外就是湖景。酒店的亲子活动又很多，以致于我们也没时间去下面的黄兴公园了。送的早晚餐很丰富！餐厅里都是带着孩子的父母。服务员态度也好，因为房间只有一个2米床，三个人怕挤，所以我们要求加床加被子也很快送过来了。房间里的配套设施处处显示着人性化，特别是宝宝这一块。小浴袍，小拖鞋，而且拖鞋超级软哦。宝宝离开酒店时还说，下次我还要住这里。我想这就是最好的评价了。</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/23060v000000jlgg071BF_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/23060v000000jlgg071BF_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/23010v000000jxrcsF20B_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/23010v000000jxrcsF20B_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/23010v000000jxrct4268_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/23010v000000jxrct4268_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230b0v000000jn81s6852_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230b0v000000jn81s6852_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/23060v000000jlgg5A124_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/23060v000000jlgg5A124_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/23080v000000jl12wD55F_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/23080v000000jl12wD55F_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230g0v000000jlixv1FE7_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230g0v000000jlixv1FE7_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/23090v000000jn8lcDC27_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/23090v000000jn8lcDC27_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230b0v000000jn81u0914_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230b0v000000jn81u0914_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-06</span></p><a class="useful useful_voted" data-voted="8" data-cid="236148692" href="javascript:void(0);">有用<span class="n">(8)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="241154986" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="7" data-img-count="39" data-arrivcitycount="23" data-comhotcount="6" data-userfulcount="6" data-isuserself="False"><img src="//images4.c-ctrip.com/target/t1/headphoto/645/991/736/25b26b6d859a4078a715208186608e3a_R_100_100.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>1***1</span></p><p class="level_daren"></p><p class="num">点评总数 7<br />被点有用 6<br />上传图片 39</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:5.0"><span class="b" style="width:80px;"></span></span><span class="score"><span class="n">5.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760880" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_biz"></i>商务出差</span></p><div class="comment_txt"><div class="J_commentDetail">很舒适的房间，景观一流，楼下就是漂亮的黄兴公园，没有时间享用早餐，中餐全日制餐厅的味道和品种都挺好的，不过最好先预定，用餐的人蛮多。个人觉得离地铁黄兴公园站挺近，不穿恨天高10分钟以内能到，公交站就在地铁站门口，交通很方便啦！在酒店外的十字路口有星巴克和超市，晚上买了些水果挺新鲜。总体感觉非常好，下次若还在附近出差会继续选择小南国花园酒店。👍🏻👍🏻</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230a0v000000jzcaq4CCC_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230a0v000000jzcaq4CCC_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230u0v000000jxzqw8D00_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230u0v000000jxzqw8D00_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230n0v000000jx2wkCCC4_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230n0v000000jx2wkCCC4_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230b0v000000k0eqb4A0D_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230b0v000000k0eqb4A0D_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/23040v000000jx045E9D2_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/23040v000000jx045E9D2_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230o0v000000jwv1bAB67_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230o0v000000jwv1bAB67_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230e0v000000k0rqlD45F_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230e0v000000k0rqlD45F_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230q0v000000jzb5vDA28_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230q0v000000jzb5vDA28_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-23</span></p><a class="useful useful_voted" data-voted="3" data-cid="241154986" href="javascript:void(0);">有用<span class="n">(3)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="238473562" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="3" data-img-count="8" data-arrivcitycount="0" data-comhotcount="0" data-userfulcount="0" data-isuserself="False"><img src="//pic.c-ctrip.com/common/pic_default_avatar.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>1***8</span></p><p class="level_new"></p><p class="num">点评总数 3<br />上传图片 8</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:1.0,设施:1.0,服务:1.0,卫生:1.0"><span class="b" style="width:16px;"></span></span><span class="score"><span class="n">1.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760890" data-baseroomname="至尊湖景房">至尊湖景房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_family"></i>家庭亲子</span></p><div class="comment_txt"><div class="J_commentDetail">首先我从来不写评价，但我为了不让接下去的人特别带着小孩去的人受到和我一样的伤害，我在百忙之中，决定把入住的遭遇和大家分享一下。希望别的小孩不要在遭遇这样的不幸。13号晚上小孩吵着要去游泳，我带着他来到所谓五星级酒店应该标配的游泳池，首先到游泳池看到的是，没有任何的安全提醒，大门是敞开的，一大堆大妈大爷穿着自己的鞋子就站在游戏旁看自己的小孩学游泳（里面是酒店承包出去的，有些私教在上课），卫生很不到位，没有任何的私密性，和外面公开的低价游泳池一样，只想用脏乱臭开形容，看到这一幕本来就打算放弃不游了。可是因为他们安全措施不到位，防滑做得不够，没有防滑垫的位置都是水，又是瓷砖，我小孩就这样赤裸裸的摔倒在地板，半张脸直接磕到椅子上，脸肿得很大，乌青了一片，还划了一道，当场大哭起来。可是就在我无助的时候，在场的工作人员很冷血，连一个人过来问下下我需不需要帮助都没有。直到我在那边安慰小孩将近10分钟也没有一个人过来关心问一下。当场我真的怀疑自己是住在五星级酒店还是住在无证廉价公寓里。这就是我花了一千多块得到的服务，零服务，负服务。我真不懂携程怎么会允许这样的酒店滥竽充当进去。真是吐血，一路五星酒店住过来，得到的都是最优质的服务。游泳池都是住客单独使用的，毛巾，饮料，无微不至的工作人。而小南国花园酒店呢？提供了什么样的五星服务，简直就是公共浴场都不如的服务。而且工作人员一个个表情呆板，臭着一张脸。领班经理更是不负责任，遇事推给承包泳池的老板，连站出来处理事情的勇气都没有。这样的人还配当领班经理。我后面拐回去拍照的时候，听到承包老板笑嘻嘻在那边交待，明天要把安全提示拍放在大门，大门就开一条缝。事后诸葛亮，不知道还要害多少人在那边摔倒。再来说说他们是怎么处理事情的：刚开始酒店可能觉得不是多大的事，也许他们认为和他们没关系，他们承包出去。就叫承包的老板忽悠来房间说了几声对不起，想这样了事。我认为消费的是酒店，需要酒店给我一个说法。当日领班经理才不得不站出来处理事情。不得不佩服这个领班经理遇事不是第一时间出来处理。而是推卸责任，也就是不能扛事。第二次带着承包老板带了点小东西想来了事。我跟他们说这不是我的目的，我的目的就是你们既然是五星级酒店，你们就应该让住客得到五星级待遇。我也不希望你们为了盈利而不顾住客的安全，特别是小孩子的安全。我回绝了。接下来就没有任何消息了。我把我的经历一五一十的没有任何谎言的阐述出来。希望能帮助到大家。大家也可以去看评价，差评很多，我所遇到的事不止一个人遇到。早上去吃早餐的时候，也是很失望，地板粘粘的，也不像五星酒店该有的，地板亮的可以照人。餐厅当天经理也是一副高高在上，面无表情。晚上的遭遇已经心情糟糕，一早看到这样的面无表情真的是快疯了。如果一早能得到一个微笑或许昨晚的遭遇我都会忘记了。就是因为这样的一而再，让我下定决心写这些点评分享大家。我就纳闷了，这家酒店的经理是不是都是老板亲戚还是有很大的特权，都是一副他是上帝的样子。怎么这样的标准也能评到五星。我真的想不明白。配套设施真的一点都不达标，人员素质和服务也不达标。卫生马马虎虎。懒得写了，本来就最不爱写东西的人。祝大家好运。晚安</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230g0v000000jqd3z896F_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230g0v000000jqd3z896F_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/23090v000000js2r6947B_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/23090v000000js2r6947B_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/23010v000000k2liv7A16_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/23010v000000k2liv7A16_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230i0v000000johp99A37_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230i0v000000johp99A37_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230a0v000000jqzs27FCA_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230a0v000000jqzs27FCA_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/23020v000000jwr4s5004_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/23020v000000jwr4s5004_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230j0v000000jp6qm9482_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230j0v000000jp6qm9482_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230b0v000000js27qCF2C_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230b0v000000js27qCF2C_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-14</span></p><a class="useful useful_voted" data-voted="39" data-cid="238473562" href="javascript:void(0);">有用<span class="n">(39)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="242911466" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="17" data-img-count="20" data-arrivcitycount="0" data-comhotcount="0" data-userfulcount="0" data-isuserself="False"><img src="//images4.c-ctrip.com/target/t1/headphoto/136/299/437/649eb217e3e54746b7a53b8665e14b00_R_100_100.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>拖***噢</span></p><p class="level_daren"></p><p class="num">点评总数 17<br />上传图片 20</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:5.0"><span class="b" style="width:80px;"></span></span><span class="score"><span class="n">5.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760880" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_biz"></i>商务出差</span></p><div class="comment_txt"><div class="J_commentDetail">位置很好，湖景房很棒～
早上可以绕湖晨跑

房间整洁

自己洗了五件衣服，没有地方晾晒，酒店帮忙免费烘干～</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230k0v000000k703b7843_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230k0v000000k703b7843_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230u0v000000k2slh6F97_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230u0v000000k2slh6F97_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/23010v000000kfqvt4261_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/23010v000000kfqvt4261_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230p0v000000k1ycvB51C_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230p0v000000k1ycvB51C_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/23030v000000k4jtz7987_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/23030v000000k4jtz7987_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230b0v000000k57kt0485_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230b0v000000k57kt0485_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/23010v000000kfqvy9404_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/23010v000000kfqvy9404_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/23090v000000k584m9074_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/23090v000000k584m9074_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-30</span></p><a class="useful useful_voted" data-voted="1" data-cid="242911466" href="javascript:void(0);">有用<span class="n">(1)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="245373176" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="8" data-img-count="20" data-arrivcitycount="4" data-comhotcount="7" data-userfulcount="12" data-isuserself="False"><img src="//images4.c-ctrip.com/target/t1/headphoto/685/724/771/3cd584c18f744104b47d3f3d075d10e3_R_100_100.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>M***3</span></p><p class="level_daren"></p><p class="num">点评总数 8<br />被点有用 12<br />上传图片 20</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:5.0"><span class="b" style="width:80px;"></span></span><span class="score"><span class="n">5.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760880" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年09月入住</span><span class="type"><i class="k_friend"></i>朋友出游</span></p><div class="comment_txt"><div class="J_commentDetail">一周两次入住，说实话，是近几年在上海住过最舒适的酒店。房间干净整洁、四周环境安静怡人，大堂办理入住和退房也很迅速，推荐给各位携友。</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230s0w000000ki26a0A3D_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230s0w000000ki26a0A3D_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230j0w000000kap2g2CAE_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230j0w000000kap2g2CAE_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230q0w000000kcgz2F8CB_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230q0w000000kcgz2F8CB_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230w0w000000kh7shBD8C_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230w0w000000kh7shBD8C_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-09-11</span></p><a class="useful" data-voted="0" data-cid="245373176" href="javascript:void(0);">有用<span class="n">(0)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="244376471" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="36" data-img-count="18" data-arrivcitycount="0" data-comhotcount="0" data-userfulcount="0" data-isuserself="False"><img src="//images4.c-ctrip.com/target/Z80j0v000000jmncmD055_R_100_100.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>s***顺</span></p><p class="level_master"></p><p class="num">点评总数 36<br />上传图片 18</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:2.0,卫生:5.0"><span class="b" style="width:68px;"></span></span><span class="score"><span class="n">4.3</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760880" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年09月入住</span><span class="type"><i class="k_biz"></i>商务出差</span></p><div class="comment_txt"><div class="J_commentDetail">外部环境在上海这样的地方比较难得，设施齐全，只是不满意的是房间服务，叫了房食，吃完还打电话叫他们回收碗筷，到退房还是没有人来，差评！</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230j0w000000k70t8F9C5_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230j0w000000k70t8F9C5_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230f0w000000k7j1936B3_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230f0w000000k7j1936B3_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230d0w000000k6110BC37_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230d0w000000k6110BC37_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230k0w000000kbotb1C32_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230k0w000000kbotb1C32_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-09-06</span></p><a class="useful useful_voted" data-voted="2" data-cid="244376471" href="javascript:void(0);">有用<span class="n">(2)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="243890324" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="30" data-img-count="23" data-arrivcitycount="16" data-comhotcount="27" data-userfulcount="2" data-isuserself="False"><img src="//images4.c-ctrip.com/target/Z8070w000000kv2fe46A5_R_100_100.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>毛***侬</span></p><p class="level_master"></p><p class="num">点评总数 30<br />被点有用 2<br />上传图片 23</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:4.0,卫生:5.0"><span class="b" style="width:74px;"></span></span><span class="score"><span class="n">4.8</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="512945" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_single"></i>独自旅行</span></p><div class="comment_txt"><div class="J_commentDetail">体验不错的一次发呆之旅，紧靠黄兴公园。酒店唯一就是每天只供应四瓶水。多余按照五元一瓶收费。晚上在酒店吃的自助餐，相交于其他五星级酒店品种不算多，但是也不少。毕竟价格摆在这里的。菜品算是精致，特别是凉菜都很爽口。</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230i0w000000k4c929312_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230i0w000000k4c929312_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230s0w000000kcee7561D_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230s0w000000kcee7561D_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230q0w000000k6t6zFA59_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230q0w000000k6t6zFA59_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230k0w000000k9pa58EB0_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230k0w000000k9pa58EB0_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-09-03</span></p><a class="useful" data-voted="0" data-cid="243890324" href="javascript:void(0);">有用<span class="n">(0)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="237987019" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="2" data-img-count="5" data-arrivcitycount="12" data-comhotcount="2" data-userfulcount="1" data-isuserself="False"><img src="//pic.c-ctrip.com/common/pic_default_avatar.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>k***j</span></p><p class="level_new"></p><p class="num">点评总数 2<br />被点有用 1<br />上传图片 5</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:4.0,设施:4.0,服务:4.0,卫生:4.0"><span class="b" style="width:64px;"></span></span><span class="score"><span class="n">4.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="38424158" data-baseroomname="亲子家庭房">亲子家庭房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_family"></i>家庭亲子</span></p><div class="comment_txt"><div class="J_commentDetail">看到闺蜜带她小朋友来 感觉还不错 就带着宝贝也来了 可能是因为周末的关系 原本订的亲子房间说是升级到了行政套房 少了挺多小朋友的东西 和介绍上有点不一样 不过服务之类的还是令人满意的 下次打算带着父母也来体验一下</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230e0v000000jrcyiD634_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230e0v000000jrcyiD634_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230g0v000000jpauj4FAA_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230g0v000000jpauj4FAA_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230t0v000000jonp9D7AC_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230t0v000000jonp9D7AC_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230j0v000000jo4h76F8D_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230j0v000000jo4h76F8D_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230i0v000000jnffuD644_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230i0v000000jnffuD644_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-12</span></p><a class="useful useful_voted" data-voted="1" data-cid="237987019" href="javascript:void(0);">有用<span class="n">(1)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="236962335" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="79" data-img-count="137" data-arrivcitycount="45" data-comhotcount="65" data-userfulcount="34" data-isuserself="False"><img src="//images4.c-ctrip.com/target/fd/headphoto/g3/M00/BB/B6/CggYGVZNVqaAfi5gAAEo4v3erdE970_R_100_100.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>l***5</span></p><p class="level_master"></p><p class="num">点评总数 79<br />被点有用 34<br />上传图片 137</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:5.0"><span class="b" style="width:80px;"></span></span><span class="score"><span class="n">5.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760880" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_biz"></i>商务出差</span></p><div class="comment_txt"><div class="J_commentDetail">非常好。黄兴公园旁边。绿树成荫。午夜抵达酒店，升级了套房，23楼，住的非常非常舒适，床品、卫生，都很到位。早餐丰富，出行方便。</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230j0v000000jmat63AAE_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230j0v000000jmat63AAE_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230e0v000000jpjamC7D1_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230e0v000000jpjamC7D1_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230d0v000000jlb0u0F74_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230d0v000000jlb0u0F74_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230w0v000000jstjd9657_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230w0v000000jstjd9657_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230k0v000000jqytfF33B_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230k0v000000jqytfF33B_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230h0v000000jocw747B4_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230h0v000000jocw747B4_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/23070v000000k3gxtB936_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/23070v000000k3gxtB936_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-09</span></p><a class="useful useful_voted" data-voted="6" data-cid="236962335" href="javascript:void(0);">有用<span class="n">(6)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="240729639" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="4" data-img-count="12" data-arrivcitycount="0" data-comhotcount="0" data-userfulcount="0" data-isuserself="False"><img src="//images4.c-ctrip.com/target/t1/headphoto/062/938/215/f5f05c77006946428867e3c0dae6f4eb_R_100_100.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>_***8</span></p><p class="level_new"></p><p class="num">点评总数 4<br />上传图片 12</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:5.0"><span class="b" style="width:80px;"></span></span><span class="score"><span class="n">5.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760880" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_family"></i>家庭亲子</span></p><div class="comment_txt"><div class="J_commentDetail">酒店超级棒！环境很好，我房间可以看到黄兴公园的景色，超级好看！！！洗漱用品也很棒是欧舒丹，隔音效果很好，只是外卖要到保安亭去取，不可以送近来，这样更安全啦~我很喜欢这个酒店！！！有机会一定回访！</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230h0v000000jyjrn5495_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230h0v000000jyjrn5495_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230j0v000000jwhp9ECC6_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230j0v000000jwhp9ECC6_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/23080v000000jx67oDB27_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/23080v000000jx67oDB27_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230l0v000000jx54wDC00_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230l0v000000jx54wDC00_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-21</span></p><a class="useful useful_voted" data-voted="2" data-cid="240729639" href="javascript:void(0);">有用<span class="n">(2)</span></a></div></div><div class="additional_reply"><p class="title">当天追加：</p><p class="text">啦啦啦啦啦~</p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230h0v000000jyjrn5495_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230h0v000000jyjrn5495_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230l0v000000jx54wDC00_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230l0v000000jx54wDC00_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230j0v000000jwhp9ECC6_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230j0v000000jwhp9ECC6_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/23080v000000jx67oDB27_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/23080v000000jx67oDB27_W_550_412.jpg" ispass="T" /></div></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="240527656" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="32" data-img-count="17" data-arrivcitycount="10" data-comhotcount="16" data-userfulcount="1" data-isuserself="False"><img src="//images4.c-ctrip.com/target/Z80a090000003qdm3D739_R_100_100.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>萧***瑟</span></p><p class="level_master"></p><p class="num">点评总数 32<br />被点有用 1<br />上传图片 17</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:5.0"><span class="b" style="width:80px;"></span></span><span class="score"><span class="n">5.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760880" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_biz"></i>商务出差</span></p><div class="comment_txt"><div class="J_commentDetail">酒店还是不错，环境十分幽雅，打开窗帘黄兴公园的景色一览无余…闲暇的时候还可以去公园里面走走，交通也还算便利，8号线地铁10分钟就走到了</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230c0v000000jz0a80356_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230c0v000000jz0a80356_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230n0v000000jvf8j2118_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230n0v000000jvf8j2118_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230o0v000000jv7da7E02_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230o0v000000jv7da7E02_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230i0v000000jv6js11C4_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230i0v000000jv6js11C4_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-21</span></p><a class="useful useful_voted" data-voted="1" data-cid="240527656" href="javascript:void(0);">有用<span class="n">(1)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="240074664" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="17" data-img-count="25" data-arrivcitycount="0" data-comhotcount="0" data-userfulcount="0" data-isuserself="False"><img src="//images4.c-ctrip.com/target/Z80i0l000000d4h2i317E_R_100_100.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>哈***公</span></p><p class="level_daren"></p><p class="num">点评总数 17<br />上传图片 25</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:5.0"><span class="b" style="width:80px;"></span></span><span class="score"><span class="n">5.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="38424158" data-baseroomname="亲子家庭房">亲子家庭房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_family"></i>家庭亲子</span></p><div class="comment_txt"><div class="J_commentDetail">非常棒的亲子酒店，房间很大，可以俯瞰黄兴公园，还能看到远处的东方明珠。为小孩准备了很多的活动，宝宝玩得很开心。停车场有些拥挤，找停车位挺困难，这也说明酒店生意实在太好。非常值得推荐。</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/23060v000000jvmf39D38_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/23060v000000jvmf39D38_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230b0v000000jxe0t8A07_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230b0v000000jxe0t8A07_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230d0v000000jtir3B5F9_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230d0v000000jtir3B5F9_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/23090v000000jxekf382B_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/23090v000000jxekf382B_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-19</span></p><a class="useful useful_voted" data-voted="1" data-cid="240074664" href="javascript:void(0);">有用<span class="n">(1)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="246579076" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="4" data-img-count="0" data-arrivcitycount="0" data-comhotcount="0" data-userfulcount="0" data-isuserself="False"><img src="//pic.c-ctrip.com/common/pic_default_avatar.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>1***9</span></p><p class="level_new"></p><p class="num">点评总数 4</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:4.0,服务:4.0,卫生:5.0"><span class="b" style="width:71px;"></span></span><span class="score"><span class="n">4.5</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="35368170" data-baseroomname="亲子家庭房">亲子家庭房</a><span class="date">2018年09月入住</span><span class="type"><i class="k_family"></i>家庭亲子</span></p><div class="comment_txt"><div class="J_commentDetail">带孩子来新华医院看医生，酒店离医院还是挺近的，开车十几分钟，房间非常好，窗外景色很美，配的宝宝洗澡盆很贴心，亲子房还送晚餐，划算</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg11.c-ctrip.com/images/230m0w000000kndanAF4C_R_150_150.jpg" data-bigimgsrc="//dimg11.c-ctrip.com/images/230m0w000000kndanAF4C_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/23060w000000kelv5739C_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/23060w000000kelv5739C_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg12.c-ctrip.com/images/230p0w000000kd48j2515_R_150_150.jpg" data-bigimgsrc="//dimg12.c-ctrip.com/images/230p0w000000kd48j2515_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-09-16</span></p><a class="useful" data-voted="0" data-cid="246579076" href="javascript:void(0);">有用<span class="n">(0)</span></a></div></div></div></div><div class="comment_block J_asyncCmt" data-cid="243035152" data-islooking=""><div class="user_info  J_ctrip_pop" style="position:relative;"><p class="head"><span class="img" data-commentcount="20" data-img-count="6" data-arrivcitycount="0" data-comhotcount="0" data-userfulcount="0" data-isuserself="False"><img src="//pic.c-ctrip.com/common/pic_default_avatar.jpg" onerror="this.onerror=''; this.src='//pic.c-ctrip.com/common/pic_default_avatar.jpg'" style="width:33px; height:33px;" /></span></p><p class="name"><span>_***2</span></p><p class="level_daren"></p><p class="num">点评总数 20<br />上传图片 6</p></div><div class="comment_main"><p class="comment_title"><span class="small_c" data-value="位置:5.0,设施:5.0,服务:5.0,卫生:5.0"><span class="b" style="width:80px;"></span></span><span class="score"><span class="n">5.0</span>分</span><a class="room J_baseroom_link room_link" data-baseroomid="4760880" data-baseroomname="豪华湖景房">豪华湖景房</a><span class="date">2018年08月入住</span><span class="type"><i class="k_biz"></i>商务出差</span></p><div class="comment_txt"><div class="J_commentDetail">超级好的一次体验，原本计划7点能到酒店入住，但是各种忙，弄到晚上进10点才到酒店。预定高层大床都没了，酒店给免费升级套房，，，一个人，有点太大了……。套房还送迎宾果盘。。很意外。值得推荐的酒店。晚上窗外一片寂静，第二一早，看到这样的景色，心情舒畅吖</div><p class="comment_txt_more J_commentShowMore hidden"><a href="javascript:;" class="show_unfold">查看更多<i></i></a></p><p class="comment_txt_more J_commentShowLess hidden"><a href="javascript:;" class="show_fold">收起<i></i></a></p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230k0v000000k7dl4C202_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230k0v000000k7dl4C202_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230q0v000000k4hhzB615_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230q0v000000k4hhzB615_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230d0v000000k1psuA6D4_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230d0v000000k1psuA6D4_W_550_412.jpg" ispass="T" /></div></div><div class="comment_bar"><p class="comment_bar_info"><i class="phone"></i><span class="time">发表于2018-08-30</span></p><a class="useful" data-voted="0" data-cid="243035152" href="javascript:void(0);">有用<span class="n">(0)</span></a></div></div><div class="additional_reply"><p class="title">当天追加：</p><p class="text">风景如画，❤️情哈好</p><div class="comment_pic"><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230k0v000000k7dl4C202_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230k0v000000k7dl4C202_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg10.c-ctrip.com/images/230d0v000000k1psuA6D4_R_150_150.jpg" data-bigimgsrc="//dimg10.c-ctrip.com/images/230d0v000000k1psuA6D4_W_550_412.jpg" ispass="T" /></div><div class="pic"><img onerror="errorComImg(this)" class="p listimg" src="//dimg13.c-ctrip.com/images/230q0v000000k4hhzB615_R_150_150.jpg" data-bigimgsrc="//dimg13.c-ctrip.com/images/230q0v000000k4hhzB615_W_550_412.jpg" ispass="T" /></div></div></div></div></div></div><div class="c_page_box"><div class="c_page"><a href="javascript:;" class="c_up_nocurrent"></a><div class="c_page_list layoutfix"><a href="javascript:;" class="current"><span>1</span></a><a value="2" href="/hotel/dianping/428365_p2t0.html"><span>2</span></a><a value="3" href="/hotel/dianping/428365_p3t0.html"><span>3</span></a><a value="4" href="/hotel/dianping/428365_p4t0.html"><span>4</span></a><a value="5" href="/hotel/dianping/428365_p5t0.html"><span>5</span></a><a value="6" href="/hotel/dianping/428365_p6t0.html"><span>6</span></a><span class="c_page_ellipsis">...</span><a value="435" href="/hotel/dianping/428365_p435t0.html"><span>435</span></a></div><a value="2" class="c_down" href="/hotel/dianping/428365_p2t0.html"><span>下一页</span></a><div class="c_pagevalue">到<input type="text" class="c_page_num" name="cPageNum" id="cPageNum" value="1" />页<input type="button" class="c_page_submit" value="确定" name="cPageBtn" id="cPageBtn" /></div><input type="hidden" id="cTotalPageNum" value="435" /></div></div></div></div></div><div id="commentTracker" style="display:none">Version=1.0&amp;PageID=102003&amp;Rank=237608153,236148692,241154986,238473562,242911466,245373176,244376471,243890324,237987019,236962335,240729639,240527656,240074664,246579076,243035152&amp;IdentityTextFilter=-1&amp;OrderBy=2&amp;RecommentType=All</div><div id="commentTracker20150415" style="display:none">{"hotelid":"428365","commentselect":"1","ordertype":"1","outcategory":"全部","roomtype":"","chooseorsearch":"2","keyword":"","result":"2","others":""}</div></div>
<div class="score_pop" style="display:none;" id="score_pop">
    <span class="score_item" id="score_pos"></span>
    <span class="score_item" id="score_set"></span>
    <span class="score_item" id="score_srv"></span>
    <span class="score_item" id="score_cln"></span>
</div>
<div class="comment_pic_pop" id="pic_big" style="display:none;">
    <div class="pic"><img class="p" src="//pic.c-ctrip.com/common/pic_alpha.gif" alt="" /></div>
    <p class="pic_txt"></p>
</div>
                    <div id="AdviceHotelHasPrice" style="display: block;">
                        

                    </div>
                </div>
            </div>
        

        </div>

        <div class="detail_side">
            
	<div class="htl_com J_htl_com " itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating">
        <div class="htl_com_box basefix">
            <meta itemprop="ratingValue" content="" />
            <a class="commnet_score" href="/hotel/dianping/428365.html" title="客户点评：4.7分，总分5分。" name="needTraceCode" data-dopost="T">
                <span class="hotel_level">很好</span><p class="s_row"><span class="score">4.7</span>/5分</p><p class="s_row">97%用户推荐</p><span class="commnet_num">源自<span itemprop="reviewCount">6518位住客点评</span>
			</span></a>
            <div class="comment_text hidden" data-index="0" id="J_defaultCommentRecommand"><div class="text_box"><div class="text"><span class="p"></span>1***0:<br />“带孩子到新华医院看病，住在这里是最好的选择，离新华只有三站地铁。干净卫生房间够大，酒店用品是欧舒丹的。
订的是湖景房，视野很好，我在携程订的时候没有选择大床还是双床，到了前台说要双床，但是只有大床了，前台的小姑娘很热情的给升级了房间。
26楼的西餐口味尚可，只是不明白为什么要消费者承担税费？
小南国中餐厅点了它的名菜，花雕蒸鲥鱼，388元，以为会很鲜美，但是略失望，不是新鲜的鱼，是腌制过的，肉已不鲜嫩，有点柴，再加上花雕酒，真的好咸，如果这个菜作为小南国名菜，绝对需要改进。
糖醋小排孩子很爱吃。
酒店其他都不错，下次来还住这里。
还有，洗手间地漏确实像很多人评价的那样，有异味，需改进。”</div></div></div>
            <div class="comment_text" data-index="0" id="J_commentRecommand"><div class="text_box">
            <div class="text"><span class="p"></span>1***1<br />“很舒适的房间，景观一流，楼下就是漂亮的黄兴公园，没有时间享用早餐，中餐全日制餐厅的味道和品种都挺好的，不过最好先预定，用餐的人蛮多。个人觉得离地铁黄兴公园站挺近，不穿恨天高10分钟以内能到，公交站就在地铁站门口，交通很方便啦！在酒店外的十字路口有星巴克和超市，晚上买了些水果挺新鲜。总体感觉非常好，下次若还在附近出差会继续选择小南国花园酒店。👍🏻👍🏻”</div>
        </div></div>
        </div>
	</div>

    <div class="htl_com htl_com_no_comment J_htl_com hidden">
			<div class="htl_no_com_box basefix">
				<div class="no_commnet_txt">暂无点评</div>
			</div>
    </div>


	<div class="htl_map">
        
        <a href="/map/428365.html" class="view" id="viewMap" data-hotelid="428365">查看地图</a>
        
        <div class="map" id="map" style="overflow: hidden; width: 300px; height: 222px;"><div style="height: 151px; width: 300px; padding-top: 71px; text-align: center; background-color: rgb(255, 255, 255); display: none;"><img src="//pic.ctrip.com/common/loading_50.gif" /></div><iframe src="/Domestic/MapIframeDetail.aspx?city=2&amp;province=2" frameborder="none" scrolling="no" width="300px" height="222px" style="border: none;"></iframe></div>
    </div>

            <div class="traffic_side">
    <div class="title">交通信息</div> 
    <div class="traffic_box">
        
            
            <div class="traffic_item">
                <span class="spot_type shopping"></span>
                
                <p class="name"><a href="javascript:;" class="rounte" data-name="江湾、五角场商业区" data-lnglat="121.51953887939453|31.306631088256836" data-distance="3.57">路线</a>江湾、五角场商业区</p>
                <p class="distance">驾车距离3.6公里（约7分钟）</p>
                
                <p class="name"><a href="javascript:;" class="rounte" data-name="吴淞口国际邮轮港" data-lnglat="121.48900604248047|31.409420013427734" data-distance="15.7">路线</a>吴淞口国际邮轮港</p>
                <p class="distance">驾车距离15.7公里（约26分钟）</p>
                
            </div>
            
        
            
            <div class="traffic_item">
                <span class="spot_type airport"></span>
                
                <p class="name"><a href="javascript:;" class="rounte" data-name="浦东国际机场" data-lnglat="121.809|31.15597" data-distance="36.9">路线</a>浦东国际机场</p>
                <p class="distance">驾车距离36.9公里（约44分钟）</p>
                
                <p class="name"><a href="javascript:;" class="rounte" data-name="虹桥国际机场" data-lnglat="121.3345718|31.2001705" data-distance="28.17">路线</a>虹桥国际机场</p>
                <p class="distance">驾车距离28.2公里（约45分钟）</p>
                
            </div>
            
        
            
            <div class="traffic_item">
                <span class="spot_type train"></span>
                
                <p class="name"><a href="javascript:;" class="rounte" data-name="虹桥火车站" data-lnglat="121.3273|31.20061" data-distance="28.09">路线</a>虹桥火车站</p>
                <p class="distance">驾车距离28.1公里（约45分钟）</p>
                
                <p class="name"><a href="javascript:;" class="rounte" data-name="上海火车站" data-lnglat="121.4617|31.25503" data-distance="11.14">路线</a>上海火车站</p>
                <p class="distance">驾车距离11.1公里（约20分钟）</p>
                
            </div>
            
        
            
            <div class="traffic_item">
                <span class="spot_type centre"></span>
                
                <p class="name"><a href="javascript:;" class="rounte" data-name="市中心" data-lnglat="121.4802384079|31.2363508011" data-distance="11.07">路线</a>市中心</p>
                <p class="distance">驾车距离11.1公里（约23分钟）</p>
                
            </div>
            
        
            
            <div class="traffic_item">
                <span class="spot_type sight"></span>
                
                <p class="name"><a href="javascript:;" class="rounte" data-name="共青国家森林公园" data-lnglat="121.55773|31.32594" data-distance="4.51">路线</a>共青国家森林公园</p>
                <p class="distance">驾车距离4.5公里（约10分钟）</p>
                
                <p class="name"><a href="javascript:;" class="rounte" data-name="浦江游船" data-lnglat="121.52499|31.255638" data-distance="7.23">路线</a>浦江游船</p>
                <p class="distance">驾车距离7.2公里（约16分钟）</p>
                
            </div>
            
        
    </div>
 </div>
            
<div id="faq-block" class="faq-block side_mod J_faq_block">
    <div class="faq-block-hd">
		<h3 class="title">酒店问答</h3>		
		<div class="J_ask_info ask-first"><a href="javascript:;" id="faq428365" class="btn J_ask">我要提问</a><p class="tips">还没有人提问哦，你开个头吧！</p></div>
	</div>
    
    <a class="go-default-qa J_go_default_qa J_qa_part hidden" herf="javascript:;">
		<i class="arrow-right"></i>
		<p class="t1">常见问答</p>
		<p class="t2">支付、担保、返现、酒店联系方式等</p>
	</a>
    <div class="J_faq_container J_qa_part">
    
	<ul class="qa-user-list">
        
	</ul>
</div>
    <!--常见问答列表-->
    <div class="qa-default J_qa_default J_default_part">
        <ul>
			<li>
				<div class="qa-default-box">
					<span class="qa-default-q"><i></i>预订酒店如何支付房费？</span>
					<p class="qa-default-a">如【预订】图标下方注明【担保】或没有文字说明，表示房费当天在酒店前台付。具体支付方式请与酒店确认哦～如【预订】图标下方注明【预付】，表示房费需要全额预付至携程，您可以在支付界面看到目前订单可以选择的支付方式（例如信用卡，第三方、支付宝，微信等，具体请以网上提示您的支付方式为准）。</p>
				</div>
			</li>
			<!--hover后的效果白底+出向下的icon-->
			<li>
			    <div class="qa-default-box">
					<span class="qa-default-q"><i></i>预订的酒店能保证可以入住吗？</span>
					<p class="qa-default-a">酒店订单提交后会有短信回复您是否预订成功，只要您收到携程的确认，且您按订单上的信息入住，就确认有房间。收到相关短信后届时凭有效证件即可办理入住哦～</p>
				</div>
			</li>
			<li>
				<div class="qa-default-box">
					<span class="qa-default-q"><i></i>什么是酒店担保？</span>
					<p class="qa-default-a">由于房源紧张等问题，部分酒店要求客人在预订时提供担保，一般支持信用卡、支付宝、第三方网银担保，担保后当晚房间将一直为客人保留。届时在您离店后，酒店会进入审核状态，在订单审核确认入住后3个工作日内，担保金额会解冻，全额退还到您的支付帐户中～请放心～如您未入住，将从您的担保费用中扣除部分或全部房费哦～<br />	小游温馨提示：担保订单在您到酒店后，正常支付押金办理入住，离店时支付房费即可。</p>
				</div>
			</li>
			<li>
				<div class="qa-default-box">
				    <span class="qa-default-q"><i></i>如何查询酒店联系电话？</span>
					<p class="qa-default-a">您在通过点击【酒店详情-详情/卖点-酒店介绍-联系酒店】即可查看到酒店电话哟~</p>
				</div>
			</li>
			<li>
				<div class="qa-default-box">
				    <span class="qa-default-q"><i></i>如何添加酒店特殊要求？</span>
				  	<p class="qa-default-a">如您有特殊要求（如需要安排大床、无烟房等）或有问题要确认，可以在预订时点击【特别要求】注明您的需求，并提交订单，酒店专员会为您联系酒店哦。<br />小游温馨提示：特殊要求一般酒店只能尽量安排，无法保证。部分酒店预订时不接受任何特殊要求，此类酒店在预订时就没有【特别要求】输入框，预订时请留意哦~</p>
				</div>
			</li>
			<li>
				<div class="qa-default-box">
					<span class="qa-default-q"><i></i>酒店有接送机服务吗？</span>
					<p class="qa-default-a">您可以在点击【预订】后的填写信息页面下方"特别提示"中查看哦。如果有接机，需要您在订单的【特别要求】中备注上您的航班信息/车次信息，我们会有专员与酒店确认的。如您需要收费的接送机（站）服务， 请您在【特别要求】注明相关情况，由专员为您确认收费情况。<br />小游温馨提示：若您需要单独预订接送机服务，您可以在首页点击【用车 自驾】 预订哦～</p>
				</div>
			</li>
			<li>
		    	<div class="qa-default-box">
					<span class="qa-default-q"><i></i>预订酒店是否能确定房间号？</span>
					<p class="qa-default-a">预订酒店暂时没有房间号，酒店会在您到店时根据当天排房情况来安排房间的哦～～</p>
				</div>
			</li>
			<li>
				<div class="qa-default-box">
					<span class="qa-default-q"><i></i>凌晨到店如何预订？</span>
					<p class="qa-default-a">如您在凌晨6：00前到店都算是前一天的预订，需要下前一天的订单，预订时请在订单【特别要求】中注明您的实际最晚到店时间，到中午12：00退房，算一天房费。【例如：您实际入住时间为1月2日凌晨1：00，到1月2日中午12：00，即算一天房费，订单应提交1月1日入住哦】</p>
				</div>
			</li>
			<li>
				<div class="qa-default-box">
					<span class="qa-default-q"><i></i>如何查看酒店入住与离店时间？</span>
					<p class="qa-default-a">您可以点击酒店名称，在页面下方“酒店政策”中查看酒店入住和离店时间哦～</p>
				</div>
			</li>
		</ul>				
	</div>
    <div class="page-list J_page_control J_qa_part hidden">
		<a class="first" herf="javascript:;"><i class="ico"></i></a>
		<a class="prev" herf="javascript:;"><i class="ico"></i></a>
		<span class="page-num"><input type="text" class="num J_qa_page_num" value="1" data-val="1" />/<span class="J_total_page_num" max-num="1">1</span><a class="submit disabled hidden" href="javascript:;">确定</a></span>
		<a class="next" herf="javascript:;"><i class="ico"></i></a>
		<a class="last" herf="javascript:;"><i class="ico"></i></a>							
	</div>
</div>

<div id="pop-box-ask" class="pop-box pop-box-ask hidden">
	<a class="c_close" href="javascript:void(0);">×</a>
	<div class="pop-bd">
		<p><span class="fr"><span class="charnumber" data-maxlen="50">0</span>/50字</span>我的问题</p>
		<textarea placeholder="请输入您想要提的问题" class="form-textarea" id="J_AskTitle"></textarea>
		<div class="wrap-email">
			<input type="text" value="" placeholder="请输入您的邮箱地址" class="form-text" id="J_userEmail" /><span class="gray">邮件会告诉您有答案了。</span><a class="btn-primary fr disabled" href="javascript:void(0);"><i class="icon-loading hidden"></i><span>发表问题</span></a>
		</div>
	</div>
</div>

<div id="pop-box-msg" class="pop-box pop-box-msg hidden">
	<div class="pop-hd"><a class="c_close" href="javascript:void(0);">×</a>友情提示：</div>
	<div class="pop-bd"></div>
	<div class="pop-ft"><a class="btn btn-primary" href="javascript:void(0);">确定</a></div>
</div>

<div id="pop-qa-box" class="pop-box pop-qa-box hidden">
	<a class="c_close" href="javascript:void(0);">×</a>
	<div class="qa-write">
		<div class="qustion-title">
			<p class="head-ask">问<i class="icon-right"></i></p>
			<p class="txt J_question" title=""></p>
			<p class="info"></p>
		</div>
		<textarea class="qa-textarea" placeholder="请输入回答，尽可能详细描述哦"></textarea>
		<div class="txt-num" data-maxlen="500">最多可输入500个字</div>
		<div class="submit-again">
			<a href="javascript:;" class="btn btn-large disabled">发表</a>
			<p class="tips hidden"><i class="ico"></i>您的回答提交出现问题，请重新提交</p>
		</div>
	</div>
</div>

<div class="pop-box pop-qa-box J_reply_loading hidden">
	<div class="qa-load">
		<p class="txt"><i class="ico"></i>正在发表您的回答，请勿关闭该页面</p>
	</div>
</div>
<div class="pop-box pop-qa-box J_replay_success hidden">
	<a class="c_close" href="###">×</a>
	<div class="qa-success">
		<p class="txt"><i class="ico"></i>您的回答已提交成功，等待审核中...</p>
		<a href="javascript:;" class="btn btn-large">确定</a>
	</div>
</div>

<script type="text/javascript" language="javascript">
    var faqConfig = {
        addFaqUrl: "/Domestic/tool/AjaxHotelFaqAdd.aspx",
        AddReplyUsefulUrl : "/Domestic/tool/AjaxHotelFaqReplyUseful.aspx",
        isCallAjax: true,
        loadFaqUrl: "/Domestic/tool/AjaxHotelFaqLoad.aspx",
        replyFaqUrl: "/Domestic/tool/AjaxHotelFaqReply.aspx",
        cityId : 2,
        hotelId : 428365,
        hotelName: "上海小南国花园酒店",
        hotelEname: "WH Ming Hotel Shanghai",
        quickLogin : false
    };
</script>

<script type="text/template" id="J_htlQaListTmpl">
    {{if multipage}}
        &lt;div class="go-strategy"&gt;&lt;a href="${tagUrl}"&gt;全部问答&amp;nbsp;&amp;gt;&lt;/a&gt;&lt;/div&gt;
    {{/if}}
	&lt;ul class="qa-user-list"&gt;
        {{each qaList}}
            &lt;li&gt;
				&lt;div class="user-modular"&gt;
                    {{if isMyAsk}}
                        &lt;p class="head-my"&gt;我的问题&lt;i class="icon-right"&gt;&lt;/i&gt;&lt;/p&gt;
                    {{else}}
                        &lt;p class="head-ask"&gt;问&lt;i class="icon-right"&gt;&lt;/i&gt;&lt;/p&gt;
                    {{/if}}
					&lt;p class="txt" title="${qTitle}"&gt;${q}&lt;/p&gt;
                    &lt;p class="info"&gt;
                            &lt;span class="uname"&gt;${qn}&lt;/span&gt;
                             &lt;span class="time"&gt;${qt}&lt;/span&gt;
                        &lt;/p&gt;
					&lt;p class="tools"&gt;
                         &lt;span class="label"&gt;${ql}&lt;/span&gt;
                         {{if !isMyAsk &amp;&amp; isAnswerable }}&lt;a href="javascript:;" id="reply${id}" class="answer-btn" data-id="${id}"&gt;我来回答&lt;/a&gt;{{/if}}
					  &lt;/p&gt;
				&lt;/div&gt;
                {{each rList}}
                    &lt;div class="user-modular"&gt;
					    &lt;p class="head-master"&gt;						
					    &lt;/p&gt;
                        &lt;p class="head-ans"&gt;答&lt;i class="icon-right"&gt;&lt;/i&gt;						
					    &lt;/p&gt;
					    &lt;p class="txt" title="${aTitle}"&gt;${a}
                        &lt;/p&gt;
					    &lt;p class="info"&gt;
                            &lt;span class="uname"&gt;${rn}&lt;/span&gt;
                            &lt;span class="time"&gt;${rt}&lt;/span&gt;
                        &lt;/p&gt;
                        &lt;p class="tools"&gt;
					        &lt;span class="label"&gt;${rl}&lt;/span&gt;
                            {{if !zd}}
					            &lt;span class="{{if zaned}}useful{{else}}useless{{/if}} J_faq_add_askZan"&gt;&lt;i class="i-use J_like" ask-id="${id}" answer-id="${rid}"&gt;&lt;/i&gt;有用 &lt;span class="J_usefulCount"&gt;${uc}&lt;/span&gt;&lt;/span&gt;
                            {{/if}}
					    &lt;/p&gt;
				    &lt;/div&gt;
                {{/each}}
                {{if rc &gt; 3}}
                    &lt;div class="other-answer"&gt;&lt;a href="${ru}" target="_blank"&gt;查看其它${rc - 3}条回答&amp;nbsp;&amp;gt;&lt;/a&gt;&lt;/div&gt;
                {{/if}}
			&lt;/li&gt;    
        {{/each}}
	&lt;/ul&gt;
</script>

            <div id="groupProduct" class="">
    <div class="sider_tuan">
        <div class="sider_title"><a href="http://tuan.ctrip.com/group/city_shanghai/item_2/" class="more" target="_blank">更多 </a>酒店周边美食团购</div>
        <ul class="sider_tuan_list">
            
            <li>
                <a href="http://tuan.ctrip.com/group/10343051.html" target="_blank"><img src="http://images4.c-ctrip.com/target/2A0u0v000000jvt84A124.jpg" width="62" height="62" alt="" onerror="this.src='//images4.c-ctrip.com/target/fd/tuangou/g6/M01/EC/B1/CggYtFcl8bmAZviXAAA7i47G0go720.jpg';this.onerror=null;" /></a>
                <a href="http://tuan.ctrip.com/group/10343051.html" class="tuan_name" target="_blank">WH中西荟臻双人下午茶</a>
                <p class="tuan_num">已售112份</p><p class="tuan_price"><dfn>¥</dfn><span class="price">168</span></p>
            </li>
            
            <li>
                <a href="http://tuan.ctrip.com/group/10309424.html" target="_blank"><img src="http://images4.c-ctrip.com/target/2A0r0v000000js7sv4B20.jpg" width="62" height="62" alt="" onerror="this.src='//images4.c-ctrip.com/target/fd/tuangou/g6/M01/EC/B1/CggYtFcl8bmAZviXAAA7i47G0go720.jpg';this.onerror=null;" /></a>
                <a href="http://tuan.ctrip.com/group/10309424.html" class="tuan_name" target="_blank">工作日自助晚餐</a>
                <p class="tuan_num">已售129份</p><p class="tuan_price"><dfn>¥</dfn><span class="price">178</span></p>
            </li>
            
            <li>
                <a href="http://tuan.ctrip.com/group/10309412.html" target="_blank"><img src="http://images4.c-ctrip.com/target/2A0r0v000000ju8ot7062.jpg" width="62" height="62" alt="" onerror="this.src='//images4.c-ctrip.com/target/fd/tuangou/g6/M01/EC/B1/CggYtFcl8bmAZviXAAA7i47G0go720.jpg';this.onerror=null;" /></a>
                <a href="http://tuan.ctrip.com/group/10309412.html" class="tuan_name" target="_blank">工作日自助午餐</a>
                <p class="tuan_num">已售140份</p><p class="tuan_price"><dfn>¥</dfn><span class="price">138</span></p>
            </li>
            
        </ul>
    </div>
 </div>
            <div class="sider_pic hidden" style="*zoom:1;"> 
                <div id="favlist"></div>
                
 
                <!--浏览历史记录-->
                <div id="visitedHistory"></div>
                
<!--酒店活动-->

            </div>
        </div>
        
<div class="detail2_room_area seo_201305"> 
				<p class="p"><img src2="//dimg11.c-ctrip.com/images/hotel/373000/372135/c3028fa548b34dd883e187498a1fe26e_R_300_225.jpg" width="121" height="91" alt="上海小南国花园酒店" />携程网为您推荐<a target="_blank" data-dopost="T" class="black" href="/hotel/428365.html">上海小南国花园酒店</a>以及酒店预订、价格查询，上海小南国花园酒店信息，酒店地址：佳木斯路777号; 涵盖酒店周边设施，酒店交通地图，真实用户点评等信息，同时还可查找<a target="_blank" data-dopost="T" class="black" href="//vacations.ctrip.com/tours/d-shanghai-2">上海旅游</a>报价以及<a target="_blank" class="black" data-dopost="T" href="//you.ctrip.com/place/shanghai2.html">上海旅游攻略</a>。
                <a target="_blank" class="black" data-dopost="T" href="//hotels.ctrip.com/hotel/shanghai2">上海酒店</a>预订，<a target="_blank" class="black" data-dopost="T" href="//hotels.ctrip.com/domestic-2.html">上海酒店导航</a>，酒店团购，特价酒店，选携程更放心！
                <a class="seo_more" id="seo_more" href="javascript:;">查看全部</a></p>
                
                <dl class="seo_hot">
				<dt><h4>热门城市</h4></dt> 
				<dd><a title="北京酒店预订" href="//hotels.ctrip.com/hotel/beijing1" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_1" target="_blank">北京酒店</a></dd>
				<dd><a title="上海酒店预订" href="//hotels.ctrip.com/hotel/shanghai2" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_2" target="_blank">上海酒店</a></dd>
				<dd><a title="广州酒店预订" href="//hotels.ctrip.com/hotel/guangzhou32" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_3" target="_blank">广州酒店</a></dd>
				<dd><a title="深圳酒店预订" href="//hotels.ctrip.com/hotel/shenzhen30" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_4" target="_blank">深圳酒店</a></dd>
				<dd><a title="南京酒店预订" href="//hotels.ctrip.com/hotel/nanjing12" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_5" target="_blank">南京酒店</a></dd>
				<dd><a title="杭州酒店预订" href="//hotels.ctrip.com/hotel/hangzhou17" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_6" target="_blank">杭州酒店</a></dd>
				<dd><a title="成都酒店预订" href="//hotels.ctrip.com/hotel/chengdu28" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_7" target="_blank">成都酒店</a></dd>
				<dd><a title="厦门酒店预订" href="//hotels.ctrip.com/hotel/xiamen25" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_8" target="_blank">厦门酒店</a></dd>
				<dd><a title="青岛酒店预订" href="//hotels.ctrip.com/hotel/qingdao7" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_9" target="_blank">青岛酒店</a></dd>
				<dd><a title="三亚酒店预订" href="//hotels.ctrip.com/hotel/sanya43" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_10" target="_blank">三亚酒店</a></dd>
				<dd><a title="香港酒店预订" href="//hotels.ctrip.com/hotel/hong-kong58" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_11" target="_blank">香港酒店</a></dd>
				<dd><a title="澳门酒店预订" href="//hotels.ctrip.com/hotel/macau59" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_12" target="_blank">澳门酒店</a></dd>
				<dd><a title="西安酒店预订" href="//hotels.ctrip.com/hotel/xian10" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_13" target="_blank">西安酒店</a></dd>
				<dd><a title="苏州酒店预订" href="//hotels.ctrip.com/hotel/suzhou14" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_14" target="_blank">苏州酒店</a></dd>
				<dd><a title="长沙酒店预订" href="//hotels.ctrip.com/hotel/changsha206" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_15" target="_blank">长沙酒店</a></dd>
				<dd><a title="武汉酒店预订" href="//hotels.ctrip.com/hotel/wuhan477" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_16" target="_blank">武汉酒店</a></dd>
				<dd><a title="大连酒店预订" href="//hotels.ctrip.com/hotel/dalian6" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_17" target="_blank">大连酒店</a></dd>
				<dd><a title="天津酒店预订" href="//hotels.ctrip.com/hotel/tianjin3" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_18" target="_blank">天津酒店</a></dd>
				<dd><a title="重庆酒店预订" href="//hotels.ctrip.com/hotel/chongqing4" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_19" target="_blank">重庆酒店</a></dd>
				<dd><a title="长春酒店预订" href="//hotels.ctrip.com/hotel/changchun158" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_20" target="_blank">长春酒店</a></dd>
				<dd><a title="济南酒店预订" href="//hotels.ctrip.com/hotel/jinan144" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_21" target="_blank">济南酒店</a></dd>
				<dd><a title="贵阳酒店预订" href="//hotels.ctrip.com/hotel/guiyang38" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_22" target="_blank">贵阳酒店</a></dd>
				<dd><a title="昆明酒店预订" href="//hotels.ctrip.com/hotel/kunming34" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_23" target="_blank">昆明酒店</a></dd>
				<dd><a title="郑州酒店预订" href="//hotels.ctrip.com/hotel/zhengzhou559" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_24" target="_blank">郑州酒店</a></dd>
				<dd><a title="银川酒店预订" href="//hotels.ctrip.com/hotel/yinchuan99" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_25" target="_blank">银川酒店</a></dd>
				<dd><a title="南昌酒店预订" href="//hotels.ctrip.com/hotel/nanchang376" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_26" target="_blank">南昌酒店</a></dd>
				<dd><a title="沈阳酒店预订" href="//hotels.ctrip.com/hotel/shenyang451" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_27" target="_blank">沈阳酒店</a></dd>
				<dd><a title="石家庄酒店预订" href="//hotels.ctrip.com/hotel/shijiazhuang428" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_28" target="_blank" class="_blank">石家庄酒店</a></dd>
				<dd><a title="福州酒店预订" href="//hotels.ctrip.com/hotel/fuzhou258" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_29" target="_blank">福州酒店</a></dd>
				<dd><a title="合肥酒店预订" href="//hotels.ctrip.com/hotel/hefei278" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_30" target="_blank">合肥酒店</a></dd>
				<dd><a title="南宁酒店预订" href="//hotels.ctrip.com/hotel/nanning380" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_31" target="_blank">南宁酒店</a></dd>
				<dd><a title="乌鲁木齐酒店预订" href="//hotels.ctrip.com/hotel/urumqi39" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_32" target="_blank">乌鲁木齐酒店</a></dd>
				<dd><a title="太原酒店预订" href="//hotels.ctrip.com/hotel/taiyuan105" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_33" target="_blank">太原酒店</a></dd>
				<dd><a title="哈尔滨酒店预订" href="//hotels.ctrip.com/hotel/harbin5" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_34" target="_blank">哈尔滨酒店</a></dd>
				<dd><a title="兰州酒店预订" href="//hotels.ctrip.com/hotel/lanzhou100" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_35" target="_blank">兰州酒店</a></dd>
				<dd><a title="台北酒店预订" href="//hotels.ctrip.com/hotel/taipei617" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_36" target="_blank">台北酒店</a></dd>
				<dd><a title="拉萨酒店预订" href="//hotels.ctrip.com/hotel/lasa41" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_37" target="_blank">拉萨酒店</a></dd>
				<dd><a title="西宁酒店预订" href="//hotels.ctrip.com/hotel/xining124" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_38" target="_blank">西宁酒店</a></dd>
				<dd><a title="呼和浩特酒店预订" href="//hotels.ctrip.com/hotel/huhehaote103" data-ctm="#ctm_ref=hd_hp_hc_lst_hi_i_a_39" target="_blank">呼和浩特酒店</a></dd>
				</dl>
				<div class="seo_line"></div>
				<dl class="seo_hot sta_unfold">
				<dt><h4>品牌推荐</h4></dt>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h132/" title="7天连锁酒店">7天连锁酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h110/" title="如家快捷酒店">如家快捷酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h48/" title="汉庭酒店">汉庭酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h50/" title="锦江之星酒店">锦江之星</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h35/" title="香格里拉酒店">香格里拉酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h168/" title="格林豪泰酒店">格林豪泰</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h44/" title="莫泰168酒店">莫泰168</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h160/" title="布丁酒店">布丁酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h68/" title="桔子酒店">桔子酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h10/" title="希尔顿酒店">希尔顿</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h166/" title="凯宾斯基酒店">凯宾斯基</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h23/" title="皇冠假日酒店">皇冠假日酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h15/" title="威斯汀酒店">威斯汀酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h21/" title="假日酒店">假日酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h12/" title="喜来登酒店">喜来登酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h152/" title="维也纳酒店">维也纳酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h53/" title="星程酒店">星程酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h8/" title="宜必思酒店">宜必思酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h24/" title="洲际酒店">洲际酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h18/" title="万豪酒店">万豪酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h39/" title="速8酒店">速8酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h26/" title="凯悦酒店">凯悦酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h108/" title="百时快捷酒店">百时快捷酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h162/" title="半岛酒店">半岛酒店</a></dd>
                <dd><a target="_blank" href="//hotels.ctrip.com/brand/h5/" title="诺富特酒店">诺富特酒店</a></dd>
                </dl>

                
				
</div>

    </div>
</div>

<!--集团酒店非首次预订提示-->
<div class="pop-box hidden" id="J_ForNewUserPopbox">
    <div class="pop-hd"><a class="c_close" href="###">×</a>温馨提示</div>
    <div class="pop-bd">
        <div class="first-book">此房型价格仅携程用户首次预订酒店可享，您可预订该酒店的其他同类房型</div>
    </div>
    <div class="pop-ft">
        <a class="btn J_return" href="javascript:;">返回</a>
    </div>
</div>
<div id="J_roomDetail_float" style="position: absolute;z-index:10;top=500px;display:none;">
    <div class="pop-box htl-room-detail" id="J_room_detail"></div>
</div>   
<!--Input标签 -->   
<input type="hidden" id="hotel" value="428365" />
<input type="hidden" id="hotel_pic" value="" />
<input type="hidden" id="room_pic" value="" />
<input type="hidden" name="useFG" id="useFG" value="F" />
<input type="hidden" name="__action" value="ShowHotelListNew.aspx" />
<input type="hidden" id="rdoHotelType" name="rdoHotelType" />
<input type="hidden" id="rdoStar" name="rdoStar" />
<input type="hidden" id="cityId" name="cityId" value="2" />
<input type="hidden" id="cityPY" name="cityPY" value="Shanghai" />
<input type="hidden" id="cityCode" name="cityCode" value="021" />
<input type="hidden" id="cityName" name="cityName" value="上海" />
<input type="hidden" id="priceCx" name="priceCx" />
<input type="hidden" id="positionArea" name="positionArea" />
<input type="hidden" id="positionId" name="positionId" />
<input type="hidden" id="hotelAreaName" name="keyword" />
<input type="hidden" id="checkIn" name="Checkin" value="2018-09-21" />
<input type="hidden" id="checkOut" name="Checkout" value="2018-09-22" />
<input type="hidden" id="DealSale" name="DealSale" />
<input type="hidden" id="hotsalesroomids" value="" />
<input type="hidden" id="isTravelMoneyFromList" value="" />
<input type="hidden" id="isJustConfirmFromList" value="" />
<input type="hidden" id="htl.list.seladd" data-key="htl.list.seladd" />
<input type="hidden" id="htl.detail.subrmsel" data-key="htl.detail.subrmsel" />
<input id="ulogin" type="hidden" name="ulogin" />
<input type="hidden" id="HotelInfoFrom" value="" /> 
<div class="hidden" itemprop="geo" itemscope="" itemtype="//schema.org/GeoCoordinates">
<meta itemprop="latitude" content="31.298553330946" />
<meta itemprop="longitude" content="121.53983581837" />
<input type="hidden" id="ubt_price_key" name="ubt_price_key" value="htl_detail_htl_promotion" />
<input type="hidden" id="sctx" name="sctx" />
<input type="hidden" id="defaultcoupon" name="defaultcoupon" value="" />
<input type="hidden" id="swid" name="swid" />
<input type="hidden" id="priceLowList" value="" name="priceLowList" /> 

<input type="hidden" id="priceCheckIn" value="" name="pcheckIn" /> 
<input type="hidden" id="priceCheckOut" value="" name="pcheckOut" />
<input type="hidden" id="from" name="from" />
<input type="hidden" id="isFullFromList" name="isFullFromList" value="" />
<input type="hidden" id="defaultLoad" name="defaultLoad" value="F" /><!--默认第一次加载-->
 <input type="hidden" id="hasPyramid" value="T" />
 <input type="hidden" id="keyword" value="" />
 <input type="hidden" id="zonelist" value="" />
 <input type="hidden" id="starlist" value="" />
 <input type="hidden" id="hotelposition" value="" />
 <input type="hidden" id="traceAdContextIdFromList" value="" />
 <input type="hidden" id="traceAdContextId" name="traceAdContextId" value="" />
 <input type="hidden" id="estagid" name="estagid" value="" />
 <input type="hidden" id="esfiltertag" name="esfiltertag" value="" />
</div>


<input type="hidden" id="htlPageView" name="htlPageView" value="0" />
<input type="hidden" value="M:21,161214_hod_lhlz:B;M:60,180522_hod_onsz:B" id="ab_testing_tracker" />
<input type="hidden" id="page_id" value="102003" />
<input type="hidden" id="hotelCoordinate" value="121.53983581837|31.298553330946" />
<input type="hidden" id="orderid" name="orderid" value="0" />
<input type="hidden" name="hotel" value="428365" />
<input type="hidden" name="Resource" value="" />
<input type="hidden" name="Room" value="" />
<input type="hidden" name="Paymentterm" value="" />
<input type="hidden" name="BRev" value="" />
<input type="hidden" name="Minstate" value="" />
<input type="hidden" name="PromoteType" value="" />
<input type="hidden" name="PromoteDate" value="" />
<input type="hidden" name="operationtype" value="NEWHOTELORDER" />
<input id="startdate" type="hidden" name="StartDate" value="2018-09-21" />
<input id="depdate" type="hidden" name="DepDate" value="2018-09-22" />
<input type="hidden" id="_releaseNo_" value="2018-09-20-02-02-00" />
<input type="hidden" id="J_edm" name="EDM" value="" />
<input type="hidden" id="htl.detail.subrmsel" value="" data-key="htl.detail.subrmsel" /> 
<input type="hidden" name="tag" value="" />
<input type="hidden" name="tagtop" value="" />
<input type="hidden" name="tagrank" value="" />

<!--特惠酒店专用 begin-->
<input type="hidden" name="returnurl" value="" />
<input type="hidden" name="ishotsale" value="0" />
<!--特惠酒店专用 end-->

<input type="hidden" id="init_page_id" value="102003" />
<input type="hidden" id="qrcodeurl" value="https://m.ctrip.com/webapp/hotel/wechatlab/detail/428365?allianceid=&amp;sid=" />
    

             

 <!-- PageUrl for SEO:   aHR0cDovL2hvdGVscy5jdHJpcC5jb20vRG9tZXN0aWMvU2hvd0hvdGVsSW5mb3JtYXRpb24uYXNweD9ob3RlbD00MjgzNjUmdGFiPTEm  -->
        
<div id="hotelBrandAjaxSuggest" style="left: 441px; top: 460px; display: none; position: absolute;" class="choice box_shadow">
    <div id="hotelBrandAjaxLoading" style="text-align: center;">
        <img src="//pic.c-ctrip.com/common/loading.gif" alt="" style="vertical-align: -4px" />
        查询中...
    </div>
    <div id="hotelBrandAjaxResultList">
    </div>
</div>
<div id="photoabulm" class="hidden"></div>
<div id="jmpTempCommon" style="display:none;">
    <div class="jmp_bd">
        ${txt}
    </div>
</div>
<div id="jmpTemp" class="hidden">
    
	
    
 <div id="jmpTempCashback">
    <div class="jmp_bd">
        <h5 style="font-size:12px;">使用消费券预订酒店返现金</h5>
        <div>
            入住离店后3个工作日自动返现<dnf>¥</dnf>${txt}至你的携程账户。
        </div>
        {{if HasCoupon='T'}}
        <h5 style="font-size:12px;">${title}</h5>
        <div>
            ${context}
        </div>
        {{/if}}
        <div class="jmp_warn">
           <i></i>使用礼品卡支付，将不能同时享受返现活动。
        </div>
    </div>
</div>

 <div id="jmpTempCashbackNew">
    <div class="jmp_bd">
        <h5 style="font-size:12px;">使用消费券预订酒店返现金</h5>
        <div>
            入住离店后3个工作日自动返现<dnf>¥</dnf>${total}至你的携程账户，每晚返现<dnf>¥</dnf>${avg}元
        </div>
        <div class="jmp_warn_new">
         若您使用礼品卡支付订单将无法享受返现
       </div>
        {{if HasCoupon='T'}}
        <h5 style="font-size:12px;">${title}</h5>
        <div>
            ${context}
        </div>
        {{/if}}
    </div>
</div>


    
 <div id="jmpTempRefundNow">
   <div class="jmp_bd">
       <h5 style="font-size:12px;">预订酒店返现金</h5>
       <div>
           入住离店后3个工作日自动返现<dnf>¥</dnf>${txt}至你的携程账户。
       </div>
       {{if HasCoupon='T'}}
        <h5 style="font-size:12px;">${title}</h5>
        <div>
            ${context}
        </div>
        {{/if}}
       <div class="jmp_warn">
           <i></i>使用礼品卡支付，将不能同时享受返现活动。
       </div>
   </div>
</div>


    

<textarea id="jmpTempTravelTicket" style="display:none">&lt;div class="jmp_bd"&gt;
    &lt;h5 style="font-size:12px;"&gt;预订酒店送礼品卡&lt;/h5&gt;
    &lt;div&gt;
        &lt;table&gt;
            {{each data}}
            &lt;tr&gt;
                &lt;td style="width:550px;border-bottom: 1px dashed #CCCCCC; vertical-align:top;"&gt;入住离店后3个工作日自动返现${info}元礼品卡至你的携程账户。&lt;/td&gt;
            &lt;/tr&gt;
            {{/each}}
        &lt;/table&gt;
            &lt;a href="//help.ctrip.com/QuestionDetail.aspx?questionId=475" target="_blank"&gt;返现帮助&lt;/a&gt;
    &lt;/div&gt;
&lt;/div&gt;
</textarea>


    

 <textarea id="jmpTempTicket" style="display:none">        &lt;div class="jmp_bd"&gt;
            &lt;h5 style="font-size:12px;"&gt;预订酒店送抵用券&lt;/h5&gt;
            &lt;div&gt;
                &lt;table&gt;
                    {{each data}}
                    &lt;tr&gt;
                          &lt;td style="border-bottom: 1px dashed #CCCCCC; vertical-align:top;"&gt;网上成功预订并入住，且完成Email确认，订单成交后3个工作日内您将获得${info}元抵用券。&lt;/td&gt;
                    &lt;/tr&gt;
                    {{/each}}
                &lt;/table&gt;
                &lt;a href="//help.ctrip.com/QuestionDetail.aspx?questionId=475" target="_blank"&gt;返现帮助&lt;/a&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    </textarea>
    
<div id="jmpTempCoupon" class="jmp_content">
	<div class="jmp_bd">
		<dl class="coupon_pop">
			<dt>酒店优惠券信息</dt>
			${txt}
			<dd class="coupon_pop_tip"><i class="icon_desc_text"></i>其他活动，以具体优惠券使用说明为准
		</dd></dl>
	</div>
</div>
    
<div id="jmpTempPackage">
<div class="jmp_bd">
<p>套餐内包含：</p>
    {{each info}}
        <p><span style="font-weight:bold;">·</span> ${txt}</p>
    {{/each}}
</div>
</div> 
 
 
    
 <div id="jmpTempNet">
    <div class="jmp_bd">
        <div>
            ${txt}
        </div>
    </div>
</div>    
<div id="jmpTempReduce">
<div class="pop_discount_box basefix">
	<h4>如何获得立减优惠</h4>
	<ul>
		<li class="method1">
			<span class="method">·方式一</span>
			<p>下载手机客户端，直接享受立减<dfn>¥</dfn><span class="price_tag">${price}</span>特惠</p>
			<div>
				<span class="method_txt">扫描下载客户端预订，<br />随时管理行程 </span>
				<img src="//pic.c-ctrip.com/hotels121118/book/pic_qrcode.png" />
			</div>
		</li>
		<li class="method2">
			<span class="method">·方式二</span>
			<p>立刻登录，输入3个月内机票订单号，享受立减<dfn>¥</dfn><span class="price_tag">${price}</span>特惠</p>
		</li>
	</ul>
</div>
</div>
    
 <div id="jmpTempCouponToolTip">
   <div class="jmp_bd"><h5 style="font-size:12px;">${txt}</h5>
        <div>
            ${context}
        </div> 
   </div>
</div> 
    
<textarea id="jmpTempPrice" style="display: none">	&lt;div class="jmp_breakfast"&gt;
		&lt;div class="hotel_everyday_data"&gt;
			&lt;p&gt;您已选择&lt;strong&gt;${checkIn}&lt;/strong&gt;至&lt;strong&gt;${checkOut}&lt;/strong&gt;&lt;span class="all"&gt;共&lt;strong&gt;${totalCount}&lt;/strong&gt;晚&lt;/span&gt;&lt;/p&gt;
			&lt;p&gt;
                {{each breakfastSum}}
                {{if isFirst == "F"}} | {{/if}}{{if iswuzao == "T"}}&lt;span&gt;{{else}}&lt;span class="text_green"&gt;{{/if}}${name}&lt;/span&gt;  {{if roomCount&gt;1}} &lt;strong&gt;${roomCount}&lt;/strong&gt;间 {{/if}}            &lt;strong&gt;${count}&lt;/strong&gt;晚
                {{/each}}
			&lt;/p&gt;
		&lt;/div&gt;
		&lt;div class="everyday_main"&gt;
			&lt;span class="btn_prev hidden" onclick="goPrevDInfo(this);"&gt;&lt;i&gt;&lt;/i&gt;&lt;/span&gt;
            {{if disnext == "T"}} 
			&lt;span class="btn_next" onclick="goNextDInfo(this);"&gt;&lt;i&gt;&lt;/i&gt;&lt;/span&gt;
            {{/if}}
			&lt;div class="everyday_scroll"&gt;
				&lt;ul class="everyday_item J_EveryDayScroll" cindex="1" style="width:3000px;"&gt;
                    {{enum(key1, arrPageData) info}}
                    &lt;li&gt;
						&lt;table cellspacing="0" cellpadding="0" class="hotel_everyday_list2"&gt;
							&lt;tbody&gt;
                                {{enum(key2, arrWeek) arrPageData}}
								&lt;tr&gt;
                                    {{each arrWeek}}
									&lt;th&gt;${day}&lt;/th&gt;
                                    {{/each}}
								&lt;/tr&gt;
								&lt;tr&gt;
                                    {{each arrWeek}}
                                    {{if isfull == "T"}}
                                        &lt;td class="day_full"&gt;&lt;p&gt;满房&lt;/p&gt;&lt;/td&gt;
                                    {{else}}
                                    &lt;td&gt;
                                        {{if isdata == "T"}}
										    &lt;p class="hotel_everyday_price"&gt;{{if flag == 2}}&lt;i class="i_high"&gt;高&lt;/i&gt;{{/if}}{{if flag == 1}}&lt;i class="i_low"&gt;低&lt;/i&gt;{{/if}}{{if roomstatus !="N"}}&lt;dfn&gt;¥&lt;/dfn&gt;{{/if}}&lt;span class="price"&gt;${price}&lt;/span&gt;&lt;/p&gt;
										    {{if isgat == "T"}}&lt;p&gt;&lt;dfn&gt;${currency}&lt;/dfn&gt;${oriprice}&lt;/p&gt;{{/if}}
										    {{if breakfast=="无早"}}&lt;p&gt;{{else}}&lt;p class="text_green"&gt;{{/if}}${breakfast}&lt;/p&gt;
                                        {{else}}
                                            &lt;p class="hotel_everyday_price"&gt; &lt;/p&gt;
										    &lt;p&gt; &lt;/p&gt;
										    &lt;p class="text_green"&gt; &lt;/p&gt;
                                        {{/if}}
									&lt;/td&gt;
                                    {{/if}}
                                    {{/each}}
								&lt;/tr&gt;
                                {{/enum}}
							&lt;/tbody&gt;
						&lt;/table&gt;
					&lt;/li&gt;
                    {{/enum}}
				&lt;/ul&gt;
			&lt;/div&gt;
		&lt;/div&gt;
		{{if totalPrice &amp;&amp; totalPriceDesc &amp;&amp; totalPriceDesc2}}
		&lt;div class="hotel_currency"&gt;&lt;strong&gt;${totalPriceDesc}总价：&lt;/strong&gt; &lt;span class="base_price"&gt; ${currency} ${totalPrice}&lt;/span&gt; &lt;/div&gt;
		&lt;span style="color:gray"&gt;${totalPriceDesc2}&lt;/span&gt;
		{{/if}}
		{{if TaxDesc}}
		&lt;span style="color:gray"&gt;${TaxDesc}&lt;/span&gt;
		{{/if}}
		&lt;div class="hotel_currency"  style="${display}"&gt;&lt;strong&gt;货币换算&lt;/strong&gt; &lt;span class="base_price"&gt; ${currency} ${avePrice}&lt;/span&gt; = ${oriCurrency} ${oriPrice} &lt;span class="hotel_currency_tips"&gt;人民币价格仅供参考&lt;/span&gt;&lt;/div&gt;
	&lt;/div&gt;
</textarea>
    
<textarea id="jmpTempPriceOld" style="display:none">	    &lt;div class="jmp_breakfast"&gt;
            &lt;!--只有港澳才会显示下面代码--&gt;
            &lt;div class="hotel_currency"  style="margin:6px;${display}"&gt;&lt;strong&gt;货币换算&lt;/strong&gt; &lt;span class="base_price" style="color:#f60;"&gt; ${currency} ${avePrice}&lt;/span&gt; = ${oriCurrency} ${oriPrice}
            &lt;/div&gt;
            &lt;table cellspacing="0" cellpadding="0" style="margin:6px;" class="hotel_everyday_list hotel_everyday_list2"&gt;
	           &lt;tbody&gt; 
                     {{enum(key,arr) info}}
                        &lt;tr&gt;
                        {{each arr}}
                        &lt;th&gt;${date}&lt;/th&gt;
                        {{/each}}
                        &lt;/tr&gt;
                        &lt;tr&gt;
                        {{each arr}}
                        &lt;td&gt;&lt;span class="hotel_everyday_price"&gt;${data[0]}&lt;/span&gt; &lt;span style=" ${display}" &gt;${data[1]}&lt;/span&gt; ${data[2]}&lt;/td&gt;
                        {{/each}}
                        &lt;/tr&gt;
                     {{/enum}}
                &lt;/tbody&gt; 
            &lt;/table&gt;
            &lt;div style="padding-top:6px; margin-bottom:-4px; color:#666; ${isdisplayinfo} " class="fyi"&gt;${displayinfo}&lt;/div&gt; 
            &lt;div class="hotel_everyday_txt" style="${showreduce}"&gt;${reduce}&lt;/div&gt;
        &lt;/div&gt;
        
    </textarea>    
    <div id="jmpTempCacnel">
            <div class="jmp_bd">
                <div>${txt}</div>
             </div>
        </div>
    <div id="jmpTempBookingStatus">
        <div class="jmp_bd">
            <p class="book_percent_tips">${txt}，
            {{if level == 1}}
                <span class="green">优于同业</span>
            {{/if}}
            {{if level == 0}}
                <span class="orange">与同业持平</span>
            {{/if}}
            {{if level == -1}}
                <span class="blue">低于同业</span>
            {{/if}}
            </p>
        </div>
    </div>
       
		<div id="jmpTempGift" class="jmp_content" style="display: block; width: 100%;">
			<div class="jmp_bd">
				<div class="jmp_discount_info">
                    {{if gift=='T' || package=='T'|| Spot=='T'}}
					<div class="title">酒店礼物信息</div>
                    {{/if}}
                    {{if gift=='T' || package=='F'}}
					${giftinfo}
                    {{/if}}
                     {{if Spot=='T'}}
                    <div class="list">
                    <span class="col1">${SpotDesc}</span>
                        </div>
                    {{/if}}
                    {{if package=='T'}}
                        <div class="list">
                        {{each(idx, value) pkgInfo}}
                        <div class="jmp_gift_cont_desc">{{if idx==0}}<span></span>{{/if}}<span>${value}</span></div>
                        {{/each}}
                        </div>
                    {{/if}}
                     {{if ShadowGift=='T'}}
                    {{if gift=='T'}}
                    <div class="title line">携程优惠信息</div>
                    {{/if}}
                    {{if gift=='F'}}
                    <div class="title">携程优惠信息</div>
                    {{/if}}
                    {{each(idx, gif) giftInfoTemp}}                            
                            <div class="list">
						        <span class="col1">${gif.GiftEffectDate}</span>
						        <span class="col2">${gif.GiftExpireDate}</span>
						        <span class="col3">${gif.GiftTips}</span>
					        </div>
                        {{/each}}
                     {{/if}}
				</div>
			</div>
		</div>
    <div class="jmp_content" id="jmpTempOnePrice">
        <div class="jmp_bd">
            <!--只有港澳才会显示下面代码-->
            <div style="margin:6px;">
                <strong>货币换算</strong> <span class="base_price" style="color:#f60;"> ${currency} ${avePrice}</span> = ${oriCurrency} ${oriPrice}
            </div>
        </div>
    </div>    
</div>



<div id="mapDialog" class="map_pop" style="display:none;">
    <a href="javascript:;" id="J_delMap" class="delete">×</a>
    <div class="map_box_tabs" style="right:290px;">
        <a id="J_showAMap" href="javascript:;" class="tabs_map hidden"><i class="tabs_map_icon"></i>地图</a>
        <a id="J_showSOSO" href="javascript:;" class="tabs_street hidden"><i class="tabs_street_icon"></i>街景</a>
    </div>
    <div id="J_mapBox" style="height:100%" class="map_box">
        <div id="J_amapLoading" class="map_pop_loading">地图加载中...</div>
        <div class="map_marker_tips" style="display:none;">请在地图上点击需要标记的点</div>
        <a class="map_marker_box" href="javascript:;"><i></i>标记</a>
        <div class="map_side" id="J_mapSide" style="height: 222px;">
            <div class="btn_side_close" id="J_foldBtn"><a href="javascript:;"></a></div>
            <div class="around_search" id="J_aroundSearch">
                <div class="map_side_title"><span class="back" id="J_aroundBack" style="display:none;"><a href="javascript:;">&lt; 返回</a>|</span>周边查询</div>
                <div class="around_box" id="J_aroundBox">
                    <a class="hotel" data-type="hotel" href="javascript:;"><i></i>酒店</a>
                    <a class="restaurant" data-type="restaurant" data-subtype="中餐|西餐|日本料理|韩国料理|快餐小吃|咖啡馆|蛋糕房" href="javascript:;"><i></i>餐厅</a>
                    
                    <a class="metro" data-type="metro" href="javascript:;"><i></i>地铁</a>
                    
                    <a class="entertainment" data-type="entertainment" data-subtype="KTV|电影院" href="javascript:;"><i></i>娱乐</a>
                    <a class="sight" data-type="sight" href="javascript:;"><i></i>景点</a>
                    <a class="market" data-type="market" href="javascript:;"><i></i>购物</a>
                </div>
            </div>
            <div class="traffic_hub" id="J_trafficHub" style="display:none">
                <div class="map_side_title">交通枢纽<span class="traffic_info">快速查询到酒店的路线</span></div>
                <div class="traffic_item">
                    <i class="airport"></i><span id="J_airportItem"></span>     
                </div>
                <div class="traffic_item">
                    <i class="train"></i><span id="J_stationItem"></span>
                </div>
            </div>
            <div class="rounte_search_ipad" id="J_rounteSearchIPad" style="display:none;">查询路线</div>
            <div class="route_search" id="J_routeSearch">
                <div class="map_side_title"><span class="back" id="J_routeBack" style="display:none;"><a href="javascript:;">&lt; 返回</a>|</span>线路查询</div>
                <div class="route_way" id="J_routeWay">
                    <a class="selected" href="javascript:;" data-way="transfer">公交</a>
                    <a href="javascript:;" data-way="driving">驾车</a>
                    <a href="javascript:;" data-way="walking">步行</a>
                </div>
                <div class="route_box">
                    <div class="change"><a href="javascript:;" id="J_changeStartEnd">换</a></div>
                    <input class="input_txt" type="text" id="J_startPoint" value="" />
                    <input class="input_txt" type="text" id="J_endPoint" value="" />
                    <a class="btn" id="J_routeSearchBtn" href="javascript:;">查询路线</a>
                </div>
            </div>
            <div class="around_list_box" id="J_aroundListBox" style="display:none;">
                <div class="around_title" id="J_aroundTitle" style="display:none;"><p class="result"><span class="num" id="J_aroundNum">0</span>条结果</p>周边<span class="b"><span id="J_aroundDistance">5</span>公里</span>的<span id="J_aroundType">酒店</span></div>
                <div class="list_type" id="J_aroundListType" style="display:none;"></div>
                <div class="no_result_spot" id="J_noResultSpot" style="display:none;">
                    <i class="i"></i>
                    <p class="txt">您所选的范围内未找到<span class="b">酒店</span>，</p>
                    <p class="txt">您可以拖动圆环扩大搜索范围。</p>
                </div>
                <div class="around_list" id="J_aroundList" style="height:469px;"></div>
                <div class="c_page_mini" id="J_aroundPage"></div>
            </div>
            <div class="no_result" id="J_noRoute" style="display:none;">
                <span class="i"></span>
                <p class="txt">没有查询到相关路线，</p>
                <p class="txt">请更换地点重新查询。</p>
            </div>
            <div class="no_result" id="J_tooClose" style="display:none;">
                <span class="i"></span>
                <p class="txt">起点和终点距离很近，</p>
                <p class="txt">您可以 <a class="b" id="J_orWalking" href="javascript:;">步行</a> 前往。</p>
            </div>
            <div class="result_error" id="J_startAndEnd" style="display:none;"></div>
            <div class="route_search_box" id="J_routeSearchBox" style="display:none;">
                <div class="route_result bus_route_result">
                    <div class="bus_sort">
                        <a class="selected" data-policy="LEAST_TIME" href="javascript:;">速度最快</a>
                        <a data-policy="LEAST_TRANSFER" href="javascript:;">最少换乘</a>
                        <a data-policy="LEAST_WALK" href="javascript:;">步行最少</a>
                        <a data-policy="NO_SUBWAY" href="javascript:;">不乘地铁</a>
                    </div>
                    <div class="line_tips">路线均为实时信息</div>
                    <div class="bus_route_height" style="height:409px;"></div>
                </div>
                <div class="route_result car_route_result" style="display:none;">
                    <div class="car_sort">
                        <a data-policy="REAL_TRAFFIC" href="javascript:;">躲避拥堵</a>
                        <a data-policy="LEAST_DISTANCE" href="javascript:;">避免高速</a>
                        
                    </div>
                    <div class="line_tips">路线均为实时信息</div>
                    <div class="car_total">
                        <p class="l"><a class="print" href="javascript:;">打印</a>全程约 <span class="b distance"></span></p>
                        <p class="l" id="J_taxiCost">打车费约 <span class="b"><span class="tolls"></span>元</span></p>
                    </div>
                    <div class="route_detail_box" style="height:337px;"></div>
                </div>
                <div class="route_result foot_route_result" style="display:none;">
                    <div class="line_tips">路线均为实时信息</div>
                    <div class="car_total">
                        <p>全程约 <span class="b distance"></span></p>
                        <p><a class="print" href="javascript:;">打印</a><!--打车费约 <span class="b"><span class="tolls"></span>元 -->或 <a id="J_changeBus" href="javascript:;">乘坐公交</a></p>
                    </div>
                    <div class="route_detail_box" style="height:383px;"></div>
                </div>
            </div>
        </div>
        <div class="map_content" id="mapContent"></div>
    </div>
    <div id="J_streetBox" style="height:100%" class="street_box hidden">
        <div id="J_streetLoading" class="map_pop_loading">正在进入街景...</div>
    </div>
</div>
<script type="text/template" id="J_aroundHotelTpl">
{{each(i, item) list}}
&lt;div class="around_item" data-uid="${uid}"&gt;
    &lt;span class="num"&gt;${i+1}&lt;/span&gt;
    {{if distance &gt; 0}}
    &lt;span class="distance"&gt;{{if distance &gt;= 1000}}&lt;span&gt;${Math.round(distance / 100) / 10}&lt;/span&gt;公里{{else}}&lt;span&gt;${distance}&lt;/span&gt;米{{/if}}&lt;/span&gt;
    {{/if}}
    &lt;p class="name"&gt;&lt;a class="around_hotel" href="/hotel/${id}.html" title="${name}" target="_blank" data-dopost="T"&gt;${name}&lt;/a&gt;&lt;/p&gt;
    &lt;div class="go_to" data-poi='{"name": "${name}", "pos": "${location.lng}|${location.lat}"}'&gt;
        &lt;a data-way="transfer" href="javascript:;"&gt;公交&lt;/a&gt;|&lt;a data-way="driving" href="javascript:;"&gt;驾车&lt;/a&gt;|&lt;a data-way="walking" href="javascript:;"&gt;步行&lt;/a&gt;
    &lt;/div&gt;
    &lt;p class="price"&gt;&lt;span class="base_price"&gt;&lt;dfn&gt;&amp;yen;&lt;/dfn&gt;${price}&lt;/span&gt; 起&lt;/p&gt;
&lt;/div&gt;
{{/each}}
</script>
<script type="text/template" id="J_aroundOtherTpl">
{{each(i, item) list}}
&lt;div class="around_item" data-uid="${uid}"&gt;
    &lt;span class="num"&gt;${i+1}&lt;/span&gt;
    {{if distance &gt; 0}}
    &lt;span class="distance"&gt;{{if distance &gt;= 1000}}&lt;span&gt;${Math.round(distance / 100) / 10}&lt;/span&gt;公里{{else}}&lt;span&gt;${distance}&lt;/span&gt;米{{/if}}&lt;/span&gt;
    {{/if}}
    &lt;p class="name" title="${name}"&gt;${name}&lt;/p&gt;
    &lt;div class="go_to" data-poi='{"name": "${name}", "pos": "${location.lng}|${location.lat}"}'&gt;
        &lt;a data-way="transfer" href="javascript:;"&gt;公交&lt;/a&gt;|&lt;a data-way="driving" href="javascript:;"&gt;驾车&lt;/a&gt;|&lt;a data-way="walking" href="javascript:;"&gt;步行&lt;/a&gt;
    &lt;/div&gt;
    &lt;p class="info"&gt;${type.split(";")[1]}&lt;/p&gt;
&lt;/div&gt;
{{/each}}
</script>
<script type="text/template" id="J_dotMarkerTpl">
&lt;div class="landmarks_click"&gt;
    &lt;a href="javascript:;" onclick="parent.CtripHotelMap.closeInfoWin('${uid}');return false;" class="landmarks_click_x"&gt;×&lt;/a&gt;
    &lt;div class="landmarks_name"&gt;${name}&lt;/div&gt;
    {{if sourceType=="hotel"}}
        &lt;div class="landmarks_xz"&gt;
            &lt;span class="hotel_diamond0${star}" title="${starDetail}"&gt;&lt;/span&gt;
            &lt;span class="score"&gt;&lt;span class="num"&gt;${score}&lt;/span&gt;分&lt;/span&gt;
        &lt;/div&gt;
    {{/if}}
    {{if sourceType=="customMarker"}}
        &lt;div class="landmarks_distance"&gt;${distance}&lt;/div&gt;
    {{else}}
        {{if distance &gt; 0}}
        &lt;div class="landmarks_distance"&gt;{{if distance &gt;= 1000}}${Math.round(distance / 100) / 10}公里{{else}}${distance}米{{/if}}&lt;/div&gt;
        {{/if}}
    {{/if}}
    {{if sourceType=="hotel"}}&lt;div class="landmarks_price"&gt;RMB&lt;span${price}&lt;/span&gt; 起&lt;/div&gt;{{/if}}
    &lt;div class="landmarks_bottom"&gt;
        {{if sourceType=="customMarker"}}&lt;a class="del" onclick="parent.CtripHotelMap.deleteInfoWin('${uid}');return false;" href="javascript:;"&gt;&lt;/a&gt;{{/if}}
        {{if sourceType=="hotel"}}&lt;a href="${url}" target="_blank" class="more"&gt;查看详情 &amp;gt;&lt;/a&gt;{{/if}}
        &lt;div class="go_to"&gt;
            &lt;a href="javascript:;" onclick="parent.CtripHotelMap.popSide.endRoute('transfer', '${name}', '${location.lng}|${location.lat}');return false;"&gt;公交&lt;/a&gt;|&lt;a onclick="parent.CtripHotelMap.popSide.endRoute('driving', '${name}', '${location.lng}|${location.lat}');return false;" href="javascript:;"&gt;驾车&lt;/a&gt;|&lt;a onclick="parent.CtripHotelMap.popSide.endRoute('walking', '${name}', '${location.lng}|${location.lat}');return false;" href="javascript:;"&gt;步行&lt;/a&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/div&gt;
</script>
<script type="text/ctrip-tpl" id="J_centerMarkerTpl">
&lt;div class="detail_map_mark"&gt;&lt;span class="ico_mark"&gt;&lt;/span&gt;&lt;div class="map_mark_inner"&gt;&lt;span class="map_mark_name"&gt;${label}&lt;/span&gt;&lt;/div&gt;&lt;/div&gt;
</script>

<script type="text/ctrip-tpl" id="J_MarkerPopTpl">
&lt;div&gt;
    &lt;span class="map_${poiType} J_poiIcon"&gt;${index+1}&lt;/span&gt;
&lt;/div&gt;
&lt;div class="landmarks_click hidden"&gt;
    &lt;a href="javascript:;" onclick="parent.$(this).parentNode().addClass('hidden');return false;" class="landmarks_click_x"&gt;×&lt;/a&gt;
    &lt;div class="landmarks_name"&gt;${name}&lt;/div&gt;
    {{if sourceType=="hotel"}}
        &lt;div class="landmarks_xz"&gt;
            &lt;span class="hotel_diamond0${star}" title="${starDetail}"&gt;&lt;/span&gt;
            &lt;span class="score"&gt;&lt;span class="num"&gt;${score}&lt;/span&gt;分&lt;/span&gt;
        &lt;/div&gt;
    {{/if}}
         {{if distance &gt; 0}}
         &lt;div class="landmarks_distance"&gt;{{if distance &gt;= 1000}}${Math.round(distance / 100) / 10}公里{{else}}${distance}米{{/if}}&lt;/div&gt;
         {{/if}}
    {{if sourceType=="hotel"}}&lt;div class="landmarks_price"&gt;RMB&lt;span${price}&lt;/span&gt; 起&lt;/div&gt;{{/if}}
    &lt;div class="landmarks_bottom"&gt;
        {{if sourceType=="hotel"}}&lt;a href="${url}" target="_blank" class="more"&gt;查看详情 &amp;gt;&lt;/a&gt;{{/if}}
        &lt;div class="go_to"&gt;
            &lt;a href="javascript:;" onclick="parent.CtripHotelMap.popSide.endRoute('transfer', '${name}', '${location.lng}|${location.lat}');return false;"&gt;公交&lt;/a&gt;|&lt;a onclick="parent.CtripHotelMap.popSide.endRoute('driving', '${name}', '${location.lng}|${location.lat}');return false;" href="javascript:;"&gt;驾车&lt;/a&gt;|&lt;a onclick="parent.CtripHotelMap.popSide.endRoute('walking', '${name}', '${location.lng}|${location.lat}');return false;" href="javascript:;"&gt;步行&lt;/a&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/div&gt;
</script>



<script type="text/ctrip-tpl" id="J_citySuggestion">
    {{if (data = Help.format(data))}}{{/if}}
    &lt;div class="city_select_lhsl"&gt;
        &lt;a class="close" href="javascript:;"&gt;×&lt;/a&gt;
        &lt;p class="title"&gt;支持中文/拼音/简拼输入&lt;/p&gt;{{tmpl searchHistoryList }}
        &lt;ul class="tab_box"&gt;{{enum(key) data}}&lt;li&gt;&lt;span&gt;${key}&lt;/span&gt;&lt;/li&gt;{{/enum}}&lt;/ul&gt;
        {{enum(key,objs) data}}
        &lt;div class="city_item"&gt;
            {{enum(k,arr) objs}}
                {{if (k)}}
                &lt;div class="city_item_in"&gt;
                    &lt;span class="city_item_letter"&gt;${k}&lt;/span&gt;
                {{else}}
                &lt;div&gt;
                {{/if}}
                {{each(index, item) arr}}&lt;a href="javascript:void(0);" data="${item.data}"&gt;${item.display}&lt;/a&gt;{{/each}}
                &lt;/div&gt;
            {{/enum}}
        &lt;/div&gt;
        {{/enum}}
    &lt;/div&gt;
</script>
<script type="text/ctrip-tpl" id="J_citySuggestionIPad">
    {{if (data = Help.format($data.data))}}{{/if}}
    &lt;div class="city_select_lhsl"&gt;
    &lt;p class="title"&gt;
        &lt;a class="close CQ_suggestionClose" href="javascript:;"&gt;&amp;times;&lt;/a&gt;&lt;/p&gt;
        &lt;div class="key_word_key"&gt;&lt;div class="CQ_suggestionKeyboard ico_key"&gt;显示键盘&lt;/div&gt;&lt;/div&gt;
        {{tmpl searchHistoryList}}
        &lt;ul class="tab_box CQ_suggestionTabContainer"&gt;
            {{enum(key) data}}
                &lt;li class="CQ_suggestionTab"&gt;&lt;span&gt;${key}&lt;/span&gt;&lt;/li&gt;
            {{/enum}}
        &lt;/ul&gt;
        {{enum(key,objs) data}}
        &lt;div class="city_item CQ_suggestionPanel"&gt;
            {{enum(k,arr) objs}}
                {{if (k)}}
                &lt;div class="city_item_in"&gt;
                    &lt;span class="city_item_letter"&gt;${k}&lt;/span&gt;
                {{else}}
                &lt;div&gt;
                {{/if}}
                {{each(index, item) arr}}&lt;a href="javascript:void(0);" data="${item.data}"&gt;${item.display}&lt;/a&gt;{{/each}}
                &lt;/div&gt;
            {{/enum}}
        &lt;/div&gt;
        {{/enum}}
     &lt;/div&gt;
</script>
<script type="text/style" id="J_citySuggestionStyle">
    .city_select_lhsl{width:408px;padding:10px;border:1px solid #999;background-color:#fff;}
    .city_select_lhsl .close{float:right;width:20px;height:20px;color:#666;text-align:center;font:bold 16px/20px Simsun;}
    .city_select_lhsl .close:hover{text-decoration:none;color:#FFA800;}
    .city_select_lhsl .title{margin-bottom:10px;color:#999;}
    .city_select_lhsl .tab_box{width:100%;height:22px;margin-bottom:6px;margin-top:0;border-bottom:2px solid #ccc;}
    .city_select_lhsl .tab_box li{position:relative;float:left;display:inline;margin-right:2px;line-height:22px;cursor:pointer;}
    .city_select_lhsl .tab_box li b{display:none;}
    .city_select_lhsl .tab_box li span{padding:0 8px;}
    .city_select_lhsl .tab_box .hot_selected{border-bottom:2px solid #06c;margin-bottom:-2px;font-weight:bold;color:#06c;}
    .city_select_lhsl .tab_box .hot_selected b{position:absolute;top:23px;left:50%;display:block;width:0;height:0;margin-left:-5px;overflow:hidden;font-size:0;line-height:0;border-color:#06c transparent transparent transparent;border-style:solid dashed dashed dashed;border-width:5px;}
    .city_select_lhsl .city_item, .city_select_lhsl .search_history_box {display:inline-block;*zoom:1;overflow:hidden;}
    .city_select_lhsl .city_item{width:408px;}
    .city_select_lhsl .city_item a, .city_select_lhsl .search_history_box a {float:left;display:inline;width:52px;height:22px;margin:0 2px 2px 0;padding-left:8px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;line-height:22px;color:#333;}
    .city_select_lhsl .city_item a:hover,.city_select_lhsl .search_history_box a:hover{background-color:#2577E3;text-decoration:none;color:#fff;}
    .city_item .city_item_in{width:378px;padding-left:30px;*zoom:1;}
    .city_item .city_item_in:after,.city_select_lhsl .search_history_box:after{display:block;height:0;visibility:hidden;overflow:hidden;content:".";clear:both;}
    .city_item .city_item_letter{float:left;width:30px;height:22px;margin-left:-30px;line-height:22px;text-align:center;color:#E56700;}
    .city_select_lhsl .sarch_history_title{margin-bottom:2px;font-weight:bold;color:#06c;}
    .city_select_lhsl .search_history_box{margin-bottom:6px;}
</script>
<script type="text/style" id="J_citySuggestionStyleIPad">
    .city_select_lhsl{position:relative;width:520px;padding:10px;border:1px solid #999;background-color:#fff;font-size:16px;}
    .key_word_key{height:48px;}
    .ico_key,.ico_unkey{width:92px;height:43px;padding-left:65px;background:url(//pic.c-ctrip.com/ctripOnPad/un_key20131012.png) 10px 11px no-repeat;cursor:pointer;line-height:40px;font-size:18px;border-width:1px;border-style:solid;border-radius:3px;}
    .ico_key{border-color:#f0f0f0 #cfcfcf #707070;box-shadow:0 1px 0 #cfcfcf,1px 0 0 0 #f0f0f0 inset,-1px 0 0 0 #f0f0f0 inset,0 -1px 0 0 #f0f0f0 inset;}
    .ico_unkey{border-color:#898989 #e2e2e2 #e2e2e2;background-color:#f5f5f5;box-shadow:0 -1px 0 #e2e2e2,0 1px 0 #d1d1d1 inset;}
    .city_select_lhsl .close{float:right;width:30px;height:30px;line-height:30px;text-align:center;color:#666;font:bold 22px/30px "Heiti SC","Heiti SC light",STHeiti,STXihei,sans-serif;}
    .city_select_lhsl .title{position:absolute;z-index:1;top:10px;right:10px;color:#999;}
    .city_select_lhsl .tab_box{height:30px;margin-bottom:10px;margin-top:0;border-bottom:2px solid #ccc;}
    .city_select_lhsl .tab_box li{position:relative;z-index:1;float:left;display:inline;margin-right:10px;line-height:30px;cursor:pointer;}
    .city_select_lhsl .tab_box li span{padding:0 8px;}
    .city_select_lhsl .tab_box .hot_selected{border-bottom:2px solid #06c;margin-bottom:-2px;font-weight:bold;color:#06c;}
    .city_select_lhsl .city_item{display:inline-block;width:520px;}
    .city_select_lhsl .city_item a,.city_select_lhsl .search_history_box a{float:left;display:inline;width:70px;height:30px;margin:0 2px 10px 0;padding-left:8px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;line-height:30px;color:#333;}
    .city_item .city_item_in{width:490px;padding-left:30px;min-height:40px;}
    .city_item .city_item_in:after{display:block;height:0;visibility:hidden;overflow:hidden;content:".";clear:both;}
    .city_item .city_item_letter{float:left;width:30px;height:30px;margin-left:-30px;line-height:30px;text-align:center;color:#E56700;}
    .city_select_lhsl .sarch_history_title{margin-bottom:10px;font-weight:bold;color:#06c;}
    .city_select_lhsl .search_history_box{margin-bottom:10px;}
    .city_select_lhsl .search_history_box:after{display:block;clear:both;visibility:hidden;overflow:hidden;height:0;content:".";}
    .city_select_lhsl .search_history_box a{margin-bottom:0;}
</script>

<script type="text/ctrip-tpl" id="J_cityFilter">
    {{if $data.hasResult}}
    &lt;div class="keyword_prompting_lhsl city_suggestion_pop"&gt;
        {{if (obj = Help.groupCityFilterData($data.list))}}{{/if}}
        {{if obj.isNewVersion }}
            &lt;p class="title"&gt;
                &lt;a class="close CQ_suggestionClose" href="javascript:;"&gt;×&lt;/a&gt;
                &lt;span class="text_input"&gt;${$data.val}，&lt;/span&gt;若需缩小范围，请输入更多条件。(酒店起价为参考价)
            &lt;/p&gt;
            {{if (list = obj.list || []).length}}
                &lt;div&gt;
                    {{each (i,item) list}}
                        &lt;div class="kw_list"&gt;
                            &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                                {{if (arr=item.data.split("|"))}}{{/if}}
                                &lt;span class="kw_sort"&gt;{{tmpl Help.getEnumItemType(arr[6])}}&lt;/span&gt;
                                {{if (arr[6] != 'Hotel' &amp;&amp; arr[3] &gt; 0) }}
                                &lt;span class="kw_number"&gt;${arr[3] &gt; 0 ? arr[3] : 0}家酒店&lt;/span&gt;
                                {{/if}}
                                &lt;div class="kw_item"&gt;
                                    {{ if arr[6] == 'District'}}
                                     &lt;p class="kw_info"&gt;{{tmpl Help.highlight(arr[1] + arr[5], $data.val, 'kw_keys')}}&lt;/p&gt;
                                    {{ else arr[6] == 'FlagShip' }}
                                    &lt;p class="kw_info"&gt;{{tmpl Help.highlight(arr[4], $data.val, 'kw_keys')}}&lt;/p&gt;
                                    {{ else}}
                                    &lt;p class="kw_info"&gt;{{tmpl Help.highlight(arr[7] + arr[5], $data.val, 'kw_keys')}}&lt;/p&gt;
                                    {{/if}}
                                    {{ if arr[6] == 'Hotel'}}
                                    &lt;p class="kw_info kw_mark"&gt;
                                        {{ if arr[11] &gt; 0 }}&lt;span class="kw_cols kw_price"&gt;&lt;dfn&gt;¥&lt;/dfn&gt;&lt;b&gt;${arr[11]}&lt;/b&gt;起&lt;/span&gt;{{/if}}
                                        {{ if arr[12] &gt; 0 }}&lt;span class="kw_cols kw_score" style="margin-right: 4px;"&gt;&lt;b&gt;${arr[12]}&lt;/b&gt;分&lt;/span&gt;{{/if}}${arr[13]}
                                    &lt;/p&gt;
                                    {{/if}}
                                &lt;/div&gt;
                            &lt;/a&gt;
                        &lt;/div&gt;
                    {{/each}}
                &lt;/div&gt;
                {{if $data.page.max&gt;0}}
                &lt;div class="c_page_mini" style="display: block;"&gt;
                    {{if $data.page.current&gt;0}}
                        &lt;a href="javascript:void(0);" page="${$data.page.current-1}"&gt;&amp;lt;-&lt;/a&gt;
                    {{/if}}
                    {{if $data.page.current&lt;2}}
                        {{loop(index) Math.min(5,$data.page.max+1)}}
                            &lt;a href="javascript:void(0);"{{if $data.page.current==index}} class="address_current"{{/if}} page="${index}"&gt;${index+1}&lt;/a&gt;
                        {{/loop}}
                    {{else $data.page.current&gt;$data.page.max-2}}
                        {{loop(index) Math.max(0,$data.page.max-4),$data.page.max+1}}
                            &lt;a href="javascript:void(0);"{{if $data.page.current==index}} class="address_current"{{/if}} page="${index}"&gt;${index+1}&lt;/a&gt;
                        {{/loop}}
                    {{else}}
                        {{loop(index) Math.max(0,$data.page.current-2),Math.min($data.page.current+3,$data.page.max+1)}}
                            &lt;a href="javascript:void(0);"{{if $data.page.current==index}} class="address_current"{{/if}} page="${index}"&gt;${index+1}&lt;/a&gt;
                        {{/loop}}
                    {{/if}}
                   {{if $data.page.current&lt;$data.page.max}}
                        &lt;a href="javascript:void(0);" page="${$data.page.current+1}"&gt;-&amp;gt;&lt;/a&gt;
                    {{/if}}
                &lt;/div&gt;
            {{/if}}
            {{/if}}
        {{else}}
            &lt;p class="title"&gt;
                &lt;a class="close CQ_suggestionClose" href="javascript:;"&gt;×&lt;/a&gt;
                &lt;span class="text_input"&gt;${$data.val}，&lt;/span&gt;若需缩小范围，请输入更多条件。
            &lt;/p&gt;
            {{if (city = obj.City || []).length}}
                &lt;div class="sug_item item_list_city"&gt;
                   {{each (i,item) city}}
                        &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                            {{if (i == 0)}}&lt;div class="sug_category"&gt;城市&lt;/div&gt;{{/if}}
                            {{if (arr=item.data.split("|"))}}{{/if}}
                            &lt;span class="city"&gt;{{tmpl Help.highlight(arr[7] + arr[5], $data.val)}}&lt;/span&gt;
                           {{if (!item.isHot)}}  &lt;span class="num"&gt;${arr[3] || 0}家{{if (item.isInn)}}客栈{{else}}酒店{{/if}}&lt;/span&gt;{{/if}}
                        &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
            {{/if}}
            {{if (district = obj.District || []).length}}
                &lt;div class="sug_item item_list_scenic"&gt;
                    {{each (i,item) district}}
                        &lt;a class="city_item" href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                            {{if (arr=item.data.split("|"))}}{{/if}}
                            {{if (i == 0)}}&lt;div class="sug_category"&gt;景区&lt;/div&gt;{{/if}}
                            &lt;span class="city"&gt;{{tmpl Help.highlight(arr[1] + arr[5], $data.val)}}&lt;/span&gt;
                            {{if (!item.isHot)}}  &lt;span class="num"&gt;${arr[3] || 0}家{{if (item.isInn)}}客栈{{else}}酒店{{/if}}&lt;/span&gt;{{/if}}
                        &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
            {{/if}}
            {{if (sight = obj.Sight || []).length}}
                &lt;div class="sug_item item_list_attractions"&gt;
                    {{each (i,item) sight}}
                        &lt;a class="city_item" href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                            {{if (i == 0)}}&lt;div class="sug_category"&gt;景点&lt;/div&gt;{{/if}}
                            {{if (arr=item.data.split("|"))}}{{/if}}
                            &lt;span class="city"&gt;{{tmpl Help.highlight(arr[7] + arr[5], $data.val)}}&lt;/span&gt;
                            {{if (!item.isHot)}}  &lt;span class="num"&gt;${arr[3] || 0}家{{if (item.isInn)}}客栈{{else}}酒店{{/if}}&lt;/span&gt;{{/if}}
                        &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
            {{/if}}
            {{if (loc = obj.Location || []).length}}
                &lt;div class="sug_item item_list_areaadmin"&gt;
                    {{each (i,item) loc}}
                        &lt;a class="city_item" href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                            {{if (i == 0)}}&lt;div class="sug_category"&gt;行政区&lt;/div&gt;{{/if}}
                            {{if (arr=item.data.split("|"))}}{{/if}}
                            &lt;span class="city"&gt;{{tmpl Help.highlight(arr[7] + arr[5], $data.val)}}&lt;/span&gt;
                            {{if (!item.isHot)}}  &lt;span class="num"&gt;${arr[3] || 0}家{{if (item.isInn)}}客栈{{else}}酒店{{/if}}&lt;/span&gt;{{/if}}
                        &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
            {{/if}}
            {{if (domesticZone = obj.DomesticZone || []).length}}
                &lt;div class="sug_item item_list_business"&gt;
                    {{each (i,item) domesticZone}}
                        &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                            {{if (i == 0)}}&lt;div class="sug_category"&gt;商业区&lt;/div&gt;{{/if}}
                            {{if (arr=item.data.split("|"))}}{{/if}}
                            &lt;span class="city"&gt;{{tmpl Help.highlight(arr[7] + arr[5], $data.val)}}&lt;/span&gt;
                            {{if (!item.isHot)}}  &lt;span class="num"&gt;${arr[3] || 0}家{{if (item.isInn)}}客栈{{else}}酒店{{/if}}&lt;/span&gt;{{/if}}
                        &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
            {{/if}}
            {{if (airport = obj.Airport || []).length}}
                &lt;div class="sug_item item_list_airport"&gt;
                    {{each (i,item) airport}}
                        &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                            {{if (i == 0)}}&lt;div class="sug_category"&gt;机场&lt;/div&gt;{{/if}}
                            {{if (arr=item.data.split("|"))}}{{/if}}
                            &lt;span class="city"&gt;{{tmpl Help.highlight(arr[7] + arr[5], $data.val)}}&lt;/span&gt;
                            {{if (!item.isHot)}}  &lt;span class="num"&gt;${arr[3] || 0}家{{if (item.isInn)}}客栈{{else}}酒店{{/if}}&lt;/span&gt;{{/if}}
                        &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
            {{/if}}
            {{if (railwayStation = obj.RailwayStation || []).length}}
                &lt;div class="sug_item item_list_train"&gt;
                    {{each (i,item) railwayStation}}
                        &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                            {{if (i == 0)}}&lt;div class="sug_category"&gt;火车站&lt;/div&gt;{{/if}}
                            {{if (arr=item.data.split("|"))}}{{/if}}
                            &lt;span class="city"&gt;{{tmpl Help.highlight(arr[7] + arr[5], $data.val)}}&lt;/span&gt;
                             {{if (!item.isHot)}} &lt;span class="num"&gt;${arr[3] || 0}家{{if (item.isInn)}}客栈{{else}}酒店{{/if}}&lt;/span&gt;{{/if}}
                        &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
            {{/if}}
            {{if (Hotel = obj.Hotel || []).length}}
                &lt;div class="sug_item item_list_hotel"&gt;
                    {{each (i,item) Hotel}}
                        &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                            {{if (i == 0)}}&lt;div class="sug_category"&gt;名称&lt;/div&gt;{{/if}}
                            {{if (arr=item.data.split("|"))}}{{/if}}
                            &lt;span class="city"&gt;{{tmpl Help.highlight(arr[7], $data.val)}}&lt;/span&gt;
                        &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
            {{/if}}
            {{if $data.page.max&gt;0}}
                &lt;div class="c_page_mini" style="display: block;"&gt;
                    {{if $data.page.current&gt;0}}
                        &lt;a href="javascript:void(0);" page="${$data.page.current-1}"&gt;&amp;lt;-&lt;/a&gt;
                    {{/if}}
                    {{if $data.page.current&lt;2}}
                        {{loop(index) Math.min(5,$data.page.max+1)}}
                            &lt;a href="javascript:void(0);"{{if $data.page.current==index}} class="address_current"{{/if}} page="${index}"&gt;${index+1}&lt;/a&gt;
                        {{/loop}}
                    {{else $data.page.current&gt;$data.page.max-2}}
                        {{loop(index) Math.max(0,$data.page.max-4),$data.page.max+1}}
                            &lt;a href="javascript:void(0);"{{if $data.page.current==index}} class="address_current"{{/if}} page="${index}"&gt;${index+1}&lt;/a&gt;
                        {{/loop}}
                    {{else}}
                        {{loop(index) Math.max(0,$data.page.current-2),Math.min($data.page.current+3,$data.page.max+1)}}
                            &lt;a href="javascript:void(0);"{{if $data.page.current==index}} class="address_current"{{/if}} page="${index}"&gt;${index+1}&lt;/a&gt;
                        {{/loop}}
                    {{/if}}
                   {{if $data.page.current&lt;$data.page.max}}
                        &lt;a href="javascript:void(0);" page="${$data.page.current+1}"&gt;-&amp;gt;&lt;/a&gt;
                    {{/if}}
                &lt;/div&gt;
            {{/if}}
            {{if (scenicList = Help.getScenic(district))}}{{/if}}
            {{if scenicList &amp;&amp; scenicList.length}}
                &lt;div class="city_scenic_pic" style="width:400px;height:298px;left:399px;"&gt;
                    {{each (i,item) scenicList}}
                        {{if (i==0)}}&lt;img src="${item.pic}" width="400" height="298"&gt;{{/if}}
                        &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}" style="position:absolute;top:${item.top}px;left:${item.left}px;text-decoration:none;"&gt;
                            &lt;div class="scenic_mark"&gt;
                                &lt;span class="scenic_map_num"&gt;&lt;/span&gt;
                                &lt;div class="scenic_mark_inner"&gt;&lt;span class="scenic_mark_name"&gt;${item.name}&lt;/span&gt;&lt;/div&gt;
                            &lt;/div&gt;
                        &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
            {{/if}}
        {{/if}}
    &lt;/div&gt;
    {{else}}
    &lt;div class="keyword_prompting_lhsl notfound_pop"&gt;
        &lt;p class="title"&gt;&lt;a class="close CQ_suggestionClose" href="javascript:;"&gt;×&lt;/a&gt;对不起，找不到：${$data.val}&lt;/p&gt;
    &lt;/div&gt;
    {{/if}}
</script>

<script type="text/style" id="J_cityFilterStyle">
    .keyword_prompting_lhsl .sug_item{padding-bottom: 5px; padding-top:5px; border-bottom: 1px solid #ccc; position:relative;*zoom:1;}
    .keyword_prompting_lhsl .sug_item a{display:block; overflow:hidden; padding:5px 7px 5px 10px; color:#333;  line-height:18px; cursor:pointer;*zoom:1;}
    .keyword_prompting_lhsl .sug_item .hover { background-color:#2577e3; color:#fff; text-decoration:none;}
    .keyword_prompting_lhsl .sug_item .hover span, .keyword_prompting_lhsl .sug_item .hover b{color:#fff;}
    .notfound_pop{ padding-bottom: 4px;}
    .notfound_pop .close{ margin-top: 2px;}
    .keyword_prompting_lhsl .text_input { float:left; max-width:160px; _width:160px; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; }
    .keyword_prompting_lhsl .sug_item a:after{ clear:both; content:'.'; display:block; height:0; overflow:hidden; }
    .keyword_prompting_lhsl .sug_item .num { float:left; width:75px; overflow: hidden; color:#999; text-align: right;}
    .keyword_prompting_lhsl .sug_item .city { display:block; float: left; width:270px; padding-right:4px; overflow:hidden;}
    .city_suggestion_pop .sug_item .city {width:195px; height:18px; white-space:nowrap; text-overflow:ellipsis;}
    .keyword_prompting_lhsl .sug_item b{font-weight:bold; color:#06c; }
    .keyword_prompting_lhsl .sug_category{ float:right; height:18px; line-height:18px; background-image:url(//pic.c-ctrip.com/hotels121118/ico_search_box_2.png); background-repeat: no-repeat;width:62px; padding-right:20px; padding-left:0; text-align:right;}
    .keyword_prompting_lhsl .sug_category_hover{ color: #fff; background-color: #2577e3; background-position: right 6px; background-color:#2577e3; }
    .keyword_prompting_lhsl .item_list_city .sug_category{background-position: right -33px;}
    .keyword_prompting_lhsl .item_list_city .hover .sug_category{background-position: right 2px;}
    .keyword_prompting_lhsl .item_list_airport .sug_category{background-position: right -105px;}
    .keyword_prompting_lhsl .item_list_airport .hover .sug_category{background-position: right -67px;}
    .keyword_prompting_lhsl .item_list_hotel .sug_category{background-position: right -170px;}
    .keyword_prompting_lhsl .item_list_hotel .hover .sug_category{background-position: right -137px;}
    .keyword_prompting_lhsl .item_list_landmarks .sug_category{background-position: right -204px;}
    .keyword_prompting_lhsl .item_list_landmarks .hover .sug_category{background-position: right -238px;}
    .keyword_prompting_lhsl .item_list_scenic .sug_category{background-position: right -271px;}
    .keyword_prompting_lhsl .item_list_scenic .hover .sug_category{background-position: right -303px;}
    .keyword_prompting_lhsl .item_list_traffic .sug_category{background-position: right -336px; padding-right:40px;}
    .keyword_prompting_lhsl .item_list_traffic .hover .sug_category{background-position: right -372px;}
    .keyword_prompting_lhsl .item_list_areaadmin .sug_category{background-position: right -410px;}
    .keyword_prompting_lhsl .item_list_areaadmin .hover .sug_category{background-position: right -447px;}
    
    .keyword_prompting_lhsl .item_list_train .sug_category{background-position: right -482px;}
    .keyword_prompting_lhsl .item_list_train .hover .sug_category{background-position: right -518px;}
    
    .keyword_prompting_lhsl .item_list_business .sug_category{background-position: right -557px;}
    .keyword_prompting_lhsl .item_list_business .hover .sug_category{background-position: right -596px;}
    
    .keyword_prompting_lhsl .item_list_attractions .sug_category{background-position: right -635px;}
    .keyword_prompting_lhsl .item_list_attractions .hover .sug_category{background-position: right -674px;}
    
    .city_suggestion_pop .sug_item .num {float:left; width:80px; overflow:hidden; color:#999; text-align:right;}
    .city_suggestion_pop .city_scenic_pic{position:absolute; border:1px solid #999; display:none;}
    .city_suggestion_pop .city_scenic_pic img{display:block;}
    .city_suggestion_pop .scenic_mark{padding-left:21px;padding-top:1px;height:27px;overflow:hidden;cursor:default;white-space:nowrap; cursor:pointer;}
    .city_suggestion_pop .scenic_mark .scenic_map_num{position:absolute;top:0;left:0;width:21px;height:27px;z-index:3;background: url(//pic.c-ctrip.com/hotels_seo/scenic_mark.png) no-repeat;_background: url(//pic.c-ctrip.com/hotels_seo/scenic_mark_ie6.png) no-repeat;}
    .city_suggestion_pop .scenic_mark .scenic_map_num_hover{background: url(//pic.c-ctrip.com/hotels_seo/scenic_mark_hover.png) no-repeat;_background: url(//pic.c-ctrip.com/hotels_seo/scenic_mark_hover_ie6.png) no-repeat;}
    .city_suggestion_pop .scenic_mark_inner{background-color:#fff;height:22px;line-height:22px;padding:0 10px 0 15px;;border:1px solid #A1A19D;border-left:0 none; border-top:none; border-top-right-radius:13px;border-bottom-right-radius:13px;box-shadow:2px 2px 2px 0 #ccc;position:relative;z-index:2;left:-10px;_display:inline; *zoom:1; color:#0f66cd; font-size:12px;}

    .keyword_prompting_lhsl{width:398px; border:1px solid #999; background-color:#fff;}
    .keyword_prompting_lhsl .title{ position: relative; margin:0 10px 4px; padding:5px 28px 5px 2px; border-bottom:1px dotted #ccc; color:#999;}
	.notfound_pop .title{ color: #c01111; border-bottom: 0 none;}
	.keyword_prompting_lhsl .close{ position: absolute; right: 0; top:50%; margin-top: -13px; width:26px; height:26px; font:bold 14px/26px Simsun; color:#666; text-align:center;}
    .keyword_prompting_lhsl .close:hover { text-decoration:none; color:#FFA800; }
    .keyword_prompting_lhsl .kw_scroll{max-height: 365px; overflow-y: auto;}
    .keyword_prompting_lhsl .kw_list:after{content: ""; display: table; clear: both;}
    .keyword_prompting_lhsl .kw_list{ border-bottom: 1px solid #eee; cursor: default;}
    .keyword_prompting_lhsl .kw_list a{ display: block; padding: 6px 10px;}
    .keyword_prompting_lhsl .kw_list a:hover,.keyword_prompting_lhsl .hover{ background-color: #2577e3; text-decoration: none;} 
	.keyword_prompting_lhsl .kw_list:hover,.keyword_prompting_lhsl .hover{background-color: #2577e3;}
    .keyword_prompting_lhsl .kw_sort{float: right; width:80px; color: #333; text-align: right; overflow: hidden; white-space: nowrap;}
    .keyword_prompting_lhsl .kw_item{ overflow: hidden;}
    .keyword_prompting_lhsl .kw_info{overflow: hidden; white-space: nowrap; text-overflow: ellipsis;}
    .keyword_prompting_lhsl .kw_keys,
    .keyword_prompting_lhsl .kw_score{color: #06c;}
    .keyword_prompting_lhsl .kw_price dfn{color: #333;}
    .keyword_prompting_lhsl .kw_price b{color: #f60;}
    .keyword_prompting_lhsl .kw_mark{color: #666;}
    .keyword_prompting_lhsl .kw_cols{display: inline-block; padding-right: 4px; border-right: 1px solid #ccc; line-height: 1.1;}
    .keyword_prompting_lhsl .kw_number{float: right; width: 100px; color: #999; text-align: right; overflow: hidden; white-space: nowrap;}
	.keyword_prompting_lhsl .kw_list:hover .kw_sort,.keyword_prompting_lhsl .hover .kw_sort,
	.keyword_prompting_lhsl .kw_list:hover .kw_info,.keyword_prompting_lhsl .hover .kw_info,
	.keyword_prompting_lhsl .kw_list:hover .kw_keys,.keyword_prompting_lhsl .hover .kw_keys,
	.keyword_prompting_lhsl .kw_list:hover .kw_score,.keyword_prompting_lhsl .hover .kw_score,
	.keyword_prompting_lhsl .kw_list:hover .kw_price dfn,.keyword_prompting_lhsl .hover .kw_price dfn,
	.keyword_prompting_lhsl .kw_list:hover .kw_price b,.keyword_prompting_lhsl .hover .kw_price b,
	.keyword_prompting_lhsl .kw_list:hover .kw_mark,.keyword_prompting_lhsl .hover .kw_mark,
	.keyword_prompting_lhsl .kw_list:hover .kw_number,.keyword_prompting_lhsl .hover .kw_number{color: #fff;}
	.keyword_prompting_lhsl .kw_list:hover .kw_cols,.keyword_prompting_lhsl .hover .kw_cols{border-right-color: #5599dd;}
    .keyword_prompting_lhsl .kw_msg{margin-top: -1px; padding: 5px 10px; border-top: 1px solid #ccc; background-color: #f3f3f3;}
    .keyword_prompting_lhsl .c_page_mini { font: 12px/1.5 arial; margin:-1px 0 0; padding:6px 0; text-align: center; background:#fff; position:relative;}
    .keyword_prompting_lhsl .c_page_mini a {display: inline-block; margin: 0;color: #06c;padding: 0 6px;font:14px/1.5 Tahoma, Arial, Simsun, sans-serif;text-decoration: underline;}
    .keyword_prompting_lhsl .c_page_mini .c_page_mini_current{ color: #666;text-decoration: none;cursor: default;}
    .keyword_prompting_lhsl .kw_list a { text-decoration: none; color: #333;}
</script>

<script type="text/ctrip-tpl" id="J_keywordSuggestion">
    {{if (data)}}
    &lt;div class="c_address_box key_word_lhsl"&gt;
        &lt;a href="javascript:;" class="close CQ_suggestionClose"&gt;×&lt;/a&gt;
        {{enum(key, item) data}}
            {{if key==="subCity"}}
                &lt;div class="keyword_sub_city"&gt;
                    ${item.cnname}：{{if (item.data)}}{{each item.data}}&lt;a href="/{{if (searchOptions.isInn)}}inn{{else}}hotel{{/if}}/${ename}${id}" class="subCity" data-dopost="T"&gt;${name}&lt;/a&gt;{{/each}}{{/if}}
                &lt;/div&gt;
            {{else}}
                &lt;dl class="key_word_list"&gt;
                    &lt;dt&gt;${item.cnname}&lt;/dt&gt;
                    &lt;dd&gt;{{if (item.data)}}{{each item.data}}&lt;a href="javascript:void(0);" data="|${name}|${id}|${type}|" data-category="${key}"&gt;${name}&lt;/a&gt;{{/each}}{{/if}}&lt;/dd&gt;
                &lt;/dl&gt;
            {{/if}}
        {{/enum}}
    &lt;/div&gt;
    {{/if}}
</script>
<script type="text/ctrip-tpl" id="J_keywordSuggestionIPad">
    &lt;div class="c_address_box key_word_lhsl key_word_lhsl_pad"&gt;
        &lt;a href="javascript:;" class="close CQ_suggestionClose"&gt;&amp;times;&lt;/a&gt;
        &lt;div class="key_word_key"&gt;&lt;div class="ico_key CQ_suggestionKeyboard"&gt;显示键盘&lt;/div&gt;&lt;/div&gt;
        {{if ($data.data)}}
        {{enum(key, item) $data.data}}
            {{if key==="subCity"}}
            &lt;div class="keyword_sub_city"&gt;
                ${item.cnname}：{{if (item.data)}}{{each (key, it) item.data}}&lt;a href="/{{if (searchOptions.isInn)}}inn{{else}}hotel{{/if}}/${it.ename}${it.id}" class="subCity" data-dopost="T"&gt;${it.name}&lt;/a&gt;{{/each}}{{/if}}
            &lt;/div&gt;
            {{else}}
            &lt;dl class="key_word_list"&gt;
                &lt;dt&gt;${item.cnname}&lt;/dt&gt;
                &lt;dd&gt;{{if (item.data)}}{{each (key, it) item.data}}&lt;a href="javascript:void(0);" data="|${it.name}|${it.id}|${it.type}|" data-category="${it.key}"&gt;${it.name}&lt;/a&gt;{{/each}}{{/if}}&lt;/dd&gt;
            &lt;/dl&gt;
            {{/if}}
        {{/enum}}
        {{/if}}
    &lt;/div&gt;
</script>
<script type="text/style" id="J_keywordSuggestionStyle">
    .key_word_lhsl { width:498px; padding:8px 10px; border:1px solid #999; background-color:#fff; }
    .key_word_key{display:none;height:30px;}
    .ico_key,.ico_unkey{ width:39px; height:25px; background:url(//pic.c-ctrip.com/ctripOnPad/un_key.png) no-repeat; -webkit-transform:scale(.7);margin-left:-5px;cursor:pointer;}
    .key_word_lhsl .close { float:right; width:20px; height:20px; color:#666; text-align:center; font:bold 16px/20px Simsun; }
    .key_word_lhsl .close:hover { text-decoration:none; color:#FFA800; }
    .key_word_lhsl .key_word_list { margin-bottom:6px; }
    .key_word_lhsl .key_word_list dt { font-weight:bold; }
    .key_word_lhsl .key_word_list dd { display:inline-block; }
    .key_word_lhsl .key_word_list dd {display:block;overflow:hidden;}
    .key_word_lhsl .key_word_list a { float:left; height:22px; padding:0 15px 0 5px; border:1px solid #fff; line-height:22px; white-space:nowrap; color:#333;}
    .key_word_lhsl .key_word_list a:hover { border:1px solid #2577e3; background-color:#2577e3; text-decoration:none; color:#fff;}
    .key_word_lhsl .keyword_sub_city { margin:0 -10px -8px; padding:5px 10px; border-top:1px solid #CCC; background-color:#F3F3F3; color:#333; }
    .key_word_lhsl .keyword_sub_city a { margin-right:10px; color:#4D4D4D; }
    .key_word_lhsl_pad .key_word_key { display:block; }


</script>
<script type="text/style" id="J_keywordSuggestionStyleIPad">
    .key_word_lhsl{position:relative;width:498px;padding:8px 10px;border:1px solid #999;background-color:#fff;font-size:16px;}
    .key_word_key{height:48px;}
    .ico_key,.ico_unkey{width:92px;height:43px;padding-left:65px;background:url(//pic.c-ctrip.com/ctripOnPad/un_key20131012.png) 10px 11px no-repeat;cursor:pointer;line-height:40px;font-size:18px;border-width:1px;border-style:solid;border-radius:3px;}
    .ico_key{border-color:#f0f0f0 #cfcfcf #707070;box-shadow:0 1px 0 #cfcfcf,1px 0 0 0 #f0f0f0 inset,-1px 0 0 0 #f0f0f0 inset,0 -1px 0 0 #f0f0f0 inset;}
    .ico_unkey{border-color:#898989 #e2e2e2 #e2e2e2;background-color:#f5f5f5;box-shadow:0 -1px 0 #e2e2e2,0 1px 0 #d1d1d1 inset;}
    .key_word_lhsl .close{position:absolute;top:10px;right:10px;width:30px;height:30px;line-height:30px;text-align:center;color:#666;font:bold 22px/30px "Heiti SC","Heiti SC light",STHeiti,STXihei,sans-serif;}
    .key_word_lhsl .key_word_list{margin-bottom:6px;}
    .key_word_lhsl .key_word_list dt{margin-bottom:10px;font-weight:bold;}
    .key_word_lhsl .key_word_list dd{display:inline-block;}
    .key_word_lhsl .key_word_list dd{display:block;overflow:hidden;}
    .key_word_lhsl .key_word_list a{float:left;height:30px;padding:0 8px;margin-right:2px;margin-bottom:10px;line-height:30px;color:#333;white-space:nowrap;}
    .key_word_lhsl .keyword_sub_city{margin:0 -10px -8px;padding:5px 10px;border-top:1px solid #CCC;background-color:#F3F3F3;color:#333;}
    .key_word_lhsl .keyword_sub_city a{margin-right:10px;color:#4D4D4D;}
    .key_word_lhsl_pad .key_word_key{display:block;}
</script>

<script type="text/ctrip-tpl" id="J_keywordFilterNew">
    {{if ($data.hasResult &amp;&amp; (result = cQuery.groupHotelMarkerData($data.list)))}}
        {{if result.isNewVersion }}
            &lt;div class="keyword_prompting_lhsl"&gt;
                &lt;p class="title"&gt;
                    &lt;a class="close CQ_suggestionClose" href="javascript:;"&gt;×&lt;/a&gt;
                    &lt;span class="text_input"&gt;${$data.val}，&lt;/span&gt;若需缩小范围，请输入更多条件。(酒店起价为参考价)
                &lt;/p&gt;
                {{if (filterlist = result.filterResult)}}{{/if}}
                {{if (filterlist || []).length}}
                    &lt;div&gt;
                        {{each (i, list) filterlist}}
                            {{if (i === 1)}}&lt;div class="kw_msg"&gt;以下为您展示其他城市的查询结果&lt;/div&gt;{{/if}}
                            {{each (i,item) list}}
                                &lt;div class="kw_list"&gt;
                                    &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rank="${i+1}"&gt;
                                        {{if (arr=item.data.split("|"))}}{{/if}}
                                        &lt;span class="kw_sort"&gt;{{tmpl Help.getEnumItemType(arr[3])}}&lt;/span&gt;
                                        &lt;div class="kw_item"&gt;
                                            {{ if arr[3] == 'FlagShip' }}
                                             &lt;p class="kw_info"&gt;{{tmpl Help.highlight(arr[1], $data.val, 'kw_keys')}}&lt;/p&gt;
                                            {{ else}}
                                             &lt;p class="kw_info"&gt;{{tmpl Help.highlight(arr[13] + arr[14], $data.val, 'kw_keys')}}&lt;/p&gt;
                                            {{/if}}
                                            {{ if arr[3] == 'Hotel'}}
                                            &lt;p class="kw_info kw_mark"&gt;
                                                {{ if arr[9] &gt; 0 }}&lt;span class="kw_cols kw_price"&gt;&lt;dfn&gt;¥&lt;/dfn&gt;&lt;b&gt;${arr[9]}&lt;/b&gt;起&lt;/span&gt;{{/if}}
                                                {{ if arr[11] &gt; 0 }}&lt;span class="kw_cols kw_score" style="margin-right: 4px;"&gt;&lt;b&gt;${arr[11]}&lt;/b&gt;分&lt;/span&gt;{{/if}}${arr[12]}
                                            &lt;/p&gt;
                                            {{/if}}
                                        &lt;/div&gt;
                                    &lt;/a&gt;
                                &lt;/div&gt;
                            {{/each}}
                        {{/each}}
                    &lt;/div&gt;
                {{/if}}
            &lt;/div&gt;
        {{else}}
            {{if (filterlist = result.filterResult)}}{{/if}}
            {{if (filterlist.length)}}
            &lt;div class="keyword_prompting_lhsl"&gt;
                &lt;p class="title"&gt;&lt;a class="close CQ_suggestionClose" href="javascript:;"&gt;×&lt;/a&gt;&lt;span class="text_input"&gt;${$data.val}，&lt;/span&gt;若需缩小范围，请输入更多条件。&lt;/p&gt;
                {{each (i, newlist) filterlist}}
                {{if (i === 1)}}&lt;div style="color:#333;background-color:#f3f3f3;padding:3px 7px;"&gt;以下为您展示其他城市的查询结果&lt;/div&gt;{{/if}}
                {{if ((names = newlist.name).length)}}
                &lt;div class="sug_item item_list_hotel"&gt;
                    {{each (i,item) names}}
                    &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rankindex="${item.rankindex}" data-rank="${i+1}"&gt;
                        {{if (i==0)}}&lt;div class="sug_category"&gt;名称&lt;/div&gt;{{/if}}
                        {{if (txt=cQuery.highlightKeyword(item.right, cQuery.keywordFilterHighlights[$data.val])) }}&lt;span class="city"&gt;${txt}&lt;/span&gt;{{/if}}
                    &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
                {{/if}}
                {{if ((districts = newlist.district).length)}}                                                                                                 
                &lt;div class="sug_item item_list_scenic"&gt;                                                                                                     
                    {{each (i,item) districts}}                                                                                                               
                    &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rankindex="${item.rankindex}" data-rank="${i+1}"&gt;                                                                 
                        {{if (i==0)}}&lt;div class="sug_category"&gt;景区&lt;/div&gt;{{/if}}                                                                       
                        {{if (txt=cQuery.highlightKeyword(item.right, cQuery.keywordFilterHighlights[$data.val])) }}&lt;span class="city"&gt;${txt}&lt;/span&gt;{{/if}}  
                        &lt;span class="num"&gt;${item.data.split("|")[5] || 0}家酒店&lt;/span&gt;
                    &lt;/a&gt;                                                                                                                                     
                    {{/each}}                                                                                                                                
                &lt;/div&gt;                                                                                                                                       
                {{/if}}       

                {{if ((stations = newlist.station).length)}}
                &lt;div class="sug_item item_list_traffic"&gt;
                    {{each (i,item) stations}}
                    &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rankindex="${item.rankindex}" data-rank="${i+1}"&gt;
                        {{if (i==0)}}&lt;div class="sug_category"&gt;机场火车站&lt;/div&gt;{{/if}}
                        {{if (txt=cQuery.highlightKeyword(item.right, cQuery.keywordFilterHighlights[$data.val])) }}&lt;span class="city"&gt;${txt}&lt;/span&gt;{{/if}}
                    &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
                {{/if}}
                {{if ((positions = newlist.position).length)}}
                &lt;div class="sug_item item_list_landmarks"&gt;
                    {{each (i,item) positions}}
                    &lt;a href="javascript:;" data="${item.data}" data-yindex="${item.yindex}" data-rankindex="${item.rankindex}" data-rank="${i+1}"&gt;
                        {{if (i==0)}}&lt;div class="sug_category"&gt;位置&lt;/div&gt;{{/if}}
                        {{if (txt=cQuery.highlightKeyword(item.right, cQuery.keywordFilterHighlights[$data.val])) }}&lt;span class="city"&gt;${txt}&lt;/span&gt;{{/if}}
                    &lt;/a&gt;
                    {{/each}}
                &lt;/div&gt;
                {{/if}}
                {{/each}}
            &lt;/div&gt;
            {{/if}}
        {{/if}}
    {{else}}
    &lt;div class="keyword_prompting_lhsl notfound_pop"&gt;
        &lt;p class="title"&gt;&lt;a class="close CQ_suggestionClose" href="javascript:;"&gt;×&lt;/a&gt;对不起，找不到：${$data.val}&lt;/p&gt;
    &lt;/div&gt;
    {{/if}}
</script>
<script type="text/style" id="J_keywordFilterStyleNew">
    .keyword_prompting_lhsl .sug_item{overflow:hidden;padding-bottom: 5px; padding-top:5px; border-bottom: 1px solid #ccc;*zoom:1;}                           
    .keyword_prompting_lhsl .sug_item a{display:block; overflow:hidden; padding:5px 7px 5px 10px; color:#333;  line-height:18px; cursor:pointer;*zoom:1;}     
    .keyword_prompting_lhsl .sug_item .hover { background-color:#2577e3; color:#fff; text-decoration:none;}                                                   
    .keyword_prompting_lhsl .sug_item .hover span, .keyword_prompting_lhsl .sug_item .hover b{color:#fff;}                                                    
    .notfound_pop{ padding-bottom: 4px;}                                                                                                                      
    .keyword_prompting_lhsl .sug_item .b{font-weight:bold; color:#06c; }                       
    .notfound_pop .close{ margin-top: 2px;}                                                                                                                   
    .keyword_prompting_lhsl .text_input { float:left; max-width:160px; _width:160px; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; }           
    .keyword_prompting_lhsl .sug_item a:after{ clear:both; content:"."; display:block; height:0; overflow:hidden; }                                           
    .keyword_prompting_lhsl .sug_item .num { float:left; width: 80px; overflow: hidden; color:#999; text-align: right;}                                       
    .keyword_prompting_lhsl .sug_item .city { display:block; float: left; width:260px; padding-right:4px; overflow:hidden; }                                  
    .keyword_prompting_lhsl .item_list_scenic .city {width:195px;}                                                                                            
    .keyword_prompting_lhsl .sug_item b{font-weight:bold; color:#06c; }                                                                                       
    .keyword_prompting_lhsl .sug_category{ float:right; height:18px; line-height:18px; background-image:url(//pic.c-ctrip.com/hotels121118/ico_search_box_1.png); background-repeat: no-repeat;width:62px; padding-right:20px; padding-left:0; text-align:right;}
    .keyword_prompting_lhsl .sug_category_hover{ color: #fff; background-color: #2577e3; background-position: right 6px; background-color:#2577e3; }          
    .keyword_prompting_lhsl .item_list_city .sug_category{background-position: right -33px;}                                                                  
    .keyword_prompting_lhsl .item_list_city .hover .sug_category{background-position: right 2px;}
    .keyword_prompting_lhsl .item_list_hotel .sug_category{background-position: right -170px;}
    .keyword_prompting_lhsl .item_list_hotel .hover .sug_category{background-position: right -137px;}                                                            
    .keyword_prompting_lhsl .item_list_landmarks .sug_category{background-position: right -204px;}                                                            
    .keyword_prompting_lhsl .item_list_landmarks .hover .sug_category{background-position: right -238px;}                                                     
    .keyword_prompting_lhsl .item_list_scenic .sug_category{background-position: right -271px;} 
    .keyword_prompting_lhsl .item_list_scenic .hover .sug_category{background-position: right -303px;} 
    .keyword_prompting_lhsl .item_list_traffic .sug_category{background-position: right -336px; padding-right:40px;}                                          
    .keyword_prompting_lhsl .item_list_traffic .hover .sug_category{background-position: right -372px;}   

    .keyword_prompting_lhsl{width:398px; border:1px solid #999; background-color:#fff;}
	.keyword_prompting_lhsl .title{ position: relative; margin:0 10px 4px; padding:5px 28px 5px 2px; border-bottom:1px dotted #ccc; color:#999;}
	.notfound_pop .title{ color: #c01111; border-bottom: 0 none;}
	.keyword_prompting_lhsl .close{ position: absolute; right: 0; top:50%; margin-top: -13px; width:26px; height:26px; font:bold 14px/26px Simsun; color:#666; text-align:center;}
    .keyword_prompting_lhsl .close:hover { text-decoration:none; color:#ffa800; }
    .keyword_prompting_lhsl .kw_scroll{max-height: 365px; overflow-y: auto;}
    .keyword_prompting_lhsl .kw_list:after{content: ""; display: table; clear: both;}
    .keyword_prompting_lhsl .kw_list {border-bottom: 1px solid #eee; cursor: default; *zoom: 1;}
    .keyword_prompting_lhsl .kw_list a{ display: block; padding: 6px 10px;}
    .keyword_prompting_lhsl .kw_list a:hover,.keyword_prompting_lhsl .hover{ background-color: #2577e3; text-decoration: none;} 
	.keyword_prompting_lhsl .kw_list:hover,.keyword_prompting_lhsl .hover{background-color: #2577e3;}
    .keyword_prompting_lhsl .kw_sort{float: right; width:80px; color: #333; text-align: right; overflow: hidden; white-space: nowrap;}
    .keyword_prompting_lhsl .kw_item{ overflow: hidden;}
    .keyword_prompting_lhsl .kw_info{overflow: hidden; white-space: nowrap; text-overflow: ellipsis;}
    .keyword_prompting_lhsl .kw_keys,
    .keyword_prompting_lhsl .kw_score{color: #06c;}
    .keyword_prompting_lhsl .kw_price dfn{color: #333;}
    .keyword_prompting_lhsl .kw_price b{color: #f60;}
    .keyword_prompting_lhsl .kw_mark{color: #666;}
    .keyword_prompting_lhsl .kw_cols{display: inline-block; padding-right: 4px; border-right: 1px solid #ccc; line-height: 1.1;}
    .keyword_prompting_lhsl .kw_number{float: right; width: 100px; color: #999; text-align: right; overflow: hidden; white-space: nowrap;}
    .keyword_prompting_lhsl .kw_list:hover .kw_sort,.keyword_prompting_lhsl .hover .kw_sort,
	.keyword_prompting_lhsl .kw_list:hover .kw_info,.keyword_prompting_lhsl .hover .kw_info,
	.keyword_prompting_lhsl .kw_list:hover .kw_keys,.keyword_prompting_lhsl .hover .kw_keys,
	.keyword_prompting_lhsl .kw_list:hover .kw_score,.keyword_prompting_lhsl .hover .kw_score,
	.keyword_prompting_lhsl .kw_list:hover .kw_price dfn,.keyword_prompting_lhsl .hover .kw_price dfn,
	.keyword_prompting_lhsl .kw_list:hover .kw_price b,.keyword_prompting_lhsl .hover .kw_price b,
	.keyword_prompting_lhsl .kw_list:hover .kw_mark,.keyword_prompting_lhsl .hover .kw_mark,
	.keyword_prompting_lhsl .kw_list:hover .kw_number,.keyword_prompting_lhsl .hover .kw_number{color: #fff;}
	.keyword_prompting_lhsl .kw_list:hover .kw_cols,.keyword_prompting_lhsl .hover .kw_cols{border-right-color: #5599dd;}
    .keyword_prompting_lhsl .kw_msg{margin-top: -1px; padding: 5px 10px; border-top: 1px solid #ccc; background-color: #f3f3f3;}
    .keyword_prompting_lhsl .kw_list a { text-decoration: none; color: #333;}
</script>
<script type="text/style" id="J_keywordFilterStyleIPadNew">
    .keyword_prompting_lhsl .sug_item{overflow:hidden;padding-bottom: 5px; padding-top:5px; border-bottom: 1px solid #ccc;}                                   
    .keyword_prompting_lhsl .sug_item a{display:block; overflow:hidden; padding:5px 7px 5px 10px; color:#333;  line-height:24px; cursor:pointer;}                                                     
    .notfound_pop .close{ margin-top: 2px;}                                                                                                                   
    .keyword_prompting_lhsl .text_input { float:left; max-width:210px; _width:210px; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; }           
    .keyword_prompting_lhsl .sug_item a:after{ clear:both; content:"."; display:block; height:0; overflow:hidden; }                                           
    .keyword_prompting_lhsl .sug_item .num { float:left; width: 90px; overflow: hidden; color:#999; text-align: right;}                                       
    .keyword_prompting_lhsl .sug_item .city { display:block; float: left; width:300px; padding-right:4px; overflow:hidden; }                                  
    .keyword_prompting_lhsl .item_list_scenic .city {width:199px;}                                                                                            
    .keyword_prompting_lhsl .sug_item b{font-weight:bold; color:#06c; }                                                                                       
    .keyword_prompting_lhsl .sug_item .b{font-weight:bold; color:#06c; }                                                                                      
    .keyword_prompting_lhsl .sug_category{ float:right; height:24px; line-height:24px; background-image:url(//pic.c-ctrip.com/hotels121118/ico_search_box_1.png); background-repeat: no-repeat;width:85px; padding-right:20px; padding-left:0; text-align:right;}
    .keyword_prompting_lhsl .item_list_hotel .sug_category{background-position: right -170px;}
    .keyword_prompting_lhsl .item_list_hotel .hover .sug_category{background-position: right -137px;}
    .keyword_prompting_lhsl .item_list_city .sug_category{background-position: right -30px;}                                                                  
    .keyword_prompting_lhsl .item_list_scenic .sug_category{background-position: right -271px;} 
    .keyword_prompting_lhsl .item_list_scenic .hover .sug_category{background-position: right -303px;} 
    .keyword_prompting_lhsl .item_list_landmarks .sug_category{background-position: right -201px;}                                                            
    .keyword_prompting_lhsl .item_list_traffic .sug_category{background-position: right -333px; padding-right:40px;}

    .keyword_prompting_lhsl{width:520px; border:1px solid #999; background-color:#fff;}
	.keyword_prompting_lhsl .title{ position: relative; margin:0 10px 4px; padding:5px 28px 5px 2px; border-bottom:1px dotted #ccc; color:#999;}
	.notfound_pop .title{ color: #c01111; border-bottom: 0 none;}
	.keyword_prompting_lhsl .close{ position: absolute; right: 0; top:50%; margin-top: -13px; width:26px; height:26px; font:bold 14px/26px Simsun; color:#666; text-align:center;}
    .keyword_prompting_lhsl .close:hover { text-decoration:none; color:#ffa800; }
    .keyword_prompting_lhsl{width:450px; border:1px solid #999; background-color:#fff;}                               
    .keyword_prompting_lhsl .title{height:30px; margin:0 10px 4px; padding:0 2px; border-bottom:1px dotted #ccc; line-height:30px; color:#999;}               
    .keyword_prompting_lhsl .close{float:right; width:26px; height:30px;  font: bold 22px/30px "Heiti SC","Heiti SC light",STHeiti,STXihei,sans-serif; color:#666; text-align:center;} 
    .keyword_prompting_lhsl .kw_scroll{max-height: 365px; overflow-y: auto;}
    .keyword_prompting_lhsl .kw_list:after{content: ""; display: table; clear: both;}
    .keyword_prompting_lhsl .kw_list {border-bottom: 1px solid #eee; cursor: default; *zoom: 1;}
    .keyword_prompting_lhsl .kw_list a{ display: block; padding: 6px 10px;}
    .keyword_prompting_lhsl .kw_list a:hover,.keyword_prompting_lhsl .hover{ background-color: #2577e3; text-decoration: none;} 
	.keyword_prompting_lhsl .kw_list:hover,.keyword_prompting_lhsl .hover{background-color: #2577e3;}
    .keyword_prompting_lhsl .kw_sort{float: right; width: 80px; color: #333; text-align: right; overflow: hidden; white-space: nowrap;}
    .keyword_prompting_lhsl .kw_item{overflow: hidden;}
    .keyword_prompting_lhsl .kw_info{overflow: hidden; white-space: nowrap; text-overflow: ellipsis;}
    .keyword_prompting_lhsl .kw_keys,
    .keyword_prompting_lhsl .kw_score{color: #06c;}
    .keyword_prompting_lhsl .kw_price dfn{color: #333;}
    .keyword_prompting_lhsl .kw_price b{color: #f60;}
    .keyword_prompting_lhsl .kw_mark{color: #666;}
    .keyword_prompting_lhsl .kw_cols{display: inline-block; padding-right: 4px; border-right: 1px solid #ccc; line-height: 1.1;}
    .keyword_prompting_lhsl .kw_number{float: right; width: 100px; color: #999; text-align: right; overflow: hidden; white-space: nowrap;}
	.keyword_prompting_lhsl .kw_list:hover .kw_sort,.keyword_prompting_lhsl .hover .kw_sort,
	.keyword_prompting_lhsl .kw_list:hover .kw_info,.keyword_prompting_lhsl .hover .kw_info,
	.keyword_prompting_lhsl .kw_list:hover .kw_keys,.keyword_prompting_lhsl .hover .kw_keys,
	.keyword_prompting_lhsl .kw_list:hover .kw_score,.keyword_prompting_lhsl .hover .kw_score,
	.keyword_prompting_lhsl .kw_list:hover .kw_price dfn,.keyword_prompting_lhsl .hover .kw_price dfn,
	.keyword_prompting_lhsl .kw_list:hover .kw_price b,.keyword_prompting_lhsl .hover .kw_price b,
	.keyword_prompting_lhsl .kw_list:hover .kw_mark,.keyword_prompting_lhsl .hover .kw_mark,
	.keyword_prompting_lhsl .kw_list:hover .kw_number,.keyword_prompting_lhsl .hover .kw_number{color: #fff;}
	.keyword_prompting_lhsl .kw_list:hover .kw_cols,.keyword_prompting_lhsl .hover .kw_cols{border-right-color: #5599dd;}
    .keyword_prompting_lhsl .kw_msg{margin-top: -1px; padding: 5px 10px; border-top: 1px solid #ccc; background-color: #f3f3f3;}
    .keyword_prompting_lhsl .kw_list a { text-decoration: none; color: #333;}
</script>


<script type="text/javascript">
    // 跨城市的景区
    var ScenicData = {
        "D10264_21001": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_bs.jpg",
            "top": 76,
            "left": 250,
            "name": "坝上，克什克腾旗"
        },
        "D10072_7840": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_bs.jpg",
            "top": 192,
            "left": 155,
            "name": "坝上，沽源"
        },
        "D10072_20914": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_bs.jpg",
            "top": 145,
            "left": 260,
            "name": "坝上，围场"
        },
        "D10072_1474": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_bs.jpg",
            "top": 235,
            "left": 248,
            "name": "坝上，丰宁"
        },
        "D10072_21790": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_bs.jpg",
            "top": 215,
            "left": 78,
            "name": "坝上，张北"
        },

        "91": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_jzg.jpg",
            "top": 64,
            "left": 267,
            "name": "九寨沟，阿坝"
        },
        "D25_1372": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_jzg.jpg",
            "top": 154,
            "left": 241,
            "name": "九寨沟，松潘"
        },

        "D105_37": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_hgh.jpg",
            "top": 156,
            "left": 92,
            "name": "泸沽湖，丽江"
        },

        "D10322_21433": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_ms.jpg",
            "top": 162,
            "left": 137,
            "name": "莽山，宜章"
        },
        "D10322_612": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_ms.jpg",
            "top": 205,
            "left": 139,
            "name": "莽山，郴州"
        },

        "D281_7807": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_qhh.jpg",
            "top": 74,
            "left": 204,
            "name": "青海湖，海北"
        },
        "D281_7752": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_qhh.jpg",
            "top": 162,
            "left": 326,
            "name": "青海湖，海东"
        },
        "D281_7794": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_qhh.jpg",
            "top": 234,
            "left": 115,
            "name": "青海湖，海南"
        },

        "D10215_3886": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_cbs.jpg",
            "top": 174,
            "left": 214,
            "name": "长白山池西，白山"
        },
        "D10216_1466": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_cbs.jpg",
            "top": 118,
            "left": 238,
            "name": "长白山池北，安图"
        },
        "D2603_13": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_th.jpg",
            "top": 98,
            "left": 155,
            "name": "太湖，无锡"
        },
        "D2603_14": {
            "pic": "//pic.c-ctrip.com/hotels_seo/scenic_th.jpg",
            "top": 158,
            "left": 181,
            "name": "太湖，苏州"
        }
    };
</script>

<div class="pop-box pop-reminder" id="J_memberLoginStatus" style="display:none">
<div class="pop-hd"><a class="c_close" href="javascript:;">×</a>温馨提示</div>
	<div class="pop-bd">
	您已享受过华住首住特惠活动，请更换预订其他房型
	</div>
	<div class="pop-ft"><a class="btn" href="javascript:;">知道了</a></div>
</div>
<div class="compare_fail_pop" style="display:none">
	<div class="compare_pop_hd"><a class="close" href="javascript:;">×</a><span class="state">Powered by Brandwisdom</span><span class="J_hotelName"></span><span class="tips">-房型均可直接预订,携程保障,全程无忧</span></div>
    <div class="compare_pop_bd"><div class="compare_pop_fail"><i></i>数据加载失败，请稍后再试。</div></div>
</div>
<div class="compare_pop" style="display:none">
	<div class="compare_pop_hd"><a class="close" href="javascript:;">×</a><span class="state">Powered by Brandwisdom</span><span class="J_hotelName"></span><span class="tips">-房型均可直接预订,携程保障,全程无忧</span></div>
    <div class="compare_pop_bd"><div class="compare_pop_loading"><i></i>查询中，请稍候......</div></div>
</div>
<div class="comment_show_pop hidden">
<div class="pic">
<img class="p" src="//pic.c-ctrip.com/common/pic_alpha.gif" alt="" />
<div class="prev hover"><b></b></div>
<div class="next"><b></b></div>
<a href="javascript:;" class="close">×</a>
<span class="d hidden">照片审核未通过</span>
<span class="d hidden">照片审核中</span>
</div>
</div>

<div id="popComboPic" style="display:none;" class="recommend_jj_pop"><div class="pic"><img class="p" src="//pic.c-ctrip.com/common/pic_alpha.gif" width="300" height="225" /></div></div>
<div id="popTopPic" class="hotel_pic_top" style="position:absolute;display:none;"><img src="//pic.c-ctrip.com/common/pic_alpha.gif" onerror="this.src='//pic.c-ctrip.com/hotels121118/bg_nopic2.png';" /></div>

<div id="popCommentPic" class="comment_pic_big_new" style="position:absolute;display:none;"><div class="pic_box_big"><img src="//pic.c-ctrip.com/common/pic_alpha.gif" /></div><p></p></div>

<div id="popRoomPic" class="hotel_pic_room" style="position:absolute;display:none;"><img src="//pic.c-ctrip.com/common/pic_alpha.gif" /></div>


<script src="//webresource.c-ctrip.com/ResHotelOnline/R8/search/js.min/jquery/1.8.3/jquery.min.js?releaseno=2018-09-20-02-02-00" onload="jQuery.noConflict();"></script>
<script src="//webresource.c-ctrip.com/ResHotelOnline/R8/search/js.min/jquery/jqueryextend/jquery.qrcode.min.js?releaseno=2018-09-20-02-02-00"></script>
            
<!--[if lte IE 9]>
<script src="//webresource.c-ctrip.com/ResHotelOnline/R8/search/js.min/jquery/jqueryextend/jquery.xdomainrequest.min.js?releaseno=2018-09-20-02-02-00"></script>
<![endif]-->
<script src="//webresource.c-ctrip.com/ares/basebiz/accountsresource/~0.0.5/default/js/module/rn_seed.js?expires=1d" capdomain="" id="crealname" charset="UTF-8"></script>
<script type="text/javascript">
    var isShowComboInfo = false;
    function bindCommentLst(type) {
        location.href = "/hotel/dianping/428365_p1t" + type + ".html";
    }
    
    function commentsubmit(obj) {
        var a = obj.id;
        if (document.getElementById("__SSO_iframe_0")) {
            document.getElementById("__SSO_iframe_0").src = "/Domestic/LoginCheck.aspx?a=" + a + "&amp;t=0&amp;b=C6023559E1443B966993539FA4A1C272";
        }
    }

    function repaint() {
        if (Raphael != undefined) {
            $('.J_bp svg').remove();
            $('.J_bp shape').parentNode().remove(); //for IE7
            $('.J_bp').each(function(item,idx){
                var fn = eval("(" + $(item).attr("params") + ")");
                fn &amp;&amp; fn.data &amp;&amp; fn.data();
            })
        }
    }
</script>
<script type="text/javascript">
    function errorRoomImg(obj) { obj.src = '//pic.c-ctrip.com/hotels121118/bg_nopic1.png'; obj.removeAttribute('_src'); }
    function errorComImg(obj) { obj.src = '//pic.c-ctrip.com/hotels121118/bg_nopic3.png'; obj.removeAttribute('_src'); }
</script>
<script type="text/javascript">
    
        function F7c1b5a99e3c149128375f6fe319b6310(fn){
            var key = "";
            if(typeof fn === "function") {
                key = fn();
            }
            key = key.substr(0, 13);

            if(key === "0a432bccbc582"){
                var tracker = document.getElementById("ab_testing_tracker");
                tracker.value = "M:21,161214_hod_lhlz:B;M:60,180522_hod_onsz:B";
            }
        }
        
        eval(function(arr,f){if(typeof Array.prototype.map==="function"){return arr.map(f)}var res=[],j=0;for(var i=0,l=arr.length;i&lt;l;i++){res[j++]=f(arr[i],i,arr)}return res}([38664,38638,38707,38722,38715,38704,38721,38710,38716,38715,38645,38646,38728,38637,38637,38637,38637,38723,38702,38719,38637,38709,38707,38720,38713,38702,38725,38725,38716,38725,38702,38723,38722,38707,38708,38718,38714,38711,38718,38721,38712,38637,38666,38637,38705,38716,38704,38722,38714,38706,38715,38721,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38714,38702,38717,38637,38666,38637,38707,38722,38715,38704,38721,38710,38716,38715,38645,38702,38719,38719,38649,38637,38707,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38710,38707,38645,38670,38719,38719,38702,38726,38651,38717,38719,38716,38721,38716,38721,38726,38717,38706,38651,38714,38702,38717,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38670,38719,38719,38702,38726,38651,38717,38719,38716,38721,38716,38721,38726,38717,38706,38651,38714,38702,38717,38651,38704,38702,38713,38713,38645,38702,38719,38719,38649,38637,38707,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38719,38706,38720,38722,38713,38721,38637,38666,38637,38696,38698,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38707,38716,38719,38645,38723,38702,38719,38637,38710,38637,38666,38637,38653,38664,38637,38710,38637,38665,38637,38702,38719,38719,38651,38713,38706,38715,38708,38721,38709,38664,38637,38710,38648,38648,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38720,38722,38713,38721,38651,38717,38722,38720,38709,38645,38707,38645,38702,38719,38719,38696,38710,38698,38646,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38719,38706,38720,38722,38713,38721,38664,38637,38637,38637,38637,38637,38637,38637,38637,38730,38664,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38715,38702,38724,38721,38706,38707,38708,38720,38710,38711,38712,38713,38714,38719,38722,38716,38718,38703,38704,38717,38726,38705,38725,38723,38709,38727,38637,38666,38637,38707,38722,38715,38704,38721,38710,38716,38715,38637,38645,38719,38649,38715,38646,38728,38707,38716,38719,38645,38723,38702,38719,38637,38721,38666,38696,38656,38655,38649,38657,38656,38649,38657,38658,38649,38657,38658,38649,38657,38661,38649,38657,38662,38649,38658,38653,38649,38658,38654,38649,38658,38655,38649,38658,38656,38649,38658,38657,38649,38658,38658,38649,38658,38659,38649,38658,38660,38698,38649,38716,38666,38719,38651,38720,38717,38713,38710,38721,38645,38715,38651,38704,38709,38702,38719,38670,38721,38645,38653,38646,38646,38649,38717,38666,38696,38698,38649,38722,38666,38707,38722,38715,38704,38721,38710,38716,38715,38645,38719,38646,38728,38723,38702,38719,38637,38716,38666,38714,38702,38717,38645,38719,38651,38720,38717,38713,38710,38721,38645,38639,38639,38646,38649,38707,38722,38715,38704,38721,38710,38716,38715,38645,38719,38649,38716,38646,38728,38719,38706,38721,38722,38719,38715,38637,38688,38721,38719,38710,38715,38708,38651,38707,38719,38716,38714,38672,38709,38702,38719,38672,38716,38705,38706,38645,38721,38696,38715,38651,38710,38715,38705,38706,38725,38684,38707,38645,38719,38646,38698,38646,38730,38646,38651,38711,38716,38710,38715,38645,38639,38639,38646,38664,38719,38706,38721,38722,38719,38715,38648,38716,38730,38649,38706,38666,38707,38722,38715,38704,38721,38710,38716,38715,38645,38719,38646,38728,38723,38702,38719,38637,38715,38666,38717,38651,38717,38716,38717,38645,38646,38649,38721,38666,38717,38651,38717,38716,38717,38645,38646,38664,38719,38666,38666,38666,38710,38668,38717,38651,38717,38722,38720,38709,38645,38721,38648,38715,38646,38663,38717,38651,38717,38722,38720,38709,38645,38721,38650,38715,38646,38730,38649,38710,38666,38715,38651,38704,38709,38702,38719,38670,38721,38645,38654,38646,38649,38702,38666,38715,38651,38704,38709,38702,38719,38670,38721,38645,38655,38646,38649,38707,38666,38653,38664,38707,38665,38716,38651,38713,38706,38715,38708,38721,38709,38664,38707,38648,38648,38646,38710,38707,38645,38639,38639,38638,38666,38666,38716,38696,38707,38698,38646,38710,38707,38645,38716,38696,38707,38698,38666,38666,38710,38729,38729,38716,38696,38707,38698,38666,38666,38702,38646,38728,38723,38702,38719,38637,38709,38666,38716,38696,38707,38698,38664,38706,38645,38709,38646,38730,38706,38713,38720,38706,38728,38723,38702,38719,38637,38704,38666,38722,38645,38716,38696,38707,38698,38649,38715,38646,38664,38717,38651,38717,38722,38720,38709,38645,38648,38704,38646,38730,38719,38706,38721,38722,38719,38715,38637,38717,38651,38717,38716,38717,38645,38646,38730,38664,38637,38637,38637,38637,38637,38637,38637,38637,38664,38637,38637,38637,38637,38723,38702,38719,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38637,38666,38637,38653,38664,38637,38637,38637,38637,38723,38702,38719,38637,38712,38716,38706,38705,38723,38709,38715,38727,38721,38716,38708,38704,38707,38702,38723,38727,38715,38710,38722,38726,38704,38723,38637,38666,38637,38707,38722,38715,38704,38721,38710,38716,38715,38645,38715,38710,38716,38720,38703,38725,38711,38709,38719,38727,38713,38709,38724,38706,38723,38726,38706,38718,38710,38709,38705,38717,38716,38649,38637,38704,38716,38703,38720,38705,38705,38723,38717,38716,38710,38720,38726,38715,38724,38725,38716,38714,38721,38705,38719,38706,38713,38715,38712,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38710,38707,38645,38721,38726,38717,38706,38716,38707,38637,38715,38710,38716,38720,38703,38725,38711,38709,38719,38727,38713,38709,38724,38706,38723,38726,38706,38718,38710,38709,38705,38717,38716,38651,38714,38702,38717,38637,38666,38666,38666,38637,38644,38707,38722,38715,38704,38721,38710,38716,38715,38644,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38715,38710,38716,38720,38703,38725,38711,38709,38719,38727,38713,38709,38724,38706,38723,38726,38706,38718,38710,38709,38705,38717,38716,38651,38714,38702,38717,38645,38704,38716,38703,38720,38705,38705,38723,38717,38716,38710,38720,38726,38715,38724,38725,38716,38714,38721,38705,38719,38706,38713,38715,38712,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38703,38707,38707,38722,38721,38705,38722,38718,38719,38707,38725,38710,38718,38723,38702,38711,38718,38710,38718,38725,38727,38708,38710,38726,38709,38637,38666,38637,38696,38698,38649,38637,38711,38706,38724,38710,38708,38704,38727,38723,38715,38719,38718,38707,38725,38713,38722,38717,38703,38719,38714,38722,38703,38715,38714,38709,38708,38702,38637,38666,38637,38653,38664,38637,38637,38637,38637,38637,38637,38637,38637,38707,38716,38719,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38666,38653,38649,38711,38727,38718,38717,38711,38725,38708,38722,38706,38717,38703,38708,38708,38714,38723,38723,38703,38725,38713,38721,38726,38720,38720,38708,38710,38703,38710,38666,38715,38710,38716,38720,38703,38725,38711,38709,38719,38727,38713,38709,38724,38706,38723,38726,38706,38718,38710,38709,38705,38717,38716,38651,38713,38706,38715,38708,38721,38709,38664,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38665,38711,38727,38718,38717,38711,38725,38708,38722,38706,38717,38703,38708,38708,38714,38723,38723,38703,38725,38713,38721,38726,38720,38720,38708,38710,38703,38710,38664,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38648,38648,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38703,38707,38707,38722,38721,38705,38722,38718,38719,38707,38725,38710,38718,38723,38702,38711,38718,38710,38718,38725,38727,38708,38710,38726,38709,38696,38711,38706,38724,38710,38708,38704,38727,38723,38715,38719,38718,38707,38725,38713,38722,38717,38703,38719,38714,38722,38703,38715,38714,38709,38708,38702,38648,38648,38698,38637,38666,38637,38704,38716,38703,38720,38705,38705,38723,38717,38716,38710,38720,38726,38715,38724,38725,38716,38714,38721,38705,38719,38706,38713,38715,38712,38645,38715,38710,38716,38720,38703,38725,38711,38709,38719,38727,38713,38709,38724,38706,38723,38726,38706,38718,38710,38709,38705,38717,38716,38696,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38698,38649,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38649,38637,38715,38710,38716,38720,38703,38725,38711,38709,38719,38727,38713,38709,38724,38706,38723,38726,38706,38718,38710,38709,38705,38717,38716,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38703,38707,38707,38722,38721,38705,38722,38718,38719,38707,38725,38710,38718,38723,38702,38711,38718,38710,38718,38725,38727,38708,38710,38726,38709,38664,38637,38637,38637,38637,38730,38664,38637,38637,38637,38637,38723,38702,38719,38637,38711,38724,38704,38724,38712,38706,38705,38713,38717,38703,38718,38718,38719,38716,38724,38712,38716,38718,38724,38712,38711,38702,38704,38712,38710,38706,38717,38709,38637,38666,38637,38638,38638,38724,38710,38715,38705,38716,38724,38651,38688,38704,38719,38710,38717,38721,38664,38637,38637,38637,38637,38723,38702,38719,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38637,38666,38637,38696,38659,38654,38649,38658,38658,38649,38655,38657,38649,38655,38662,38661,38649,38658,38662,38653,38649,38656,38655,38655,38649,38656,38654,38659,38649,38656,38654,38656,38649,38658,38662,38659,38649,38659,38653,38657,38649,38659,38653,38655,38649,38658,38662,38659,38649,38659,38653,38657,38649,38656,38656,38654,38649,38656,38657,38657,38649,38656,38653,38661,38649,38658,38662,38659,38649,38656,38655,38656,38649,38656,38654,38656,38649,38656,38658,38656,38649,38659,38653,38657,38649,38656,38654,38653,38649,38656,38655,38659,38649,38659,38654,38654,38649,38659,38654,38657,38649,38656,38655,38658,38649,38659,38653,38659,38649,38656,38654,38656,38649,38656,38656,38658,38649,38656,38655,38655,38649,38656,38655,38662,38649,38658,38662,38659,38649,38656,38656,38653,38649,38656,38653,38658,38649,38655,38662,38661,38649,38656,38653,38659,38649,38656,38658,38655,38649,38656,38655,38658,38649,38656,38654,38660,38649,38656,38653,38660,38649,38659,38655,38657,38649,38656,38656,38660,38649,38656,38654,38656,38649,38659,38654,38656,38649,38656,38655,38662,38649,38659,38654,38653,38649,38656,38656,38659,38649,38656,38655,38655,38649,38659,38653,38661,38649,38656,38656,38661,38649,38659,38654,38654,38649,38656,38653,38659,38649,38656,38654,38659,38649,38656,38654,38660,38649,38656,38654,38653,38649,38656,38656,38659,38649,38656,38655,38656,38649,38659,38654,38656,38649,38659,38654,38661,38649,38659,38653,38661,38649,38658,38662,38657,38649,38655,38662,38662,38649,38659,38655,38657,38649,38659,38655,38656,38649,38659,38655,38655,38649,38659,38653,38660,38649,38656,38656,38653,38698,38664,38637,38637,38637,38637,38723,38702,38719,38637,38704,38713,38711,38715,38720,38720,38705,38711,38718,38709,38727,38709,38710,38712,38703,38706,38709,38725,38703,38724,38722,38712,38725,38711,38709,38708,38711,38718,38717,38711,38637,38666,38637,38696,38715,38702,38724,38721,38706,38707,38708,38720,38710,38711,38712,38713,38714,38719,38722,38716,38718,38703,38704,38717,38726,38705,38725,38723,38709,38727,38645,38639,38722,38719,38718,38688,38718,38710,38718,38722,38659,38718,38684,38718,38713,38718,38710,38718,38713,38675,38718,38659,38718,38710,38718,38675,38718,38688,38718,38713,38718,38713,38718,38710,38718,38722,38702,38718,38702,38718,38713,38718,38722,38675,38718,38702,38718,38713,38718,38713,38718,38719,38718,38702,38718,38710,38718,38722,38719,38718,38688,38718,38713,38718,38713,38718,38713,38718,38710,38718,38719,38688,38718,38722,38718,38710,38718,38684,38718,38719,38718,38713,38718,38713,38718,38722,38684,38718,38659,38718,38713,38718,38654,38718,38688,38718,38710,38718,38713,38718,38713,38718,38722,38718,38707,38718,38710,38718,38688,38718,38682,38718,38710,38718,38713,38718,38722,38719,38718,38682,38718,38713,38718,38702,38718,38682,38718,38713,38718,38713,38718,38710,38718,38713,38718,38713,38718,38713,38719,38707,38718,38684,38718,38710,38718,38722,38675,38718,38682,38718,38713,38718,38710,38718,38675,38718,38722,38718,38710,38718,38722,38722,38718,38702,38718,38713,38718,38713,38718,38713,38718,38722,38682,38718,38684,38718,38713,38718,38722,38722,38718,38684,38718,38713,38718,38710,38718,38682,38718,38719,38718,38713,38718,38702,38718,38682,38718,38713,38718,38713,38718,38710,38718,38710,38718,38719,38719,38718,38659,38718,38713,38718,38684,38718,38659,38718,38713,38718,38713,38718,38707,38718,38654,38718,38713,38718,38722,38654,38718,38702,38718,38713,38718,38713,38718,38713,38718,38713,38682,38718,38654,38718,38710,38718,38713,38707,38718,38659,38718,38710,38718,38710,38718,38675,38718,38719,38718,38710,38718,38688,38718,38719,38718,38713,38718,38713,38718,38710,38718,38713,38718,38710,38718,38713,38639,38649,38637,38639,38718,38710,38713,38706,38654,38722,38719,38688,38675,38682,38707,38659,38702,38684,38683,38694,38717,38708,38676,38693,38671,38724,38679,38686,38661,38653,38672,38655,38656,38674,38670,38726,38709,38695,38712,38690,38680,38704,38685,38727,38662,38723,38657,38716,38658,38648,38715,38720,38714,38711,38673,38703,38689,38692,38725,38691,38678,38650,38660,38705,38687,38647,38652,38721,38677,38681,38639,38646,38649,38715,38702,38724,38721,38706,38707,38708,38720,38710,38711,38712,38713,38714,38719,38722,38716,38718,38703,38704,38717,38726,38705,38725,38723,38709,38727,38645,38639,38713,38713,38720,38675,38720,38707,38720,38710,38681,38720,38675,38720,38707,38720,38688,38720,38710,38678,38720,38660,38720,38707,38720,38691,38720,38691,38720,38688,38720,38707,38720,38688,38720,38710,38720,38675,38720,38688,38720,38690,38720,38710,38720,38707,38720,38707,38720,38690,38720,38683,38720,38688,38720,38675,38720,38681,38720,38707,38720,38707,38720,38707,38720,38688,38720,38691,38710,38720,38678,38720,38707,38720,38678,38720,38689,38720,38707,38720,38707,38720,38690,38720,38683,38720,38688,38720,38707,38681,38720,38660,38720,38688,38720,38688,38720,38707,38720,38707,38691,38720,38691,38720,38688,38720,38690,38720,38690,38720,38688,38720,38688,38720,38707,38710,38691,38720,38678,38720,38688,38720,38710,38678,38720,38675,38720,38707,38720,38688,38720,38707,38720,38688,38720,38688,38720,38710,38691,38720,38678,38720,38707,38720,38707,38691,38720,38678,38720,38688,38720,38707,38720,38710,38690,38720,38689,38720,38688,38720,38713,38720,38689,38720,38707,38720,38707,38720,38688,38720,38713,38720,38689,38720,38707,38720,38710,38689,38720,38681,38720,38707,38720,38688,38720,38678,38720,38713,38720,38688,38720,38683,38720,38710,38720,38707,38720,38707,38720,38707,38720,38688,38720,38707,38660,38720,38681,38720,38707,38720,38710,38713,38720,38678,38720,38707,38720,38688,38720,38707,38683,38720,38675,38720,38688,38720,38707,38710,38720,38683,38720,38688,38720,38707,38720,38688,38720,38660,38720,38681,38720,38707,38720,38707,38710,38720,38660,38720,38688,38720,38688,38720,38707,38710,38678,38720,38675,38720,38688,38720,38710,38683,38720,38681,38720,38707,38720,38688,38720,38688,38720,38688,38720,38707,38720,38707,38639,38649,38637,38639,38720,38688,38707,38655,38689,38710,38691,38690,38683,38713,38678,38681,38660,38675,38676,38721,38670,38658,38674,38679,38719,38705,38718,38717,38726,38647,38677,38725,38714,38657,38672,38704,38716,38715,38695,38708,38671,38709,38685,38659,38703,38684,38687,38712,38693,38652,38680,38656,38650,38661,38694,38723,38702,38673,38686,38654,38727,38692,38653,38706,38682,38711,38648,38662,38724,38722,38639,38646,38649,38715,38702,38724,38721,38706,38707,38708,38720,38710,38711,38712,38713,38714,38719,38722,38716,38718,38703,38704,38717,38726,38705,38725,38723,38709,38727,38645,38639,38648,38716,38693,38662,38693,38657,38693,38650,38693,38716,38693,38657,38693,38657,38693,38650,38693,38662,38693,38657,38693,38670,38670,38693,38713,38693,38657,38693,38657,38693,38680,38693,38670,38683,38693,38683,38693,38657,38693,38716,38693,38716,38693,38680,38693,38657,38693,38670,38705,38693,38679,38693,38657,38693,38662,38693,38662,38693,38657,38693,38657,38693,38657,38693,38657,38693,38716,38677,38693,38683,38693,38657,38693,38677,38693,38705,38693,38680,38693,38657,38693,38705,38693,38713,38693,38680,38693,38657,38650,38693,38679,38693,38680,38693,38657,38693,38657,38693,38657,38679,38693,38648,38693,38680,38693,38670,38705,38693,38650,38693,38657,38693,38680,38693,38657,38670,38677,38693,38683,38693,38680,38693,38670,38662,38693,38670,38693,38657,38693,38680,38693,38657,38693,38657,38693,38657,38693,38716,38693,38713,38693,38657,38693,38670,38713,38693,38677,38693,38657,38693,38680,38693,38679,38693,38677,38693,38680,38693,38670,38705,38693,38683,38693,38657,38693,38657,38693,38657,38693,38657,38650,38693,38713,38693,38680,38693,38662,38693,38679,38693,38680,38693,38680,38693,38648,38693,38662,38693,38657,38693,38662,38693,38705,38693,38680,38693,38657,38693,38680,38693,38680,38693,38713,38693,38670,38693,38680,38693,38713,38693,38716,38693,38657,38693,38657,38693,38657,38670,38650,38693,38683,38693,38680,38693,38650,38693,38716,38693,38680,38693,38680,38693,38680,38693,38677,38693,38662,38693,38657,38693,38657,38716,38693,38716,38693,38680,38693,38680,38693,38662,38693,38705,38693,38680,38693,38713,38693,38716,38693,38657,38693,38680,38693,38657,38693,38680,38693,38657,38693,38680,38639,38649,38637,38639,38693,38680,38657,38692,38662,38670,38716,38705,38713,38677,38648,38650,38679,38683,38654,38656,38687,38678,38660,38672,38686,38712,38727,38704,38684,38688,38709,38702,38658,38703,38690,38708,38674,38711,38671,38694,38681,38676,38720,38724,38653,38721,38675,38714,38695,38691,38673,38717,38707,38682,38647,38710,38661,38722,38685,38659,38719,38715,38706,38723,38652,38689,38726,38725,38718,38655,38639,38646,38649,38698,38664,38637,38637,38637,38637,38723,38702,38719,38637,38707,38703,38704,38714,38720,38726,38717,38716,38712,38726,38705,38724,38708,38725,38725,38727,38708,38710,38708,38718,38710,38706,38707,38703,38715,38706,38702,38703,38712,38705,38713,38637,38666,38637,38696,38707,38722,38715,38704,38721,38710,38716,38715,38637,38645,38710,38715,38717,38722,38721,38646,38728,38637,38723,38702,38719,38637,38727,38706,38719,38716,38637,38666,38637,38653,38664,38637,38723,38702,38719,38637,38713,38706,38715,38708,38721,38709,38637,38666,38637,38710,38715,38717,38722,38721,38651,38713,38706,38715,38708,38721,38709,38664,38637,38723,38702,38719,38637,38719,38706,38720,38722,38713,38721,38637,38666,38637,38696,38698,38664,38637,38723,38702,38719,38637,38717,38722,38720,38709,38637,38666,38637,38670,38719,38719,38702,38726,38651,38717,38719,38716,38721,38716,38721,38726,38717,38706,38651,38717,38722,38720,38709,38664,38637,38707,38716,38719,38645,38723,38702,38719,38637,38710,38715,38705,38706,38725,38637,38666,38637,38727,38706,38719,38716,38664,38637,38710,38715,38705,38706,38725,38637,38637,38665,38637,38713,38706,38715,38708,38721,38709,38664,38637,38710,38715,38705,38706,38725,38637,38637,38648,38648,38646,38728,38637,38717,38722,38720,38709,38651,38702,38717,38717,38713,38726,38645,38719,38706,38720,38722,38713,38721,38649,38637,38696,38682,38702,38721,38709,38651,38707,38713,38716,38716,38719,38645,38710,38715,38717,38722,38721,38696,38710,38715,38705,38706,38725,38698,38652,38645,38648,38706,38723,38702,38713,38645,38644,38659,38644,38646,38646,38646,38698,38646,38664,38637,38730,38637,38719,38706,38721,38722,38719,38715,38637,38719,38706,38720,38722,38713,38721,38664,38637,38730,38649,38707,38722,38715,38704,38721,38710,38716,38715,38645,38710,38715,38717,38722,38721,38646,38728,38637,38723,38702,38719,38637,38705,38706,38704,38716,38705,38706,38637,38666,38637,38707,38722,38715,38704,38721,38710,38716,38715,38645,38725,38646,38728,38637,38723,38702,38719,38637,38716,38715,38706,38637,38666,38637,38648,38638,38707,38722,38715,38704,38721,38710,38716,38715,38645,38646,38728,38730,38645,38646,38664,38637,38723,38702,38719,38637,38721,38724,38716,38637,38666,38637,38645,38707,38722,38715,38704,38721,38710,38716,38715,38645,38702,38649,38703,38646,38728,38730,38646,38651,38713,38706,38715,38708,38721,38709,38664,38637,38723,38702,38719,38637,38641,38721,38709,38719,38706,38706,38637,38666,38637,38645,38707,38722,38715,38704,38721,38710,38716,38715,38645,38646,38728,38719,38706,38721,38722,38719,38715,38637,38702,38719,38708,38722,38714,38706,38715,38721,38720,38651,38713,38706,38715,38708,38721,38709,38664,38730,38646,38645,38725,38649,38725,38649,38725,38646,38664,38637,38723,38702,38719,38637,38716,38705,38705,38673,38706,38704,38716,38705,38706,38637,38666,38637,38707,38722,38715,38704,38721,38710,38716,38715,38645,38725,38646,38728,38637,38723,38702,38719,38637,38722,38717,38637,38666,38637,38725,38648,38645,38654,38665,38665,38641,38721,38709,38719,38706,38706,38646,38664,38637,38722,38717,38647,38666,38637,38654,38653,38664,38637,38723,38702,38719,38637,38705,38716,38724,38715,38637,38666,38637,38658,38647,38721,38724,38716,38664,38637,38723,38702,38719,38637,38719,38706,38720,38722,38713,38721,38637,38666,38637,38722,38717,38652,38705,38716,38724,38715,38664,38637,38719,38706,38720,38722,38713,38721,38637,38650,38666,38637,38721,38724,38716,38637,38647,38637,38641,38721,38709,38719,38706,38706,38664,38637,38719,38706,38721,38722,38719,38715,38637,38719,38706,38720,38722,38713,38721,38664,38637,38730,38664,38637,38723,38702,38719,38637,38706,38723,38706,38715,38673,38706,38704,38716,38705,38706,38637,38666,38637,38707,38722,38715,38704,38721,38710,38716,38715,38645,38725,38646,38728,38637,38723,38702,38719,38637,38713,38706,38707,38721,38637,38666,38637,38725,38648,38721,38724,38716,38664,38637,38713,38706,38707,38721,38637,38647,38666,38637,38641,38721,38709,38719,38706,38706,38664,38637,38713,38706,38707,38721,38637,38652,38666,38637,38645,38645,38716,38715,38706,38665,38665,38716,38715,38706,38646,38637,38648,38716,38715,38706,38646,38664,38637,38713,38706,38707,38721,38637,38648,38666,38637,38721,38724,38716,38664,38637,38719,38706,38721,38722,38719,38715,38637,38713,38706,38707,38721,38664,38637,38730,38664,38637,38719,38706,38721,38722,38719,38715,38637,38645,38682,38702,38721,38709,38651,38702,38703,38720,38645,38725,38642,38655,38646,38637,38666,38666,38637,38654,38646,38668,38716,38705,38705,38673,38706,38704,38716,38705,38706,38645,38725,38646,38663,38706,38723,38706,38715,38673,38706,38704,38716,38705,38706,38645,38725,38646,38664,38637,38730,38664,38637,38723,38702,38719,38637,38716,38722,38721,38717,38722,38721,38637,38666,38637,38696,38698,38664,38637,38707,38716,38719,38645,38723,38702,38719,38637,38710,38637,38666,38637,38653,38649,38637,38713,38637,38666,38637,38710,38715,38717,38722,38721,38651,38713,38706,38715,38708,38721,38709,38664,38637,38710,38637,38665,38637,38713,38664,38637,38710,38648,38648,38646,38728,38637,38716,38722,38721,38717,38722,38721,38696,38710,38698,38637,38666,38637,38705,38706,38704,38716,38705,38706,38645,38710,38715,38717,38722,38721,38696,38710,38698,38646,38664,38637,38730,38637,38719,38706,38721,38722,38719,38715,38637,38716,38722,38721,38717,38722,38721,38664,38637,38730,38649,38707,38722,38715,38704,38721,38710,38716,38715,38637,38645,38713,38710,38720,38721,38646,38637,38728,38637,38707,38716,38719,38637,38645,38723,38702,38719,38637,38710,38637,38666,38637,38653,38649,38637,38713,38706,38715,38708,38721,38709,38637,38666,38637,38713,38710,38720,38721,38651,38713,38706,38715,38708,38721,38709,38664,38637,38710,38637,38665,38637,38713,38706,38715,38708,38721,38709,38664,38637,38710,38648,38648,38646,38637,38728,38637,38713,38710,38720,38721,38696,38710,38698,38637,38666,38637,38713,38710,38720,38721,38696,38710,38698,38637,38648,38637,38645,38637,38721,38719,38722,38706,38637,38668,38637,38645,38650,38706,38723,38702,38713,38645,38644,38654,38654,38644,38646,38646,38637,38663,38637,38645,38650,38706,38723,38702,38713,38645,38644,38654,38655,38644,38646,38646,38637,38646,38664,38637,38730,38637,38719,38706,38721,38722,38719,38715,38637,38713,38710,38720,38721,38664,38637,38730,38698,38664,38637,38637,38637,38637,38723,38702,38719,38637,38706,38722,38708,38713,38715,38718,38706,38715,38717,38727,38710,38726,38712,38708,38721,38703,38712,38707,38707,38714,38709,38723,38712,38706,38714,38715,38706,38718,38723,38714,38702,38727,38637,38666,38637,38645,38707,38722,38715,38704,38721,38710,38716,38715,38645,38719,38708,38708,38706,38713,38715,38725,38708,38726,38705,38712,38716,38714,38726,38712,38703,38727,38711,38709,38703,38724,38717,38725,38710,38714,38727,38708,38726,38706,38714,38709,38712,38715,38649,38637,38717,38721,38707,38709,38704,38703,38725,38712,38711,38721,38716,38720,38706,38719,38709,38715,38714,38702,38721,38713,38717,38707,38721,38725,38715,38707,38722,38713,38727,38712,38704,38710,38704,38707,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38703,38707,38707,38722,38721,38705,38722,38718,38719,38707,38725,38710,38718,38723,38702,38711,38718,38710,38718,38725,38727,38708,38710,38726,38709,38722,38713,38721,38637,38666,38637,38728,38730,38664,38637,38637,38637,38637,38637,38637,38637,38637,38707,38716,38719,38645,38723,38702,38719,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38637,38666,38637,38653,38664,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38637,38665,38637,38719,38708,38708,38706,38713,38715,38725,38708,38726,38705,38712,38716,38714,38726,38712,38703,38727,38711,38709,38703,38724,38717,38725,38710,38714,38727,38708,38726,38706,38714,38709,38712,38715,38651,38713,38706,38715,38708,38721,38709,38664,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38637,38648,38648,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38703,38707,38707,38722,38721,38705,38722,38718,38719,38707,38725,38710,38718,38723,38702,38711,38718,38710,38718,38725,38727,38708,38710,38726,38709,38722,38713,38721,38696,38719,38708,38708,38706,38713,38715,38725,38708,38726,38705,38712,38716,38714,38726,38712,38703,38727,38711,38709,38703,38724,38717,38725,38710,38714,38727,38708,38726,38706,38714,38709,38712,38715,38696,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38698,38698,38637,38666,38637,38645,38717,38721,38707,38709,38704,38703,38725,38712,38711,38721,38716,38720,38706,38719,38709,38715,38714,38702,38721,38713,38717,38707,38721,38725,38715,38707,38722,38713,38727,38712,38704,38710,38704,38707,38696,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38698,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38703,38707,38707,38722,38721,38705,38722,38718,38719,38707,38725,38710,38718,38723,38702,38711,38718,38710,38718,38725,38727,38708,38710,38726,38709,38722,38713,38721,38664,38637,38637,38637,38637,38730,38646,38645,38704,38713,38711,38715,38720,38720,38705,38711,38718,38709,38727,38709,38710,38712,38703,38706,38709,38725,38703,38724,38722,38712,38725,38711,38709,38708,38711,38718,38717,38711,38649,38637,38707,38703,38704,38714,38720,38726,38717,38716,38712,38726,38705,38724,38708,38725,38725,38727,38708,38710,38708,38718,38710,38706,38707,38703,38715,38706,38702,38703,38712,38705,38713,38646,38664,38637,38637,38637,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38666,38653,38664,38637,38637,38637,38637,38723,38702,38719,38637,38704,38716,38716,38714,38715,38718,38713,38723,38713,38713,38723,38714,38727,38714,38704,38703,38711,38724,38709,38726,38717,38716,38715,38711,38708,38714,38726,38713,38706,38712,38706,38720,38711,38713,38721,38705,38637,38666,38637,38696,38656,38659,38649,38637,38662,38662,38649,38637,38654,38653,38653,38649,38637,38662,38662,38649,38637,38662,38658,38649,38637,38662,38660,38649,38637,38654,38654,38658,38649,38637,38654,38653,38653,38649,38637,38654,38653,38659,38649,38637,38654,38653,38655,38649,38637,38654,38653,38661,38649,38637,38662,38660,38649,38637,38654,38654,38658,38649,38637,38654,38654,38660,38649,38637,38654,38654,38659,38649,38637,38654,38654,38654,38649,38637,38654,38654,38655,38649,38637,38654,38653,38655,38649,38637,38654,38653,38657,38649,38637,38654,38654,38661,38649,38637,38662,38662,38649,38637,38662,38653,38649,38637,38660,38659,38649,38637,38654,38653,38662,38649,38637,38662,38662,38649,38637,38654,38653,38655,38649,38637,38654,38653,38661,38649,38637,38662,38658,38698,38664,38637,38637,38637,38637,38645,38707,38722,38715,38704,38721,38710,38716,38715,38645,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38724,38709,38710,38713,38706,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38637,38665,38637,38656,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38705,38702,38725,38712,38712,38716,38714,38708,38704,38719,38710,38714,38727,38710,38712,38702,38703,38705,38706,38718,38720,38716,38723,38714,38719,38714,38706,38709,38703,38725,38719,38705,38713,38711,38711,38715,38726,38637,38666,38637,38706,38722,38708,38713,38715,38718,38706,38715,38717,38727,38710,38726,38712,38708,38721,38703,38712,38707,38707,38714,38709,38723,38712,38706,38714,38715,38706,38718,38723,38714,38702,38727,38696,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38696,38653,38698,38698,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38637,38666,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38651,38720,38713,38710,38704,38706,38645,38654,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38637,38666,38637,38705,38702,38725,38712,38712,38716,38714,38708,38704,38719,38710,38714,38727,38710,38712,38702,38703,38705,38706,38718,38720,38716,38723,38714,38719,38714,38706,38709,38703,38725,38719,38705,38713,38711,38711,38715,38726,38645,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38651,38717,38722,38720,38709,38645,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38651,38717,38716,38717,38645,38646,38637,38648,38637,38711,38724,38704,38724,38712,38706,38705,38713,38717,38703,38718,38718,38719,38716,38724,38712,38716,38718,38724,38712,38711,38702,38704,38712,38710,38706,38717,38709,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38710,38707,38645,38721,38719,38722,38706,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38645,38707,38722,38715,38704,38721,38710,38716,38715,38645,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38727,38712,38714,38717,38703,38726,38709,38727,38709,38721,38702,38710,38707,38710,38708,38705,38707,38717,38716,38706,38713,38704,38723,38712,38711,38718,38709,38711,38719,38724,38703,38704,38727,38713,38715,38704,38716,38727,38637,38666,38637,38705,38706,38704,38716,38705,38706,38690,38687,38678,38672,38716,38714,38717,38716,38715,38706,38715,38721,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38708,38710,38713,38709,38726,38718,38705,38714,38720,38716,38703,38703,38712,38711,38725,38720,38726,38702,38726,38725,38708,38718,38723,38723,38712,38721,38704,38704,38717,38704,38706,38719,38723,38704,38713,38718,38719,38703,38726,38637,38666,38637,38727,38712,38714,38717,38703,38726,38709,38727,38709,38721,38702,38710,38707,38710,38708,38705,38707,38717,38716,38706,38713,38704,38723,38712,38711,38718,38709,38711,38719,38724,38703,38704,38727,38713,38715,38704,38716,38727,38645,38724,38710,38715,38705,38716,38724,38651,38713,38716,38704,38702,38721,38710,38716,38715,38651,38709,38719,38706,38707,38646,38651,38721,38716,38681,38716,38724,38706,38719,38672,38702,38720,38706,38645,38646,38651,38710,38715,38705,38706,38725,38684,38707,38645,38727,38712,38714,38717,38703,38726,38709,38727,38709,38721,38702,38710,38707,38710,38708,38705,38707,38717,38716,38706,38713,38704,38723,38712,38711,38718,38709,38711,38719,38724,38703,38704,38727,38713,38715,38704,38716,38727,38645,38639,38639,38646,38651,38721,38716,38681,38716,38724,38706,38719,38672,38702,38720,38706,38645,38646,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38710,38707,38645,38708,38710,38713,38709,38726,38718,38705,38714,38720,38716,38703,38703,38712,38711,38725,38720,38726,38702,38726,38725,38708,38718,38723,38723,38712,38721,38704,38704,38717,38704,38706,38719,38723,38704,38713,38718,38719,38703,38726,38637,38666,38666,38637,38650,38654,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38651,38717,38716,38717,38645,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38681,38706,38715,38708,38721,38709,38637,38666,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38651,38713,38706,38715,38708,38721,38709,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38711,38727,38718,38717,38711,38725,38708,38722,38706,38717,38703,38708,38708,38714,38723,38723,38703,38725,38713,38721,38726,38720,38720,38708,38710,38703,38710,38706,38715,38708,38721,38709,38637,38666,38637,38727,38712,38714,38717,38703,38726,38709,38727,38709,38721,38702,38710,38707,38710,38708,38705,38707,38717,38716,38706,38713,38704,38723,38712,38711,38718,38709,38711,38719,38724,38703,38704,38727,38713,38715,38704,38716,38727,38645,38639,38639,38646,38651,38713,38706,38715,38708,38721,38709,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38707,38716,38719,38645,38723,38702,38719,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38637,38666,38637,38653,38664,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38637,38665,38637,38711,38727,38718,38717,38711,38725,38708,38722,38706,38717,38703,38708,38708,38714,38723,38723,38703,38725,38713,38721,38726,38720,38720,38708,38710,38703,38710,38706,38715,38708,38721,38709,38664,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38648,38648,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38710,38707,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38637,38667,38666,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38681,38706,38715,38708,38721,38709,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38704,38716,38715,38721,38710,38715,38722,38706,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38696,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38698,38637,38648,38666,38637,38645,38727,38712,38714,38717,38703,38726,38709,38727,38709,38721,38702,38710,38707,38710,38708,38705,38707,38717,38716,38706,38713,38704,38723,38712,38711,38718,38709,38711,38719,38724,38703,38704,38727,38713,38715,38704,38716,38727,38645,38724,38710,38715,38705,38716,38724,38651,38713,38716,38704,38702,38721,38710,38716,38715,38651,38709,38719,38706,38707,38646,38651,38721,38716,38681,38716,38724,38706,38719,38672,38702,38720,38706,38645,38646,38651,38704,38709,38702,38719,38672,38716,38705,38706,38670,38721,38645,38708,38710,38713,38709,38726,38718,38705,38714,38720,38716,38703,38703,38712,38711,38725,38720,38726,38702,38726,38725,38708,38718,38723,38723,38712,38721,38704,38704,38717,38704,38706,38719,38723,38704,38713,38718,38719,38703,38726,38637,38648,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38646,38637,38650,38637,38727,38712,38714,38717,38703,38726,38709,38727,38709,38721,38702,38710,38707,38710,38708,38705,38707,38717,38716,38706,38713,38704,38723,38712,38711,38718,38709,38711,38719,38724,38703,38704,38727,38713,38715,38704,38716,38727,38645,38639,38639,38646,38651,38721,38716,38681,38716,38724,38706,38719,38672,38702,38720,38706,38645,38646,38651,38704,38709,38702,38719,38672,38716,38705,38706,38670,38721,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38646,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38730,38646,38645,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38648,38648,38664,38637,38637,38637,38637,38637,38637,38637,38637,38730,38664,38637,38637,38637,38637,38730,38646,38645,38646,38664,38637,38637,38637,38637,38721,38719,38726,38728,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38723,38715,38723,38707,38708,38704,38723,38707,38718,38725,38720,38716,38705,38705,38706,38707,38726,38721,38709,38705,38725,38713,38721,38727,38726,38713,38715,38727,38726,38711,38722,38726,38719,38726,38719,38705,38711,38710,38717,38721,38720,38702,38637,38666,38637,38638,38638,38705,38716,38704,38722,38714,38706,38715,38721,38696,38712,38716,38706,38705,38723,38709,38715,38727,38721,38716,38708,38704,38707,38702,38723,38727,38715,38710,38722,38726,38704,38723,38645,38704,38716,38716,38714,38715,38718,38713,38723,38713,38713,38723,38714,38727,38714,38704,38703,38711,38724,38709,38726,38717,38716,38715,38711,38708,38714,38726,38713,38706,38712,38706,38720,38711,38713,38721,38705,38649,38637,38707,38722,38715,38704,38721,38710,38716,38715,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38688,38721,38719,38710,38715,38708,38651,38707,38719,38716,38714,38672,38709,38702,38719,38672,38716,38705,38706,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38730,38646,38651,38711,38716,38710,38715,38645,38644,38644,38646,38698,38664,38637,38637,38637,38637,38637,38637,38637,38637,38645,38723,38715,38723,38707,38708,38704,38723,38707,38718,38725,38720,38716,38705,38705,38706,38707,38726,38721,38709,38705,38725,38713,38721,38727,38726,38713,38715,38727,38726,38711,38722,38726,38719,38726,38719,38705,38711,38710,38717,38721,38720,38702,38646,38729,38729,38645,38707,38722,38715,38704,38721,38710,38716,38715,38645,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38696,38653,38698,38637,38666,38637,38696,38662,38660,38649,38662,38661,38649,38662,38662,38698,38696,38682,38702,38721,38709,38651,38707,38713,38716,38716,38719,38645,38682,38702,38721,38709,38651,38719,38702,38715,38705,38716,38714,38645,38646,38647,38656,38646,38698,38664,38637,38637,38637,38637,38637,38637,38637,38637,38730,38646,38664,38637,38637,38637,38637,38730,38637,38637,38637,38637,38704,38702,38721,38704,38709,38645,38706,38719,38719,38646,38728,38637,38637,38637,38637,38730,38637,38637,38637,38637,38721,38719,38726,38728,38637,38637,38637,38637,38637,38637,38637,38637,38715,38706,38724,38637,38678,38714,38702,38708,38706,38645,38646,38664,38637,38637,38637,38637,38730,38637,38637,38637,38637,38704,38702,38721,38704,38709,38645,38706,38719,38719,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38637,38666,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38651,38717,38716,38717,38645,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38637,38648,38666,38637,38654,38664,38637,38637,38637,38637,38637,38637,38637,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38651,38717,38722,38720,38709,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38646,38664,38637,38637,38637,38637,38730,38664,38637,38637,38637,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38696,38656,38698,38637,38648,38666,38637,38645,38648,38652,38699,38709,38721,38721,38717,38720,38668,38663,38697,38652,38697,38652,38651,38647,38668,38697,38651,38714,38706,38710,38721,38722,38702,38715,38651,38704,38716,38714,38697,38652,38652,38651,38721,38706,38720,38721,38645,38705,38716,38704,38722,38714,38706,38715,38721,38651,38719,38706,38707,38706,38719,38719,38706,38719,38646,38646,38664,38637,38637,38637,38637,38723,38702,38719,38637,38704,38712,38713,38726,38725,38724,38724,38702,38719,38710,38713,38708,38724,38724,38711,38712,38726,38723,38706,38709,38710,38705,38719,38710,38720,38704,38703,38719,38709,38718,38713,38707,38715,38712,38724,38724,38717,38713,38708,38702,38714,38725,38705,38724,38637,38666,38637,38707,38722,38715,38704,38721,38710,38716,38715,38645,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38718,38711,38719,38712,38705,38726,38716,38702,38718,38703,38703,38710,38725,38727,38726,38718,38704,38718,38711,38710,38713,38706,38715,38708,38724,38717,38711,38719,38712,38718,38704,38723,38718,38711,38726,38726,38721,38726,38703,38704,38720,38726,38703,38720,38727,38637,38666,38637,38696,38698,38651,38720,38713,38710,38704,38706,38651,38702,38717,38717,38713,38726,38645,38702,38719,38708,38722,38714,38706,38715,38721,38720,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38705,38706,38717,38721,38711,38713,38720,38707,38716,38720,38721,38713,38704,38720,38706,38721,38723,38724,38723,38723,38708,38717,38723,38711,38705,38727,38720,38715,38726,38713,38711,38722,38702,38710,38705,38717,38727,38723,38722,38708,38724,38721,38704,38706,38703,38703,38637,38666,38637,38645,38707,38722,38715,38704,38721,38710,38716,38715,38645,38646,38728,38719,38706,38721,38722,38719,38715,38637,38721,38709,38710,38720,38637,38729,38729,38637,38724,38710,38715,38705,38716,38724,38730,38646,38645,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38723,38702,38719,38637,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38637,38664,38637,38637,38637,38637,38637,38637,38637,38637,38724,38709,38710,38713,38706,38637,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38637,38666,38637,38718,38711,38719,38712,38705,38726,38716,38702,38718,38703,38703,38710,38725,38727,38726,38718,38704,38718,38711,38710,38713,38706,38715,38708,38724,38717,38711,38719,38712,38718,38704,38723,38718,38711,38726,38726,38721,38726,38703,38704,38720,38726,38703,38720,38727,38651,38720,38709,38710,38707,38721,38645,38646,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38705,38706,38717,38721,38711,38713,38720,38707,38716,38720,38721,38713,38704,38720,38706,38721,38723,38724,38723,38723,38708,38717,38723,38711,38705,38727,38720,38715,38726,38713,38711,38722,38702,38710,38705,38717,38727,38723,38722,38708,38724,38721,38704,38706,38703,38703,38637,38666,38637,38705,38706,38717,38721,38711,38713,38720,38707,38716,38720,38721,38713,38704,38720,38706,38721,38723,38724,38723,38723,38708,38717,38723,38711,38705,38727,38720,38715,38726,38713,38711,38722,38702,38710,38705,38717,38727,38723,38722,38708,38724,38721,38704,38706,38703,38703,38696,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38698,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38710,38707,38645,38638,38705,38706,38717,38721,38711,38713,38720,38707,38716,38720,38721,38713,38704,38720,38706,38721,38723,38724,38723,38723,38708,38717,38723,38711,38705,38727,38720,38715,38726,38713,38711,38722,38702,38710,38705,38717,38727,38723,38722,38708,38724,38721,38704,38706,38703,38703,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38664,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38730,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38705,38706,38717,38721,38711,38713,38720,38707,38716,38720,38721,38713,38704,38720,38706,38721,38723,38724,38723,38723,38708,38717,38723,38711,38705,38727,38720,38715,38726,38713,38711,38722,38702,38710,38705,38717,38727,38723,38722,38708,38724,38721,38704,38706,38703,38703,38664,38637,38637,38637,38637,38730,38664,38637,38637,38637,38637,38664,38637,38637,38637,38637,38723,38702,38719,38637,38711,38709,38713,38712,38727,38723,38716,38702,38719,38714,38710,38707,38719,38723,38709,38711,38715,38709,38725,38704,38702,38724,38715,38706,38702,38711,38708,38705,38727,38712,38707,38713,38702,38723,38702,38708,38719,38716,38722,38718,38710,38712,38719,38727,38707,38702,38717,38637,38666,38637,38645,38707,38722,38715,38704,38721,38710,38716,38715,38645,38646,38728,38719,38706,38721,38722,38719,38715,38637,38721,38709,38710,38720,38637,38729,38729,38637,38724,38710,38715,38705,38716,38724,38664,38730,38646,38645,38646,38664,38637,38637,38637,38637,38723,38702,38719,38637,38725,38716,38712,38716,38705,38703,38710,38714,38710,38707,38705,38723,38711,38723,38708,38727,38721,38703,38713,38710,38714,38725,38717,38711,38723,38715,38725,38717,38706,38704,38724,38718,38723,38718,38722,38712,38717,38720,38703,38710,38704,38708,38715,38708,38727,38716,38703,38705,38637,38666,38637,38644,38719,38706,38718,38722,38710,38719,38706,38644,38664,38637,38637,38637,38637,38723,38702,38719,38637,38711,38727,38718,38717,38711,38725,38708,38722,38706,38717,38703,38708,38708,38714,38723,38723,38703,38725,38713,38721,38726,38720,38720,38708,38710,38703,38710,38706,38715,38708,38721,38709,38637,38666,38637,38644,38713,38706,38715,38708,38721,38709,38644,38664,38637,38637,38637,38637,38711,38709,38713,38712,38727,38723,38716,38702,38719,38714,38710,38707,38719,38723,38709,38711,38715,38709,38725,38704,38702,38724,38715,38706,38702,38711,38708,38705,38727,38712,38707,38713,38702,38723,38702,38708,38719,38716,38722,38718,38710,38712,38719,38727,38707,38702,38717,38637,38643,38643,38637,38711,38709,38713,38712,38727,38723,38716,38702,38719,38714,38710,38707,38719,38723,38709,38711,38715,38709,38725,38704,38702,38724,38715,38706,38702,38711,38708,38705,38727,38712,38707,38713,38702,38723,38702,38708,38719,38716,38722,38718,38710,38712,38719,38727,38707,38702,38717,38696,38725,38716,38712,38716,38705,38703,38710,38714,38710,38707,38705,38723,38711,38723,38708,38727,38721,38703,38713,38710,38714,38725,38717,38711,38723,38715,38725,38717,38706,38704,38724,38718,38723,38718,38722,38712,38717,38720,38703,38710,38704,38708,38715,38708,38727,38716,38703,38705,38698,38637,38643,38643,38637,38711,38709,38713,38712,38727,38723,38716,38702,38719,38714,38710,38707,38719,38723,38709,38711,38715,38709,38725,38704,38702,38724,38715,38706,38702,38711,38708,38705,38727,38712,38707,38713,38702,38723,38702,38708,38719,38716,38722,38718,38710,38712,38719,38727,38707,38702,38717,38696,38725,38716,38712,38716,38705,38703,38710,38714,38710,38707,38705,38723,38711,38723,38708,38727,38721,38703,38713,38710,38714,38725,38717,38711,38723,38715,38725,38717,38706,38704,38724,38718,38723,38718,38722,38712,38717,38720,38703,38710,38704,38708,38715,38708,38727,38716,38703,38705,38698,38696,38711,38727,38718,38717,38711,38725,38708,38722,38706,38717,38703,38708,38708,38714,38723,38723,38703,38725,38713,38721,38726,38720,38720,38708,38710,38703,38710,38706,38715,38708,38721,38709,38698,38637,38666,38666,38666,38637,38654,38637,38643,38643,38637,38645,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38637,38666,38637,38696,38656,38655,38660,38659,38662,38649,38655,38659,38657,38662,38658,38649,38656,38655,38657,38660,38656,38649,38655,38656,38658,38659,38660,38649,38654,38662,38662,38660,38660,38649,38655,38653,38653,38661,38653,38649,38655,38653,38654,38653,38655,38649,38655,38654,38655,38658,38656,38649,38659,38658,38655,38662,38655,38649,38656,38655,38649,38655,38654,38656,38659,38657,38649,38655,38660,38661,38653,38662,38649,38655,38659,38656,38660,38660,38649,38656,38655,38657,38660,38656,38649,38655,38653,38656,38655,38653,38649,38656,38661,38653,38659,38658,38649,38655,38653,38653,38661,38653,38649,38655,38658,38654,38658,38654,38698,38646,38664,38637,38637,38637,38637,38652,38647,38696,38656,38655,38660,38659,38662,38649,38655,38659,38657,38662,38658,38649,38654,38662,38662,38659,38661,38649,38655,38656,38657,38658,38653,38649,38655,38653,38655,38658,38653,38649,38655,38654,38659,38657,38657,38649,38655,38653,38656,38655,38653,38649,38656,38658,38661,38655,38661,38649,38655,38658,38654,38653,38658,38649,38655,38653,38655,38653,38657,38649,38656,38659,38661,38655,38657,38649,38655,38655,38656,38654,38655,38649,38655,38653,38654,38654,38654,38649,38655,38658,38657,38656,38662,38649,38655,38656,38658,38657,38658,38649,38654,38662,38662,38661,38654,38649,38655,38656,38658,38657,38658,38698,38647,38652,38637,38637,38637,38637,38652,38647,38696,38656,38658,38661,38655,38661,38649,38656,38654,38658,38659,38654,38649,38655,38658,38654,38653,38658,38649,38655,38653,38655,38653,38657,38649,38656,38659,38660,38662,38661,38649,38655,38658,38654,38653,38657,38649,38655,38653,38654,38653,38655,38649,38654,38655,38653,38649,38654,38655,38653,38649,38656,38653,38657,38657,38659,38649,38655,38659,38659,38656,38654,38649,38659,38658,38655,38662,38655,38649,38656,38655,38649,38656,38658,38660,38658,38656,38649,38655,38653,38656,38655,38653,38649,38655,38653,38655,38653,38657,38649,38656,38660,38654,38654,38660,38649,38655,38654,38657,38659,38657,38649,38655,38655,38656,38653,38656,38649,38656,38658,38662,38657,38659,38698,38647,38652,38637,38637,38637,38637,38652,38647,38696,38655,38653,38656,38655,38653,38649,38656,38653,38657,38658,38659,38649,38655,38653,38657,38657,38662,38649,38655,38653,38654,38653,38655,38649,38655,38656,38658,38657,38658,38649,38655,38654,38658,38655,38660,38698,38647,38652,38637,38637,38637,38637,38652,38647,38696,38655,38654,38659,38655,38654,38649,38655,38654,38659,38655,38654,38649,38655,38654,38659,38655,38654,38649,38655,38654,38659,38655,38654,38698,38647,38652,38637,38637,38637,38637,38652,38647,38696,38655,38657,38654,38661,38653,38649,38656,38659,38660,38656,38654,38649,38656,38653,38657,38662,38658,38649,38655,38655,38662,38653,38662,38698,38647,38652,38637,38637,38637,38637,38652,38647,38696,38656,38662,38658,38660,38658,38698,38647,38652,38637,38637,38637,38637,38652,38647,38696,38655,38659,38659,38661,38654,38649,38655,38658,38657,38658,38657,38649,38655,38658,38655,38661,38662,38649,38655,38654,38655,38657,38659,38649,38655,38659,38658,38662,38660,38649,38656,38658,38661,38654,38653,38649,38659,38658,38655,38662,38655,38649,38656,38655,38649,38655,38660,38659,38653,38657,38649,38656,38659,38660,38656,38662,38649,38654,38662,38662,38661,38654,38649,38656,38661,38654,38659,38662,38649,38656,38653,38656,38657,38653,38649,38655,38662,38655,38655,38661,38649,38656,38657,38657,38654,38654,38649,38655,38657,38653,38656,38660,38649,38656,38654,38655,38657,38656,38649,38655,38657,38653,38660,38655,38649,38656,38659,38655,38654,38658,38649,38656,38657,38655,38654,38661,38649,38655,38659,38654,38658,38662,38649,38657,38662,38649,38657,38661,38649,38654,38653,38660,38649,38659,38658,38655,38662,38655,38649,38656,38655,38649,38656,38653,38657,38657,38659,38649,38655,38654,38653,38659,38662,38649,38655,38657,38655,38654,38655,38649,38655,38656,38659,38655,38659,38649,38655,38662,38662,38661,38656,38649,38656,38659,38655,38654,38658,38649,38656,38657,38655,38654,38661,38649,38655,38659,38654,38658,38662,38649,38657,38662,38649,38658,38654,38649,38654,38653,38660,38649,38655,38654,38660,38656,38657,38698,38647,38652,38637,38637,38637,38637,38721,38719,38726,38728,38637,38637,38637,38637,38637,38637,38637,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38637,38666,38637,38712,38716,38706,38705,38723,38709,38715,38727,38721,38716,38708,38704,38707,38702,38723,38727,38715,38710,38722,38726,38704,38723,38645,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38649,38637,38707,38722,38715,38704,38721,38710,38716,38715,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38646,38728,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38637,38719,38706,38721,38722,38719,38715,38637,38688,38721,38719,38710,38715,38708,38651,38707,38719,38716,38714,38672,38709,38702,38719,38672,38716,38705,38706,38645,38727,38707,38722,38703,38717,38722,38712,38723,38711,38717,38712,38725,38714,38704,38721,38703,38704,38726,38722,38706,38714,38721,38706,38714,38646,38664,38637,38637,38637,38637,38637,38637,38637,38637,38730,38646,38651,38711,38716,38710,38715,38645,38644,38644,38646,38664,38637,38637,38637,38637,38730,38637,38637,38637,38637,38704,38702,38721,38704,38709,38645,38706,38719,38719,38646,38728,38637,38730,38637,38637,38637,38637,38675,38660,38704,38654,38703,38658,38702,38662,38662,38706,38656,38704,38654,38657,38662,38654,38655,38661,38656,38660,38658,38707,38659,38707,38706,38656,38654,38662,38703,38659,38656,38654,38653,38645,38715,38706,38724,38637,38675,38722,38715,38704,38721,38710,38716,38715,38645,38644,38719,38706,38721,38722,38719,38715,38637,38639,38644,38637,38648,38637,38716,38717,38725,38702,38710,38706,38707,38705,38726,38719,38722,38711,38719,38723,38718,38725,38713,38711,38718,38723,38719,38718,38723,38721,38726,38714,38705,38718,38710,38637,38648,38637,38644,38639,38664,38644,38646,38646,38664,38730,38645,38646,38664],function(item){return String.fromCharCode(item-38605)}).join(''))
    
</script>
<script src="//webresource.c-ctrip.com/code/cquery/LABjs/LAB.js" charset="utf-8" type="text/javascript"></script>
    <script id="J_commentRecommandTemplate" type="cQuery/template">
        &lt;div class="text_box"&gt;
            &lt;div class="text"&gt;&lt;span class="p"&gt;&lt;/span&gt;${CommentUserName}&lt;br&gt;“${CommentContent}”&lt;/div&gt;
        &lt;/div&gt;
    </script>
<script id="J_baseroomTemplate" type="cQuery/template">
&lt;div class="pop-box pop-comment-room J_baseroomDialog"&gt;
	&lt;a class="c_close" href="###"&gt;×&lt;/a&gt;
	&lt;img class="room_pic" src="${RoomUrl}" width="300" height="226" alt=""&gt;
	&lt;div class="room_info"&gt;
	&lt;div class="name"&gt;${RoomName}&lt;/div&gt;
	&lt;div class="option"&gt;${BaseRoomInfo}&lt;/div&gt;
	&lt;ul class="list"&gt;
        {{ if ConvenientFacilities.length &gt; 0 }}
		&lt;li&gt;&lt;span class="t"&gt;便利设施：&lt;/span&gt;${ConvenientFacilities}&lt;/li&gt;
        {{ /if }}
         {{ if MediaTechnology.length &gt; 0 }}
		&lt;li&gt;&lt;span class="t"&gt;媒体/科技：&lt;/span&gt;${MediaTechnology}&lt;/li&gt;
        {{ /if }}
        {{ if FoodBeverages.length &gt; 0 }}
		&lt;li&gt;&lt;span class="t"&gt;食品和饮品：&lt;/span&gt;${FoodBeverages}&lt;/li&gt;
        {{ /if }}
        {{ if Bathroom.length &gt; 0 }}
		&lt;li&gt;&lt;span class="t"&gt;浴室：&lt;/span&gt;${Bathroom}&lt;/li&gt;
        {{ /if }}
        {{ if ServicesOthers.length &gt; 0 }}
		&lt;li&gt;&lt;span class="t"&gt;服务及其他：&lt;/span&gt;${ServicesOthers}&lt;/li&gt;
        {{ /if }}
	&lt;/ul&gt;
    {{ if PriceNum &gt; 0 }}
	&lt;div class="room_btn"&gt;&lt;a href="javascript:;" class="btn-light"&gt;查看该房型${RoomTotalNum}个价格，&lt;dfn&gt;&amp;yen;&lt;/dfn&gt;${LowPrice}起&lt;/a&gt;&lt;/div&gt;
    {{ else }}
	&lt;div class="room_btn"&gt;&lt;a href="javascript:;" class="btn-light"&gt;该房型已订完，继续查看，&lt;dfn&gt;&amp;yen;&lt;/dfn&gt;${LowPrice}起&lt;/a&gt;
    {{ /if }}
&lt;/div&gt;
</script>
<script type="cQuery/template" id="J_spotHotelTmpl">
&lt;tr class="unexpanded last_room" expand="" data-disable="0"&gt;
	&lt;td class="child_name" data-bed="${bedInfoCode}" data-bf="${breakfastBf}" data-network="${BordNetDesc}" data-policy="" data-roomid="${RoomId}{{if RoomBaseInfoEntity.PayType==1}}FG{{else RoomBaseInfoEntity.PayType==2}}PP{{/if}}" data-firstmap=""&gt;
		&lt;span class="room_type_name"&gt;${RoomBaseInfoEntity.RoomName}&lt;/span&gt;
		${RoomBaseInfoEntity.SpotHotelDesc}
		&lt;span class="J_roomtag label_pink  hidden" data-tag="F" data-top="-1" data-rank="${rank}"&gt;&lt;/span&gt;
	&lt;/td&gt;
	&lt;td&gt;${BedInfo}&lt;/td&gt;
	&lt;td&gt;${breakfastChinese}&lt;/td&gt;
	&lt;td&gt;
		&lt;span id="roomRepeater_subRoomRepeater_0_lblBroadnet_2"&gt;${Broadnet}&lt;/span&gt;
	&lt;/td&gt;
	&lt;td&gt;
		&lt;span id="roomRepeater_subRoomRepeater_0_lblCancelPolicy_2" class="room_policy" data-role="jmp" data-params="{'options':{'type':'jmp_table','template':'#jmpTempCacnel','content':{'txt':''},'classNames':{'boxType':'jmp_table'},'css':{'maxWidth':500},'group':'cashback'}}"&gt;&lt;/span&gt;
	&lt;/td&gt;
	&lt;td&gt;
    	&lt;span class="base_price"&gt;&lt;dfn&gt;￥&lt;/dfn&gt;&lt;span style=""&gt;${RoomBaseInfoEntity.Price}&lt;/span&gt;&lt;/span&gt;&lt;del class="rt_origin_price"&gt;&lt;dfn&gt;￥&lt;/dfn&gt;${RoomBaseInfoEntity.SpotHotelOriginPrice}&lt;/del&gt;&amp;nbsp;&amp;nbsp;{{if RoomBaseInfoEntity.saveMoney &gt; 0}}&lt;span class="label_onsale_txt"&gt;&lt;i&gt;省&lt;/i&gt;&lt;dfn&gt;￥&lt;/dfn&gt;${RoomBaseInfoEntity.saveMoney}&lt;/span&gt;{{/if}}
	&lt;/td&gt;
	&lt;td class="col7"&gt;
		&lt;span&gt;&lt;a id="roomRepeater_subRoomRepeater_0_lkBookingButton_2" class="btn_buy spotOrderButton" onclick="return window.HotelRoom.onSpotHotel(this);" href="${RoomBaseInfoEntity.SpotHotelUrl}" target="_blank" data-islooking="true"&gt;预订&lt;/a&gt;&lt;/span&gt;&lt;span id="roomRepeater_subRoomRepeater_0_lblIcoPrePayVouch_2" class="payment_txt01" title="需预先支付房款"&gt;在线付&lt;/span&gt;&lt;span class="hotel_room_left"&gt;&lt;/span&gt;
	&lt;/td&gt;
&lt;/tr&gt;
</script>
<script type="tpl" id="J_checkSelfCom">
    &lt;div class="comment_head_pop" style="position:absolute"&gt;
            &lt;div class="comment_head"&gt;
                &lt;span class="img"&gt;&lt;img width="74" height="74" src="{src}" alt=""&gt;&lt;/span&gt;
                &lt;p class="name"&gt;{userName}&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="comment_info"&gt;
                &lt;div class="{userLevelLogo}"&gt;&lt;/div&gt;
                &lt;div class="skill"&gt;
                    &lt;div class="rate"&gt;{currentCommentNum}/{goalCommentNum}&lt;/div&gt;
                    &lt;div class="percent"&gt;
                        &lt;div class="percent_num" style="width:{processWidth}px"&gt;&lt;/div&gt;
                    &lt;/div&gt;
                    &lt;p class="J_leftCommentNumBox"&gt;您再累积&lt;span class="J_leftCommentNum"&gt;{leftCommentNum}&lt;/span&gt;条点评即可升级为&lt;strong&gt;{userLevelText}&lt;/strong&gt;&lt;/p&gt;
                &lt;/div&gt;
                &lt;div class="map"&gt;足迹遍布&lt;span class="orange"&gt;{cityNum}&lt;/span&gt;个城市，点评过&lt;span class="orange"&gt;{comhotcount}&lt;/span&gt;家酒店&lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="comment_num"&gt;
                &lt;div class="comment_num_model"&gt;&lt;span class="num"&gt;{totalCommentNum}&lt;/span&gt;&lt;br&gt;&lt;i class="ico_num"&gt;&lt;/i&gt;点评总数&lt;/div&gt;
                &lt;div class="comment_num_model"&gt;&lt;span class="num"&gt;{picNum}&lt;/span&gt;&lt;br&gt;&lt;i class="ico_pic"&gt;&lt;/i&gt;上传图片&lt;/div&gt;
                &lt;div class="comment_num_model"&gt;&lt;span class="num"&gt;{usefulCommentNum}&lt;/span&gt;&lt;br&gt;&lt;i class="ico_useful"&gt;&lt;/i&gt;有用点评&lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;

</script>

 
 <script type="tpl" id="J_checkOthersCom">
    &lt;div class="comment_head_pop" style="position:absolute"&gt;
            &lt;div class="comment_head"&gt;
                &lt;span class="img"&gt;&lt;img width="74" height="74" src="{src}" alt=""&gt;&lt;/span&gt; 
                &lt;p class="name"&gt;{userName}&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="comment_info"&gt;
                &lt;div class="{userLevelLogo}"&gt;&lt;/div&gt;
                &lt;div class="skill"&gt;点评数量在{comRange}的用户。累积点评酒店即可升级。&lt;/div&gt; 
                &lt;div class="map"&gt;足迹遍布&lt;span class="orange"&gt;{cityNum}&lt;/span&gt;个城市，点评过&lt;span class="orange"&gt;{comhotcount}&lt;/span&gt;家酒店&lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="comment_num"&gt;
                &lt;div class="comment_num_model"&gt;&lt;span class="num"&gt;{totalCommentNum}&lt;/span&gt;&lt;br&gt;&lt;i class="ico_num"&gt;&lt;/i&gt;点评总数&lt;/div&gt;
                &lt;div class="comment_num_model"&gt;&lt;span class="num"&gt;{picNum}&lt;/span&gt;&lt;br&gt;&lt;i class="ico_pic"&gt;&lt;/i&gt;上传图片&lt;/div&gt;
                &lt;div class="comment_num_model"&gt;&lt;span class="num"&gt;{usefulCommentNum}&lt;/span&gt;&lt;br&gt;&lt;i class="ico_useful"&gt;&lt;/i&gt;有用点评&lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt; 
 </script>

<script type="tpl" id="J_traffic">
    &lt;div class="title"&gt;交通信息&lt;/div&gt; 
    &lt;div class="traffic_box"&gt;
        {{enum(key,places) $data}}
            {{if places.length &gt; 0}}
            &lt;div class="traffic_item"&gt;
                &lt;span class="spot_type ${key}"&gt;&lt;/span&gt;
                {{each(index,place) places}}
                &lt;p class="name"&gt;&lt;a href="javascript:;" class="rounte" data-name="${place.PlaceName}" data-lnglat="${place.Lon}|${place.Lat}" data-distance="${place.Distance}"&gt;路线&lt;/a&gt;${place.PlaceName}&lt;/p&gt;
                &lt;p class="distance"&gt;${place.ArrivalWay}&lt;/p&gt;
                {{/each}}
            &lt;/div&gt;
            {{/if}}
        {{/enum}}
    &lt;/div&gt;
 </script>

<script type="tpl" id="J_groupProuct">
    &lt;div class="sider_tuan"&gt;
        &lt;div class="sider_title"&gt;&lt;a href="${ProductMoreUrl}" class="more" target="_blank"&gt;更多&amp;nbsp;&lt;/a&gt;酒店周边美食团购&lt;/div&gt;
        &lt;ul class="sider_tuan_list"&gt;
            {{each(index,product) ProductList}}
            &lt;li&gt;
                &lt;a href="${product.ActivityUrl}" target="_blank"&gt;&lt;img src="${product.ActivityImageUrl}" width="62" height="62" alt="" onerror="this.src='//images4.c-ctrip.com/target/fd/tuangou/g6/M01/EC/B1/CggYtFcl8bmAZviXAAA7i47G0go720.jpg';this.onerror=null;"&gt;&lt;/a&gt;
                &lt;a href="${product.ActivityUrl}" class="tuan_name" target="_blank"&gt;${product.ActivityTitle}&lt;/a&gt;
                &lt;p class="tuan_num"&gt;已售${product.AcitivitySellCount}份&lt;/p&gt;&lt;p class="tuan_price"&gt;&lt;dfn&gt;&amp;yen;&lt;/dfn&gt;&lt;span class="price"&gt;${product.ActivityPrice}&lt;/span&gt;&lt;/p&gt;
            &lt;/li&gt;
            {{/each}}
        &lt;/ul&gt;
    &lt;/div&gt;
 </script>
<script type="tpl" id="J_favHotel">
    &lt;div id="favlist"&gt;
        &lt;div class="sider_title"&gt;
            &lt;a class="more" href="${$data[0].moreLink}" target="_blank"&gt;更多&lt;/a&gt;
            &lt;span id="favcount"&gt;我收藏的酒店(${$data[0].FavCount})&lt;/span&gt;
        &lt;/div&gt;
        &lt;ul class="sider_pic_list collect_list"&gt;
            {{each(index,hotel) $data}}
            &lt;li&gt;
                &lt;a onclick="DoFavHotel(this, event, 'D')" title="取消收藏" class="fav_del" href="javascript:void(0);" data-id="${hotel.HotelId}" data-favid="${hotel.HotelFavoriteId}"&gt;&lt;/a&gt; 
                &lt;a title="${hotel.HotelName}" class="sider_hotel_pic" href="${hotel.HotelUrl}" target="_blank" data-dopost="T"&gt;
                    &lt;img alt="" src="${hotel.LogoPic}"&gt;
                &lt;/a&gt;
                &lt;a title="${hotel.hotelName}" class="hotel_name" href="${hotel.HotelUrl}" target="_blank" data-dopost="T"&gt;${hotel.HotelName}&lt;/a&gt;
                &lt;span class="${hotel.CustomerEvalCss}" title="${hotel.CustomerEvalStr}"&gt;&lt;/span&gt;
            &lt;/li&gt;
            {{/each}}
        &lt;/ul&gt;
    &lt;/div&gt;
</script>

<script type="tpl" id="J_visitedHotel">
    &lt;div id="visitedHistory"&gt;
        &lt;div class="sider_title"&gt;我浏览过的酒店&lt;/div&gt;
        &lt;ul id="vistedHotels" class="sider_pic_list J_historyHotelsList"&gt;
            {{each(index,hotel) $data}}
            &lt;li hotel-id="${hotel.HotelId}" hotel-amount="0" class=""&gt;
              &lt;a id="ctl00_repeaterOtherPage_ctl00_linkDelete" class="delete" data-id="${hotel.HotelId}" href="javascript:void(0);"&gt;×&lt;/a&gt;
              &lt;a id="ctl00_repeaterOtherPage_ctl00_linkHotelPicture" class="sider_hotel_pic" title="${hotel.HotelName}" tracecodevalue="hi_br_1_i" name="needTraceCode" data-hotel="${hotel.HotelId}" href="/hotel/${hotel.HotelId}.html" target="_blank"&gt;
                &lt;img id="ctl00_repeaterOtherPage_ctl00_imgHotelPicture" src="${hotel.LogoUrl}" style="border-width:0px;width:36px; height:36px;"&gt;&lt;/a&gt;
              &lt;a id="ctl00_repeaterOtherPage_ctl00_linkHotelName" data-dopost="T" class="hotel_name" title="${hotel.HotelName}" tracecodevalue="hi_br_1_n" name="needTraceCode" data-hotel="${hotel.HotelId}" href="/hotel/${hotel.HotelId}.html" target="_blank"&gt;${hotel.HotelName}&lt;/a&gt;
              &lt;span class="${hotel.CustomerEvalCss}" title="${hotel.CustomerEvalStr}"&gt;&lt;/span&gt;
            &lt;/li&gt;
            {{/each}}
        &lt;/ul&gt;
    &lt;/div&gt;
 </script>

<script type="text/javascript" language="javascript">
    var isInternational = "T";
    var isIntGtaHotel = "T";
    //详情&amp;点评tab默认值
    
        var tabtype = 1; //酒店信息
    
    var isQuickBookUser = false;
    var urlCurrentPage = 1;
    var urlCommentType =0;
    var urlWrittingId = 0;
    var useNewCompare = 1;
    //列表页选择的免费无线免费有线等参数id
    var equip = "";
    window.__uidc_init = new Date * 1;
    var POPMAP_URL = '//webresource.c-ctrip.com/ResHotelOnline/R8/search/js.min/widget/popup-map.js?releaseno=2018-09-20-02-02-00';
    var SOSOMAP_URL = '//webresource.c-ctrip.com/ResHotelOnline/R8/search/js.min/sosoMap.js?releaseno=2018-09-20-02-02-00';
    var ISSSOQUICKLOGIN=0;
    var MAX_STAY = 28 * 24 * 3600 * 1000;
    var HAS_ROOM_RESULT = false;
    var isShowResult = true;
    var addressMessageConfig = {
        cityname: {
            suggestionB: '支持中文/拼音/简拼输入',
            suggestion: "&lt;strong&gt;热门城市&lt;/strong&gt;（可直接选择城市或输入城市全拼/简拼）"
        },
        searchHistory: '搜索历史',
        addressTab: "省市",
        hotelPos: {
            suggestion: "可直接选择地理位置或输入位置关键词",
            titles: {
                "zone": "商业区",
                "location": "行政区",
                "metro": "地铁线"
            },
            showAMap: false,
            AMapTitle: '查看商业区地图',
            all: '全部',
            subCity: '下辖市/县：'
        },
        defaultValue: ['上海','2','shanghai']
    };
    var validateMessageConfig = {
        hotel: {
            city: '请选择酒店所在城市',
            checkIn: '请选择入住日期',
            checkOut: '请选择离店日期',
            dateErr: '日期格式为yyyy-mm-dd',
            too_early_in: '入住日期不能早于今天',
            too_early_out: '您选择的离店日期早于/等于入住日期，请重新选择',
            too_long: '您入住酒店时间超过28天，请分订单提交预订',
            no_room: '您选择的日期没有房间可供预订!',
            room_num: '请选择预订房间数',
            noExistCity: '目的地{city}不存在'
        }
    };

    var noticeMessageConfig = ['中文/拼音', '输入或选择位置关键词', '名称/品牌 如:如家'];

    var roomMessageConfig = {
        noVisit: '暂无浏览记录',
        loading: '给力加载中，请稍候......',
        week:["，星期日","，星期一","，星期二","，星期三","，星期四","，星期五","，星期六","，今天","，明天","，后天"],
        noResult: '&lt;div class="tips_unresult"&gt;&lt;b&gt;&lt;/b&gt;酒店暂未公布价格，建议您选择其他酒店。&lt;/div&gt;'
    };
    var commentVersion = 'c';
    var commentMessageConfig = {
        loading: '点评载入中',
        noResult:'&lt;div class="comment_alert"&gt;此酒店暂时还没有携程入住客户点评。&lt;/div&gt;'
    };

   var mapMessageConfig = {
        temp: ['全程', '分钟', '约', '站', '换乘', '次'],
        license: 'GS（2010）1049号',
        distance: '实际距离为',
        noInfo: '暂无交通信息数据',
        traffic: ['公交', '驾车', '交换起始位置', '起：', '终：', '上行|下行']
    };
   
   var addressUrlConfig = {
       visitCount: '/domestic/tool/AjaxHotelVisitCount.aspx?hotelid=428365',
       imgMapUrl: '',
       mapIframe: '/Domestic/MapIframeDetail.aspx?city=2&amp;province=2',
       trafficinfo: '/Domestic/Tool/AjaxMapHotelTrafficinfo.aspx?hotelid=428365&amp;type=piloting',
       trafficline: '/Domestic/Tool/AjaxMapHotelTrafficinfo.aspx?typetraffic=$1&amp;hotelid=428365&amp;placeid=$2&amp;type=trafficline',
       roomlink:"/hotel-rtm$1/428365.html",
       order: '/DomesticBook/DomeInputNewOrderCS.aspx',  //下订单链接
       delayOrder: '/DomesticBook/InputDelayOrder.aspx', //下订单链接 
       //lvPingRecomand:"/Domestic/Tool/AjaxLvPingDemandNew.aspx?hotelid=428365",
       ajaxRoomList: '/Domestic/tool/AjaxHote1RoomListForDetai1.aspx?psid=&amp;MasterHotelID=428365&amp;hotel=428365&amp;EDM=F&amp;roomId=&amp;IncludeRoom=&amp;city=2&amp;showspothotel=T&amp;supplier=&amp;IsDecoupleSpotHotelAndGroup=F&amp;contrast=0&amp;brand=0',
       ajaxRoomListBaseUrl: '/Domestic/tool/AjaxHote1RoomListForDetai1.aspx?psid=&amp;MasterHotelID=428365&amp;hotel=428365&amp;EDM=F&amp;roomId=&amp;IncludeRoom=&amp;city=2&amp;supplier=&amp;showspothotel=T&amp;IsDecoupleSpotHotelAndGroup=F&amp;contrast=0&amp;brand=0',
       ajaxGroupRoomList:'/Domestic/Tool/AjaxGetGroupRoomList.ashx?psid=&amp;MasterHotelID=428365&amp;hotel=428365&amp;EDM=F&amp;roomId=&amp;IncludeRoom=&amp;city=2&amp;showspothotel=T&amp;supplier=&amp;IsDecoupleSpotHotelAndGroup=F&amp;contrast=0&amp;brand=0',
       ajaxCommentList: '/Domestic/tool/AjaxHotelCommentList.aspx?MasterHotelID=428365&amp;hotel=428365&amp;property=0&amp;card=0&amp;cardpos=0&amp;NewOpenCount=0&amp;AutoExpiredCount=0&amp;RecordCount=6518&amp;OpenDate=',
       ajaxGetPictureAlbum:'/Domestic/tool/AjaxLoadPictureAlbum.aspx?hotel=428365&amp;city=2&amp;istaiwan=0',
       ajaxGetHotelAddtionalInfo:'/Domestic/tool/AjaxGetHotelAddtionalInfo.ashx?commentData=1&amp;browseData=1&amp;routeData=1&amp;groupProductData=1&amp;favData=1&amp;provinceId=2&amp;cityId=2&amp;hotelId=428365&amp;lng=121.53983581837&amp;lat=31.298553330946&amp;ck=0%2c0%2c4.7%2c6518%2c%2fhotel%2f373000%2f372135%2fc3028fa548b34dd883e187498a1fe26e.jpg%2c&amp;hotelidlist=428365',
       AjaxGetHotelRelationInfo:'/Domestic/tool/AjaxGetHotelRelationInfo.aspx?city=2&amp;hotel=428365&amp;EDM=&amp;startdate=2018-09-21&amp;enddate=2018-09-22&amp;lat=31.298553330946&amp;lot=121.53983581837&amp;isghi=F&amp;brand=0',
       AjaxHotelComboInfo:'/Domestic/tool/AjaxHotelComboInfo.aspx',
       AjaxSHXDPInfo:'/Domestic/tool/AjaxGetSHXDPHotelRecommend.aspx?CityId=2&amp;HotelId=428365&amp;PayMode=P&amp;Latitude=31.298553330946&amp;Longitude=121.53983581837&amp;HotelName=%e4%b8%8a%e6%b5%b7%e5%b0%8f%e5%8d%97%e5%9b%bd%e8%8a%b1%e5%9b%ad%e9%85%92%e5%ba%97',
       AjaxPuzzle:'/Domestic/cas/puzzle',
       AjaxMeetingRooms:'/Domestic/Tool/AjaxMeetingRooms.ashx?hotel=428365&amp;star=5&amp;customereval=6',
       AjaxGHIGroupProduct:'/Domestic/tool/AjaxGetGHIFromGroup.aspx?Products=428365',
       MeetingDomain:'http://meeting.ctrip.com',
   	hyattUrl:"/flagship/hyatt"
   };
    //判断特惠标记
    var isFromHotSale = 'False';
    var IsOpenBaiDuMapFlgForGAT = "F";
    var IsOpenBaiDuMapFlg = "T";
    var IsGAT = "F";
    var IsLatlonOffset = "T";
    var isOpenRoomSort = 'T';
    var isNewBookSucessVer = '0';
    var DomesticCityId = '2';
    var isBookingInNewPage = '0';
    var rmsTokenSearch = '';

    //团购房型获取方式开关
    var IsAjaxGetGroupRoomList = 'True';

    var hotelDomesticConfig = {
        
        isLocalhost: 0,
        webResourceReleaseNo: '20130508',
        popMapFlag: 1,
        hotel: {
            id: "428365",
            name: "上海小南国花园酒店",
            position: "121.53983581837|31.298553330946",
            vacationsDP:"true"
        },
        query: {
            cityId:'2',
            checkIn:'2018-09-21', 
            checkOut:'2018-09-22'
        },
        cas:{
            EnableDescartes:true,
            NeverMore: true,
            Pretty: false,
            decrypt: true,
            testSwitch: {
                CAT:undefined,
                sniffing:false
            },
            MainSwitch: {
                jsTemplate:false,
                SXX: false
            },
            BI:{
                SXX: '/Domestic/CAS/Image/SXX'
            },
            OceanBall:true,
            OceanBallUrl: '/domestic/cas/oceanball'
        },
        EDM:'',
        nearFacility: '',
        istaiwan :'0',
        isghi:'F',
        bookingOver : false,
        bookOverView : false,
        bookOverView : false,
        SHXDPFocus:false,
        bookOverView : false
    };

    var HotelMapStreetJson={"428365":{"amap":{"pos":"121.53983581837|31.298553330946","label":"上海小南国花园酒店","fullname":"上海小南国花园酒店"},"soso":{"pano":"10021010130616095856000","zoom":1,"heading":159,"pitch":-1,"pos":"121.53983581837|31.298553330946"}}};

    var HotelMaiDianData = {
    	key: 'hotel_inland_detail_basic_online',
    	value: {
    		datetime: '2018-09-21 16:14:13',
    		cityid: '2',
            cityname: '上海',
            starttime: '2018-09-21',
            endtime: '2018-09-22',
            productid: '428365',
            star: '5',
            brand: '0',
            amount: '',
            country: '1',
            hotellon: '121.53983581837',
            hotellat: '31.298553330946',
            roomnum: '',
            rnum: '',
            pnum: '',
            mnum: '',
            cnum: '',
            bookable_cx: '',
            bookable_zl: '',
            price_cx: '',
            price_zl: '',
            credit:'',
            loadtime: '09-21-2018 08:14:13 UTC',
        	abnorm_condition: '',
        	listproductid: '',
        	listroomid: '',
        	listshadowid: '',
        	listBookable: '',
        	liststarttime: '',
        	listendtime: '',
        	listhasfilters: '',
        	listismemberlogin: '',
        	listdatetime: ''

        }    
    };
    
    function loadCallback(){ 
        (function(){
            try{
                initialAdvertiseIds();
                $("#list a").bind("click",function(e){
                    var adid = $(this).attr("data-adpos-id"); 
                    var advValue ="version=1.0&amp;channelid=4&amp;moduleid=hod_dl_ad_def&amp;hoteladvertiseid="+adid;
                    _tracklog("hotel.adclick",advValue);
                });
            }
            catch(e){}       
        })();

        window.__rmsbfi = window.__rmsbfi || [];
        window.__rmsbfi.push(['_getRmsToken', function (rmsToken) {
            rmsTokenSearch = rmsToken;
        }]); 

        $.mod.load('sideBar', '2.0', function () {
            var sidebar = $(document).regMod('sideBar', '2.0', {
                HTML: '&lt;div class="side_fixed" id="sidebar"&gt;\
					&lt;a class="to_top" title="${backTop}" href="javascript:;" rel="nofollow" id="gotop2"&gt;&amp;nbsp;&lt;/a&gt;\
					&lt;a target="_blank" class="c_sidebar" href="${feedBackURL}" rel="nofollow" title="${feedBack}"&gt;${feedBack}&lt;/a&gt;\
					&lt;a target="_blank" class="c_sidebar" href="${liveChatURL}" rel="nofollow" title="${liveChat}"&gt;${liveChat}&lt;/a&gt;\
				&lt;/div&gt;',
                url: {
                    feedBackURL: '//my.ctrip.com/uxp/Community/CommunityAdvice.aspx?producttype=3&amp;sourceid=2&amp;hotelid=428365',
                    liveChatURL: '//livechat.ctrip.com/livechat/Login.aspx?GroupCode=HotelLocal&amp;amp;AsFrom=1%7c%d6%d0%ce%c4%be%c6%b5%ea%7c%be%c6%b5%ea%ca%d7%d2%b3%7c%7c+%7c+%7c+%7c+%7c'
                },
                title:
                {
                    liveChat:'在线咨询',
                    feedBack: '建议反馈'
                },
                bgSrc:
                {
                   src: '//pic.c-ctrip.com/htlpic/common/un_sidebar.png'
                },
                bottom_px: 100,
                CSS:'.side_fixed{position:fixed;right:20px;bottom:100px;z-index:9999;width:35px;}\
			        .to_top,.c_sidebar{background-image:url(${src});_background-image:url(${srcIE6});background-repeat:no-repeat;}\
			        .to_top{position:relative;float:left;clear:both;width:35px;height:0;margin-bottom:2px;padding-top:35px;overflow:hidden;cursor:pointer;z-index:2;visibility:hidden;background-position:0 0;}\
			        .to_top:hover{background-position:-79px 0;}\
			        .c_sidebar{display:inline-block;width:35px;height:32px;padding-top:3px;margin-bottom:2px;overflow:hidden;vertical-align:top;font-size:12px;color:#fff;background-position:0 -37px;text-align:center;text-decoration:none;line-height:14px;}\
			        .c_sidebar:hover{background-position:-79px -37px;}\
			        .c_sidebar_hl{background-position:-40px -37px;}'
            });
        });
        
        PageLoad.initPage();
        PageLoad.initHotelComment();
        DetailPage.init({});
        
        
        var ref = '';
        var res = (window.location + "").match(/#ctm_ref=([^&amp;#]*)/i); //hd_0_0_0_0_lst_sr_1_df_pe_1_i_hi_0_0_0
        if (res) {
            ref = res[1] || '';
        }
        hotelDomesticConfig['ref'] = ref; 
        PageLoad.initRoom()
        
        
        if (tabtype == 4) {
            $('#linkViewMap').click();
        }

        PageLoad.initComplete();

        logTimer();
        
        
        window.bd_cpro_rtid="nW03n1D";
        
        var param = {
            type: 'text/javascript',
            async: true
        }
        cQuery.loader.js('//cpro.baidu.com/cpro/ui/rt.js', param);
        
        LoadAjaxGetHotelRelationInfo();
        
        window.$_bf.tracklog("hotel.detail", "UID=${duid}&amp;page_id=${page_id}&amp;VERSION=1&amp;HotelId=428365&amp;From=上海&amp;Star=5&amp;CityId=2&amp;Price=0&amp;PositionType=zone&amp;PositionId=368&amp;FromTime=2018-09-21&amp;ToTime=2018-09-22&amp;CityId=2");
    }

    var $globalPad = true; //support ctrip on pad
    var $isPad = /pad/.test(navigator.userAgent.toLowerCase());
    $LAB.script({ src: '//webresource.c-ctrip.com/code/cquery/cQuery_110421.js', charset: 'utf-8' }).wait()
        .script({ src: '//webresource.c-ctrip.com/reshotelcasonline/R6/js/butterfly.js?releaseno=2018-09-20-02-02-00', charset: 'utf-8' }).wait()
        .script({ src: '//webresource.c-ctrip.com/ResHotelOnline/R8/search/js.merge/base-bmap.js?releaseno=2018-09-20-02-02-00', charset: 'utf-8' }).wait()
.script({ src: '//webresource.c-ctrip.com/ResHotelOnline/R8/search/js.merge/showhotelinformation.js?releaseno=2018-09-20-02-02-00', charset: 'utf-8' }).wait(loadCallback);
</script>

<script type="text/javascript">
    function initialAdvertiseIds()
    { 
        var valueIds = '';
        if(valueIds != ''){
            var advValue ="version=1.0&amp;channelid=4&amp;moduleid=hod_dl_ad_def&amp;hoteladvertiseid_list="+valueIds;
            _tracklog("hotel.adimpression",advValue);
        }
    }

    //class为 list 的a标签bindclick
      
    function _tracklog(key,value){
        if(typeof window['__bfi'] == 'undefined') window['__bfi'] = [];
        window['__bfi'].push(['_tracklog', key, value]);
    };

    function hiddenAdvertise(boxName) {
        if(boxName){
            $("." + boxName).addClass("hidden");
        }else{
            $(".discount_box").addClass("hidden");
        }
    }
</script>

<script src="//webresource.c-ctrip.com/ResHotelOnline/R8/search/js.min/twemoji/twemoji.min.js?releaseno=2018-09-20-02-02-00"></script>    

<script>var getuseridentityresult=function (){return 0;}</script>

<noscript>
&lt;div style="display:none;"&gt;
&lt;img height="0" width="0" style="border-style:none;" src="//eclick.baidu.com/rt.jpg?t=noscript&amp;rtid=nW03n1D" /&gt;
&lt;/div&gt;
</noscript>

<div style="display:inline;">
<img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/1066331136/?value=0&amp;label=cG9hCIyRngMQgNi7_AM&amp;guid=ON&amp;script=0" />
</div>
<script type="text/javascript" src="//webresource.c-ctrip.com/ResCRMOnline/R6/member/common/js/mask_young.js?20140603" charset="gb2312"></script><div class="login_popup" id="sso_maskDIv" style="display:none"><div class="lg_main" id="sso_memberlogin"><div class="lg_hd"><div class="lg_sale"><i class="lg_ico_sale"></i>登录可享：积分换礼、预订返现、更快速的预订</div></div><div class="lg_switch"><label class="lg_label" id="sso_domUser"><input type="radio" name="1" checked="checked" id="sso_memberRadio" />普通登录</label><label class="lg_label" id="sso_phonePwd"><input type="radio" name="1" id="sso_cardRadio" />手机动态密码登录</label></div><ul class="lg_form" id="sso_domUserUl"><li><label class="lg_form_label">登 录 名</label><input type="text" id="sso_txtUid" value="用户名/卡号/手机/邮箱" class="lg_input_text lg_input_unfocus" /></li><li><label class="lg_form_label">密   码</label><input type="password" class="lg_input_text" id="sso_txtPwd" maxlength="20" onpaste="return false;" onkeydown="sso_member_enter();" oncontextmenu="return false;" oncopy="return false;" oncut="return false;" /> <a href="https://accounts.ctrip.com/member/PassWord/VerifyUserInfo.aspx" id="sso_forgetPwd" target="_blank">忘记密码？</a> </li><li id="sso_divVerifyCode" style="display: none;"><label class="lg_form_label">验 证 码</label><input type="text" class="lg_input_text lg_input_small lg_input_unfocus" maxlength="6" name="verifyCode" id="sso_verifyCode" autocomplete="off" value="不区分大小写" onkeydown="sso_member_enter();" /><img width="88" height="32" alt="" id="sso_imgCode" /></li><li id="sso_domErrorli" style="display: none;"><div class="lg_form_wrap"><div class="base_error" id="sso_membererror" style="visibility: hidden;"><i class="lg_ico_alert"></i>登录名或密码错误</div></div></li><li><div class="lg_form_wrap"><label class="lg_label"><input type="checkbox" name="" checked="checked" id="sso_chkAutoLogin" />30天内自动登录</label></div></li><li class="lg_form_btn"><div class="lg_form_wrap"><input type="button" value="登 录" class="lg_btn" id="sso_btnSubmit" /> <a href="javascript:;" id="sso_register">免费注册</a></div></li></ul><ul class="lg_form" style="display: none;" id="sso_phonePwdUl"><li><label class="lg_form_label">手 机 号</label><input type="text" class="lg_input_text lg_input_unfocus" id="sso_mobilePhone" value="请输入注册手机号" /></li><li id="sso_phoneCodeLi" style="display:none"><label class="lg_form_label">验 证 码</label><input type="text" class="lg_input_text lg_input_small lg_input_unfocus" maxlength="6" id="sso_txtCodePwd" value="不区分大小写" /> <img width="88" height="32" alt="" id="sso_imgCodePhone" /></li><li><label class="lg_form_label">密   码</label><input type="password" id="sso_dyPwdFirst" onkeydown="sso_phone_enter();" class="lg_input_text lg_input_small lg_input_unfocus" /> <a href="javascript:;" class="lg_btn3" id="sso_reSend">发送动态密码</a> </li><li id="sso_phoneLoginErr" style="display: none"><div class="lg_form_wrap" style="display: ;"><div class="base_error" id="sso_dymembererror"><i class="lg_ico_alert"></i>登录名或密码错误</div></div></li><li id="sso_phoneLoginTip" style="display: none"><div class="lg_form_wrap" style="display: ;"><div class="base_success"><i class="lg_ico_success"></i>动态密码已发送至您的手机，请注意查收。</div></div></li><li><div class="lg_form_wrap"><label class="lg_label"><input type="checkbox" name="" checked="checked" id="sso_chkAutoLoginDy" />30天内自动登录</label></div></li><li class="lg_form_btn"><div class="lg_form_wrap"><input type="button" value="登 录" class="lg_btn" id="sso_btnSubmitLogin" /> <a href="javascript:;" id="sso_register2">免费注册</a></div></li></ul><div class="lg_others">其他登录： <a href="javascript:;" id="sso_clogin">合作卡</a> | <a href="http://ct.ctrip.com/crpTravel/zh-cn" target="_parent" id="sso_corpLogin">公司客户</a> | <a href="javascript:;" id="sso_tlogin">第三方帐号</a></div></div><div class="lg_main" id="sso_commonlogin" style="display: none"><div class="lg_hd"><strong>合作卡登录</strong></div><input type="hidden" id="sso_hidSourceId" name="sso_hidSourceId" value="1" /><ul class="lg_form"><li><label class="lg_form_label">合 作 卡</label><input type="text" id="sso_cardName" class="lg_input_text lg_input_unfocus" value="中文/拼音" /></li><li><label class="lg_form_label">登 录 名</label><input type="text" id="sso_txtCUid" value="用户名/卡号/手机/邮箱" class="lg_input_text lg_input_unfocus" /></li><li><label class="lg_form_label">密   码</label><input type="password" class="lg_input_text" maxlength="20" id="sso_txtcPwd" onpaste="return false;" oncontextmenu="return false;" oncopy="return false;" onkeydown="sso_card_enter();" oncut="return false;" /> <a href="javascript:;" id="sso_lkbtnGetPwd">忘记密码？</a> </li><li id="sso_cardError" style="display: none"><div class="lg_form_wrap" style="display: ;"><div class="base_error" id="sso_commonerror"><i class="lg_ico_alert"></i>登录名或密码错误</div></div></li><li class="lg_form_btn"><div class="lg_form_wrap"><input type="button" value="登 录" class="lg_btn" id="sso_btnCSubmit" /> </div></li></ul><div class="lg_others"><a href="javascript:;" class="lg_goback" id="sso_mlogin">&lt; 返回普通会员登录</a></div></div><div class="lg_main" id="sso_thirdlogin" style="display: none"><div class="lg_hd"><strong>第三方账号登录</strong></div><ul class="lg_account_list"><li><a href="javascript:;"><span><i class="lg_ico_sina" id="sso_sina"></i></span>新浪微博</a></li><li><a href="javascript:;"><span><i class="lg_ico_qq" id="sso_qq"></i></span><p>QQ</p></a></li><li><a href="javascript:;"><span><i class="lg_ico_renren" id="sso_renren"></i></span><p>人人网</p></a></li><li><a href="javascript:;"><span><i class="lg_ico_baidu" id="sso_baidu"></i></span><p>百度</p></a></li><li><a href="javascript:;"><span><i class="lg_ico_wangyi" id="sso_nete"></i></span><p>网易</p></a></li></ul><div class="lg_others"><a href="###" class="lg_goback" id="sso_mlogin2">&lt; 返回普通会员登录</a></div></div><div class="lg_side" id="sso_lg_side"><p>非会员预订</p><p><a href="javascript:;" class="lg_btn2" id="sso_btnDirectBook">不登录，直接预订 &gt;</a></p></div><a href="javascript:;" class="lg_close" id="sso_divClose">×</a></div><iframe id="sso_ifrprocxy" style="display: none;"></iframe><script type="text/javascript" src="//webresource.c-ctrip.com/ResCRMOnline/R6/member/common/js/Globle_young.js?20171226" charset="utf-8"></script><script type="text/javascript" src="//webresource.c-ctrip.com/ResCRMOnline/R6/member/common/js/client_young.js?20150924" charset="utf-8"></script><script type="text/javascript" src="//webresource.c-ctrip.com/ResCRMOnline/R6/member/common/js/cocardlist.js?20171019" charset="utf-8"></script><script type="text/javascript" src="//webresource.c-ctrip.com/ResCRMOnline/R6/member/common/js/CrossDomainCookie.js?20161208" charset="utf-8"></script>
<input type="hidden" id="HideIsNoneLogin" name="HideIsNoneLogin" value="T" />
<input type="hidden" id="sso_loginprocxyPath" name="sso_loginprocxyPath" value="http://hotels.ctrip.com/Domestic/loginprocxy.html" />
<script type="text/javascript">;(function(){window.onload = function(){ var ifr = document.createElement('iframe');ifr.id='J_test';ifr.style.display='none';ifr.src = '/Domestic/cas/TableTennis';document.body.appendChild(ifr);}})()</script>

    </form>
    <div id="base_ft">
  <p><a href="http://pages.ctrip.com/public/sitemap/sitemap.htm" target="_blank" title="网站导航">网站导航</a> | <a href="http://hotels.ctrip.com/jiudian/" target="_blank" title="宾馆索引">宾馆索引</a> | <a href="http://flights.ctrip.com/booking/hot-city-flights-sitemap.html " target="_blank" title="机票索引">机票索引</a> | <a href="http://pages.ctrip.com/public/sitemap/dj.html" title="旅游索引">旅游索引</a> | <a href="http://ct.ctrip.com/crptravel/sitemap.html" title="商旅索引">商旅索引</a> | <a title="攻略索引" href="http://you.ctrip.com/sitemap/">攻略索引</a> | <a rel="nofollow" href="http://pages.ctrip.com/public/ctripab/abctrip.htm" target="_blank" title="关于携程">关于携程</a> | <a rel="nofollow" target="_blank" href="http://pages.ctrip.com/commerce/promote/201201/other/qygm/index.html" title="企业公民">企业公民</a> | <a rel="nofollow" target="_blank" title="诚聘英才" href="http://job.ctrip.com/">诚聘英才</a> | <a rel="nofollow" title="智慧旅游" href="http://you.ctrip.com/Intelligence.html">智慧旅游</a> 
      | <a rel="nofollow" target="_blank" href="http://u.ctrip.com/" title="分销联盟">分销联盟</a> | <a rel="nofollow" target="_blank" href="http://pages.ctrip.com/public/dlhz.htm" title="代理合作">代理合作</a> | <a target="_blank" href="http://ct.ctrip.com" title="企业商旅">企业商旅</a> | <a target="_blank" href="http://ct.ctrip.com/crptravel/default/landing" title="中小企业差旅">中小企业差旅</a> | <a rel="nofollow" target="_blank" href="http://pages.ctrip.com/public/ctripad/adyw.htm" title="广告业务">广告业务</a> | <a rel="nofollow" target="_blank" href="http://pages.ctrip.com/public/contact.htm" title="联系我们">联系我们</a></p>
  <p><a rel="nofollow" href="http://pages.c-ctrip.com/cooperation/web/cooperation.html#ctm_ref=ctr_hp_btm_coop" target="_blank">加盟合作</a> | <a rel="nofollow" href="http://join.easytrip.com/jiameng/#ctm_ref=ctr_def_btm_hsu_n_1" target="_blank" title="酒店加盟">酒店加盟</a> | <a rel="nofollow" href="http://dst.ctrip.com/">目的地及景区合作</a> | <a rel="nofollow" href="http://pages.ctrip.com/public/serve%20guideline.htm" target="_blank" title="用户协议">用户协议</a> | <a rel="nofollow" href="http://pages.ctrip.com/public/serve%20guideline.htm" target="_blank" title="隐私政策">隐私政策</a> | <a rel="nofollow" target="_blank" href="http://pages.ctrip.com/public/diploma/company.htm">营业执照</a> | <a rel="nofollow" target="_blank" href="http://pages.ctrip.com/tour/ingroupline_pages.asp?folder=ingroup0904&amp;file=0177" title="旅游度假资质">旅游度假资质</a> | <a rel="nofollow" target="_blank" href="https://insurance.ctrip.com/portal/index.aspx">保险代理</a> | <a target="_blank" href="http://pages.ctrip.com/public/link/ctrip_link.html">友情链接</a> | <a rel="nofollow" href="http://pages.ctrip.com/public/copyright.htm" id="copyright">Copyright©</a>1999-2018, <a href="http://www.ctrip.com/">ctrip.com</a>. All rights reserved. | <a rel="nofollow" target="_blank" href="http://www.miibeian.gov.cn/">ICP证：沪B2-20050130</a></p>
  <p class="gns"><a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31010502002731"><i class="icon-gns"></i>沪公网备31010502002731号</a></p>
  <div class="honour_wrap"><a href="http://www.ca-sme.com/index.credit?action=certDetail&amp;id=40288084605466f1016057ea4cb20021" class="honour1" target="_blank" rel="nofollow">信用评级</a><a href="http://www.sgs.gov.cn/lz/licenseLink.do?method=licenceView&amp;entyId=20110428175405415" title="工商亮照标识" class="honour2" target="_blank" rel="nofollow">上海工商</a><a href="http://credit.szfw.org/CX20111018000615000623.html" title="诚信认证示范企业" class="honour3" target="_blank" rel="nofollow">诚信网站</a><a href="http://www.zx110.org/" class="honour4" target="_blank" rel="nofollow" title="征信网">网络社会征信网</a><a href="http://www.shjbzx.cn/" class="honour5" target="_blank" rel="nofollow" title="上海市互联网违法与违规信息举报中心">信息举报中心</a><a href="https://ss.knet.cn/verifyseal.dll?sn=e12061531010025926306977" class="honour6" target="_blank" rel="nofollow" title="可信网站">可信网站</a><a href="http://www.12377.cn/" class="honour8" title="违法和不良信息举报中心" target="_blank" rel="nofollow">违法和不良信息举报中心</a></div>
</div><config id="timespan" value="20160329"></config><!--InstanceEnd name="position"--><script type="text/javascript">var globalConfig={AjaxUrl:'accounts.ctrip.com',PassportUrl:'passport.ctrip.com',H1:'https',H3:'my.ctrip.com',Lang:'gb2312'};</script><script type="text/javascript" src="//webresource.c-ctrip.com/ResCRMOnline/R1/pageheader/js/ActivityController.js?temp=1536663142" charset="utf-8"></script>
    
 


<div class="hidden" id="mask" style="width:100%; height:100%; position:fixed; _position:absolute; top:0; left:0; z-index:999; background:rgba(0,0,0,.5)"></div><input type="hidden" id="htl_detail_htl_hotel" value="pageid=102003;ht=428365;checkin=2018-09-21;checkout=2018-09-22;rmlist=[{&quot;rm&quot;:&quot;69643394&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:779,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;0&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69643394&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:802,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;0&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;4417042&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:841,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;0&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;73575856&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:892,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;1&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;211949554&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:935,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;1&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;F&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69643397&quot;,&quot;shadowid&quot;:&quot;1001021205&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:967,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;F&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;F&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69643397&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:991,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;2948177&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1028,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;202226980&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1235,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;F&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;0&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;F&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565417&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1384,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;0&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565361&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1410,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;0&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;73575861&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1520,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;1&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565418&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1499,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565418&quot;,&quot;shadowid&quot;:&quot;1001021205&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1566,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;F&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;F&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565363&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1510,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;2160243&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1706,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565349&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1452,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;0&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565408&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:2121,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;0&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565410&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:2178,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565352&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:2203,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;182899191&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:2526,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;F&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;F&quot;,&quot;isgift&quot;:&quot;F&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565413&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1816,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;3&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565354&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1789,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大/双&quot;,&quot;breakfast&quot;:&quot;3&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565413&quot;,&quot;shadowid&quot;:&quot;1001031205&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:1800,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;F&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;3&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;F&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69647146&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:2556,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;多床&quot;,&quot;breakfast&quot;:&quot;4&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;69565359&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:2702,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;多床&quot;,&quot;breakfast&quot;:&quot;4&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;78143116&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:6396,&quot;pt&quot;:&quot;FG&quot;,&quot;mt&quot;:&quot;0.0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;T&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;},{&quot;rm&quot;:&quot;78143132&quot;,&quot;shadowid&quot;:&quot;0&quot;,&quot;rpfq&quot;:0,&quot;rpfh&quot;:6570,&quot;pt&quot;:&quot;PP&quot;,&quot;mt&quot;:&quot;0&quot;,&quot;pn&quot;:&quot;0.0&quot;,&quot;promotiontype&quot;:&quot;0&quot;,&quot;iscomfirm&quot;:&quot;T&quot;,&quot;bedtype&quot;:&quot;大床&quot;,&quot;breakfast&quot;:&quot;2&quot;,&quot;policy&quot;:&quot;不可取消&quot;,&quot;guaranteetype&quot;:&quot;F&quot;,&quot;bk&quot;:&quot;T&quot;,&quot;isgift&quot;:&quot;T&quot;,&quot;isgroup&quot;:&quot;F&quot;}]" /><input type="hidden" id="htl_detail_htl_hotel_baseroom" /><input type="hidden" id="htl_detail_htl_hotel_rollingscreen" value="" /><input type="hidden" id="htl_detail_recom_notik" value="" /><input type="hidden" id="htl_detail_htl_hotel_comment" /><input type="hidden" id="htl_detail_htl_hotel_hotelrecommend" /><input type="hidden" id="hod_detail_picture" /><div id="uid_15375176543012911747291"><style>#uid_15375176543012911747291 .side_fixed{position:fixed;right:20px;bottom:100px;z-index:9999;width:35px;}			        #uid_15375176543012911747291 .to_top,#uid_15375176543012911747291 .c_sidebar{background-image:url(//pic.c-ctrip.com/htlpic/common/un_sidebar.png);_background-image:url(//pic.c-ctrip.com/common/un_sidebar_8.png);background-repeat:no-repeat;}			        #uid_15375176543012911747291 .to_top{position:relative;float:left;clear:both;width:35px;height:0;margin-bottom:2px;padding-top:35px;overflow:hidden;cursor:pointer;z-index:2;visibility:hidden;background-position:0 0;}			        #uid_15375176543012911747291 .to_top:hover{background-position:-79px 0;}			        #uid_15375176543012911747291 .c_sidebar{display:inline-block;width:35px;height:32px;padding-top:3px;margin-bottom:2px;overflow:hidden;vertical-align:top;font-size:12px;color:#fff;background-position:0 -37px;text-align:center;text-decoration:none;line-height:14px;}			        #uid_15375176543012911747291 .c_sidebar:hover{background-position:-79px -37px;}			        #uid_15375176543012911747291 .c_sidebar_hl{background-position:-40px -37px;}</style><div class="side_fixed" id="sidebar" style="bottom: 100px; right: 5px;">					<a class="to_top" title="回到顶端" href="javascript:;" rel="nofollow" id="gotop2" style="visibility: hidden;"> </a>					<a target="_blank" class="c_sidebar" href="//my.ctrip.com/uxp/Community/CommunityAdvice.aspx?producttype=3&amp;sourceid=2&amp;hotelid=428365" rel="nofollow" title="建议反馈">建议反馈</a>					<a target="_blank" class="c_sidebar" href="//livechat.ctrip.com/livechat/Login.aspx?GroupCode=HotelLocal&amp;AsFrom=1%7c%d6%d0%ce%c4%be%c6%b5%ea%7c%be%c6%b5%ea%ca%d7%d2%b3%7c%7c+%7c+%7c+%7c+%7c" rel="nofollow" title="在线咨询">在线咨询</a>				</div></div><div class="fl_open_wrap" style="display: none;"><div class="fl_open_wrap_cntr" id="appd_wrap_open_cnt" style="left: -100%;"></div></div><input type="hidden" id="abTestValue" value="abTestValue_Value" /><input type="hidden" id="qrcodeLink" value="http://m.ctrip.com/m/c3" /><input type="hidden" id="channel" value="自然" /><input type="hidden" id="codeImgKey" value="Cqof8juQ1537517657871" /><div class="fl_pop_wrap" id="appd_wrap_default" style="display: block;"><div class="fl_pop_wrap_cntr" id="fl_pop_wrap_cntr" style="left: 0px;"><div class="fl_pop_wrap_cntr_bg" id="fl_pop_wrap_cntr_bg"></div><div class="fl_pop_box"><div class="fl_pop_pic"><img id="imgAll" src="//images4.c-ctrip.com/img3/marketing/2016/01/float_new_year/guoneijiudian_480x194.png" /></div><div class="fl_pop_cnt"><div class="fl_pop_cnt_bg"></div><div class="fl_pop_form"><div class="fl_pop_ttl">下载携程旅行手机版<a href="http://app.ctrip.com/"><span>Pad</span>及手机网络版 &gt;</a></div><div>下载地址至手机</div><div class="fl_pop_items"><input type="text" placeholder="请输入11位手机号" id="popfloating_phone_num" value="" class="fl_pop_input_phone" /><div class="fl_pop_submit"><input type="text" id="authCodeImgInput" placeholder="动态验证码" value="" class="fl_pop_input_secode" /><div class="float_pop_secode"><img width="90" height="38" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAyAKADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigAooooAKKKjnnhtbeW4uJY4YIkLySSMFVFAySSeAAOc0ASUVwc/xn+H1tcSwP4ijLxuUYx20zqSDjhlQhh7gkHtXWaNrml+IdOS/0i/gvbVsDfC+dpIB2sOqtgjKnBGeRQBoUUVyev8AxL8H+F9UbTNY1qOC8VA7RLDJKUB6btikA45wecEHoRQB1lFZel+I9I1nw+uvWV9G2lsjv9pkBiUKhIYneAQAVPJx0rl5/jP8Pra4lgfxFGXjcoxjtpnUkHHDKhDD3BIPagDvKKz9G1zS/EOnJf6RfwXtq2BvhfO0kA7WHVWwRlTgjPIqPX/EekeFtLbUtavo7S0DhN7AsWY9AqqCWPU4APAJ6A0AalFcv4b+InhXxdqMlhoeq/a7qOIzMn2eWPCAgE5dQOrD866igAooooAKKKKACiiigAooooAK8v8Aj5Y6pffDVhpsc8kcN2k16sLf8sFV8lh/EobYx64xu6LkeoV4n+0X4h1LTNG0bS7K5kt4NQec3LROyM6oqrsOCAUIlOQQc4HpyAeEaVJoA8MeIItRhkOsMkDaXKC21SJB5qnBxkocjcCPlPIOM+qfs3WOqf8ACQ6tfrHONINp5Mj7sRtPvQqMfxMF3+u0N23DPP8Agrwf4W1j4S+LNc1Sfbq1hu8g/aQnk4QNH8vfzHJT5s5xhcHJqT4DeIdSsfiHZ6NFcyHT79JhLbs7bAwjL71XON/7tVyQeCR9AD3P4m/ES3+H2hxyiH7Rqd5uSyhYHYSuNzuR/Cu5eAcnIAxyw+RNQhvsw39+ZHfUUa6SaSTe0w8x0Zyck53o/XnjPfNdJ8RNZvNQ+J2s3GpP9uW01CW3jhmJCCGORgsfykELgc7SCck5ySaz/F3i688Y6jaXl5Z2Nn9ltEs4YbGIxxrGpYqApY4xuI44wBxQB6hf2OqX37K+iDTY55I4buSa9WFv+WCyz5LD+JQ2xj1xjd0XI8r0qTQB4Y8QRajDIdYZIG0uUFtqkSDzVODjJQ5G4EfKeQcZ0G+Imvf8IHa+D4JI7XT4HcmS3Z0lmVy5ZHIbDIfMPGOwrpPBXg/wtrHwl8Wa5qk+3VrDd5B+0hPJwgaP5e/mOSnzZzjC4OTQBsfs+fbNM1HX9fufPh8PW2nv9qn58vzFKuPlH3mVN54BIDdtwzyfxD8Y33xK1661O2tpItL0u3zFC8nMcRkVPMYZxvZpEBC9to527q4+PVtSh0ubS4tQu00+Z98toszCJ245ZM4J+VeSOw9K2LXxlc2Xgi+8K2+m6bHb37o91diN/tEpRw65bfjAxgDbjBPckkA7z9nH/koeof8AYKk/9GxV9P18SeCvGupeA9Zm1TS4LSaeW3a3ZbpGZQpZWyNrKc5Qd/WvtugAooooAKKKKACiiigAooooAK5/xj4O0vxxof8AZOreesKyrNHJA+143GRkZBB4LDkHr64I6CigD5//AOGZf+pu/wDKb/8Aba9E8A/CnRfAFxJfWlxd3eoTW6wSzTMAoGQW2IBwGYA8liMAZ657yigAry/4j/B//hYHiG31b+3fsHk2i23lfZPNzh3bdnev9/GMdq9QooA8/i+E+lz/AAzsPBerXk91DZytNHdwDyXDl3bIBLDpIy85654OMef/APDMv/U3f+U3/wC219AUUAcH4B+FOi+ALiS+tLi7u9Qmt1glmmYBQMgtsQDgMwB5LEYAz1zueNvDH/CY+EL7QPtn2P7V5f7/AMrzNu2RX+7kZztx1710FFAHl/w4+D//AAr/AMQ3Grf279v860a28r7J5WMujbs72/uYxjvXqFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH//2Q==" id="authCodeImg" /></div><a class="fl_pop_btn_normal" id="popfloating_send_msg" href="javascript:;">免费获取</a><a class="fl_pop_btn_normal fl_pop_btn_disabled" href="javascript:;" title="为避免频繁发送，请稍后再试">免费获取</a></div><div class="fl_pop_phone_tip" id="popfloating_show_msg" style="display:none;"><span class="fl_pop_ico_arrow"></span><i class="fl_pop_ico_alert"></i></div><div class="fl_pop_secode_tip" id="popfloating_show_msg_codetip" style="display:none;"><span class="fl_pop_ico_arrow"></span><i class="fl_pop_ico_alert"></i></div><div class="fl_pop_sucess_tip" id="msg_sucess" style="display:none"><i class="fl_pop_ico_sucess"></i>下载链接短信已成功发送到您的手机！</div></div></div><div class="fl_pop_qrcode"><div class="fl_pop_hint">扫描二维码下载</div><div style="position:relative;background-color:white;width:115px;height:115px;margin-top: 7px;"><img src="//webresource.c-ctrip.com/ResUnionOnline/R3/float/pic/log.png" style="position:absolute;left:40px;top:40px;z-index:999;width:35px;height:35px;" /><div id="popfloating_float_img"><canvas width="103" height="103" style="display: none;"></canvas><img alt="Scan me!" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGcAAABnCAYAAAAdQVz5AAAH90lEQVR4Xu2d0XbiMAxEy/9/dPcApY0daXJHMZTT1T5uE9vxSKMZOcDl4+Pj8+PEv8/P8fbL5bIbbb4mmm6+b3uP+ts8ljt/dP085mMtj2uj55n/RsY92vbrTjY4B7v06+CQ6H48wzYqyMKj+x7/l90fzeFmHMmqeR1H0ZyNqRikurffmVMdoMG50/hLwFFcOQNxtKiMu1V0kppBsoo8x3UdTj1TmUvAIWvaXrPLHHcAIggc6mhwfgTVcnBIXYoikNCjEzhEUW3XQdSVGjOroVt2cdZ/y+qHWoso60hSRrTW4NzFrxJNJDgbnM0u/ReZo4waySqlGskGqqh0hUhWK116qrLSclprcJ5Ia8SEVflUZY4yjCryskxzs8zxedU9cu9bbkIJrbg+5b8Hh6BKVIYyqhHlZQ3DqPHpjE1bTK+Yv7q3yxqfqiurPMwrNue3529wvo4qnOza+pEKgJHBJMqMgnX5XFQJSQEmDpsuPJO5z5TrROYv2s67kW1wxnAgHiYKIGIh3MBD4DhZQYr+WTNI1qPmiMSGu3Hz9aQB7GZegxMcq1eAego48zE1ObPZLr5yHkJlrrNJzjrczHM65mT/KHXupDQZvMHZv3ZBrEQkVhQ9ftOaijwycfX+I9UVBYIyqKpYR3ORLCIymzxHNJcc+6HWqpub6Xrq8MlDzRHX4GzeR+vMGTvNSu0RRbbNbpQ5Mx2Q5mTksG1enZz9WVpSRpe4d3L/EdU6QkbtVyqlG5yfLVYGc5X5jOoRUmtzXVCFjRhMt2ZUszqLSpeWzsr0akunwZlMKOn/VeuKS3c7KV31OcQhV5RZVDyVz4o2gEjhs/VIbTwxsWGtnaV0g7P/lIQKqrM+SZaBBmd815m2VogqzWo1rUGo8akK8vw3wsdErrqigyiqagacpUVFmSWfQ1SX4nflVxqcn92R4Myv4xJQXCm6SgoTUB26IeIhEiTKA7q0OK932NsGZ4TIoaDrnatUanhISY6pVysSZ7zrBqjenmOQq3WpYkJp41eBiwSBs5mkneGM1+AE5EvVUhbVbl2qdL4jWiE1h0Q1bTFlWVXdv8FgZ7RWHTzkTqNFokwwXdM2244UpRNcTmuHrlVSbYMTm9C3yBznewhIVBO5G0nR1cVayV1lF1wrkUlhUlcPs7rB4VCRACINVDXjkLEzramaQXpC5AGUsXOzk8hs0rYhLRpiWglz0HDYSekGZ/+lD8T1k6AkwT2oteylwuGiwluRRNkctUaIwaRRGM1F6gu9z6kxpDl8U5wNTgwRlcLEV80zNDgiLQi9vAU45LBNFdQsclyfcLYgz1iozXVqyBGtVfputlojqoem43XyBmcPAalLoZR2blQmMsoy0jdTke+08ZUUJ/WBUJ4SS8QKECtxEwTZu9JE028zRKV3g7P/4ohMicrMqZoowuMkclVQRPdnkU6yWwUXlflVJdbgfO2AQ4uUMbKi7tTlKDiGzHG+0kupjCwSZnGQjbFa9VBFVMnmSOyQvYnq8Tx/gzN93fKt+BpdkAYn2MBKlJMa9rbgZF1p+lBZWtKCTLi7ova2466+X43t0Ns2KEIh1uAcf+f5MzrOqtZ8/805bHOUTJWXz3azyWGXWhsxoeqUVR25RIJA+sMGZ/xUwVuBQzoEjnYn15JraJaqhmkmIMj8bubPY1L1p+5D7RvyMErDE34lSoz0rQgtkudpcIL0IG0gpQT/FDik5qjUywow4W4qSR0pTN6BUAXdyeBo/a6UlrTW4MRSmmTw08GpfL2Kio6qJ1h1H5GyJLoVPRIp7p7EShPqnMc0OD/Zlu3bEnCyD0/RwYnpm8GMIo8oKGXi1DpI/XO64orOzgqSYewG574dbw0O4eFneBlH7a2qJ9tnzUysYg5C62SOoz0vfek3oSByzXVxDU4OUYPzdW6kvBRhDOWPSIspgsj6oQnSLyLFV5nPs/6CFOSIclyqmgEjexPNIRmm8lF39SANzlElGf8uwSGfz5lT1o1Ob7n3q+kcWftDyXXSm6tmMJH0dGz0+ZwG5zjanZpVBicsTOIXNubro8hRBZE47FXRSDaFyHWSlVW1OoztfIMH6QY0OPHPIUciKLISDU5AD5Xs3nYWHLlMat5tbHJM/Uydn3G1EgREEVJpSzZVdcwr9ZiKnQYnMaHKi5G6nNGYo0RTE0q70pkgoPKZRnjEz3QOQlmkgJN6SteUmdih5pztSjc4+WdvCFAycIhaI5NUTzLnsUk3OCqoZJzoOZyaE9Ve56iB1K6BDhuc/Eck5mL/cnDICx4qczLvQxVJxr0kypVPoDWTeDdC3apD4GRnWHMIddENcxRJg3PfgbAz0ZnjF3TiwajRnKkTqTWVSWcnduTzdh1KyipBQGSyk8FqTWQuSvnWYVtUICt82uDkP8g3qDXnA7vEhDnXDAsRn8mcI60KrlNXB3oRv451di1KkOwyx2mrU7XkZJcSHZm0dTadXvunwCEPTaJsFWeTcciao/pC6jGtK3Kdq2iNPGiDs/9tngZnihwSJIReo2tIG4tm47Ka46S66o2R3hrZFFI7lSBREX2WJXA9ewWtkdaGKvZko9Qc82aSekDmJAF5lIEy05z31pTPqS40u48W9EwJ0uw8C8K8J6vGu467zIQ2OMcvdhA6DE2oe+Pj+ixSyJnLLTqSH6FwizbNtIzinLMW1b462pf5mZXBLr3ITtRGg5N/bQul3AYHvOAxZ9urMucfmFAXDeBShKwAAAAASUVORK5CYII=" style="display: block;" /></div></div></div></div><a href="javascript:;" class="fl_wrap_close" title="关闭" id="appd_wrap_close">×</a></div></div><div id="fl_pop_box_default"></div><div id="appd_wrap_icon_arrow_down"></div></div><iframe id="J_test" src="/Domestic/cas/TableTennis" style="display: none;"></iframe></body></html>
"""
html = Selector(text=a)
d = html.xpath('//tr[@data-disable="0"]').extract()[1:]
# print(d)
for i in d:
    aa = str(remove_tags(i)).replace('\n','').strip()
    print(aa)
    bb = re.findall('(.*?房)',aa)
    cc = re.findall('¥(\d+)',aa)
    print(bb,cc)
    # print(str(remove_tags(i)).replace('\n','').strip())
    print('--------------')
