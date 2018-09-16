import execjs
ctx = execjs.compile("""
        function Ar() {
    return Math.floor(1 + 65535 *Bt()).toString(16).substring(1)
}
function Bt() {
    return Math.random()
}
function res() {
    var l = +new Date,d = []
    d.push(l.toString(16))
    d.push(Ar())
    d.push(Ar())
    d.push(Ar())
    a =d.join("-")
    return a

}
""")
a = ctx.call("res")
print(a)
