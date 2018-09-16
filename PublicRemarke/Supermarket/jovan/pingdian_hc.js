function Ti() {
    return function() {
        function n() {
            return Math.floor(65536 * (1 + Math.random())).toString(16).substring(1)
        }
        return n() + n() + "-" + n() + "-" + n() + "-" + n() + "-" + n() + n() + n()
    }() + "." + (Math.round(+new Date / 1e3)+Math.floor(Math.random()*3600+1))
}