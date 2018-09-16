var kr, qr = (kr = function() {
        for (var n = 1 * new Date, t = 0; n === 1 * new Date && t < 200; )
            t++;
        return n.toString(16) + t.toString(16)
    }
        ,
function(height,width,useragent) {
    var n = (height * width).toString(16);
    return kr() + "-" + Math.random().toString(16).replace(".", "") + "-" + function() {
        var n = useragent
            , t = void 0
            , e = void 0
            , i = []
            , r = 0;
        function a(n, t) {
            var e = void 0
                , r = 0;
            for (e = 0; e < t.length; e++)
                r |= i[e] << 8 * e;
            return n ^ r
        }
        for (t = 0; t < n.length; t++)
            e = n.charCodeAt(t),
                i.unshift(255 & e),
            4 <= i.length && (r = a(r, i),
                i = []);
        return 0 < i.length && (r = a(r, i)),
            r.toString(16)
    }() + "-" + n + "-" + kr()
}
);
function Or(height,width,useragent) {
    var n
    var t =qr(height,width,useragent);
    return t
}
// Or()
