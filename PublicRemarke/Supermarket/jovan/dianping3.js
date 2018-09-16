function getCaptchaUrl(requestCode){
    var _token = getToken(requestCode);
    var randomId = Math.random();
    captchaUrl = 'https://verify.meituan.com/v2/captcha?request_code=' + requestCode + '&action=spiderindefence&randomId=' + randomId +'&_token='+_token;
    return captchaUrl;
}
function getToken(requestCode){
    var randomId = Math.random();
    url = 'https://verify.meituan.com/v2/captcha?request_code='+requestCode+'&action=spiderindefence&randomId='+randomId;
    return reload(url);
}