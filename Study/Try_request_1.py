import requests
import execjs
import json
jsCode = """
    function a(r) {
        if (Array.isArray(r)) {
            for (var o = 0, t = Array(r.length); o < r.length; o++)
                t[o] = r[o];
            return t
        }
        return Array.from(r)
    }
    function n(r, o) {
        for (var t = 0; t < o.length - 2; t += 3) {
            var a = o.charAt(t + 2);
            a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
            a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
            r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
        }
        return r
    }
    var i = null;
    function e(r) {
        var t = r.length;
        t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))

        var u = void 0, l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);

        u = null !== i ? i : (i = '320305.131321201' || "") || "";
        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
            var A = r.charCodeAt(v);
            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
            S[c++] = A >> 18 | 240,
            S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
            S[c++] = A >> 6 & 63 | 128),
            S[c++] = 63 & A | 128)
        }
        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S[b],
            p = n(p, F);
        return p = n(p, D),
        p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
        p %= 1e6,
        p.toString() + "." + (p ^ m)
    }
"""
url ="https://fanyi.baidu.com/basetrans"
query = input("请输入需要翻译的中文内容：")
sign = execjs.compile(jsCode).call("e", query)
print(sign)

#注意tokent和Cookie匹配的问题，前面多次未完全模拟的爬虫请求，token将被封 需要匹配完整的Cookie
querry_string={
        "from":"zh",
        "to" :"en",
        "query": query,
        "sign": sign,
        "token": "9f9086f41e322073a7c8d6d32bdc1929",
}


headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '132',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':"BAIDUID=67E2DAD89A81A917FFDC7A503E568DFA:FG=1; BIDUPSID=67E2DAD89A81A917FFDC7A503E568DFA; PSTM=1543471403; BDUSS=pkV244U2NDbi0zOVdKQVpHNGtkOWVDWWdaRmYyVWpNfkU5Z2NGYVotVnpqRFZjQVFBQUFBJCQAAAAAAAAAAAEAAADBE2kEzOz0pcSr1M8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHP~DVxz~w1cSk; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; H_PS_PSSID=1433_21083_28723_28557_28830_28584; delPer=0; BDRCVFR[pNjdDcNFITf]=mk3SLVN4HKm; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1555558247,1555644695; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22de%22%2C%22text%22%3A%22%u5FB7%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1555646033; PSINO=7; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1555653423; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1555653607",
        'DNT':  '1',
        'Host': 'fanyi.baidu.com',
        'Origin': 'https://fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'User-Agent':"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3664.3 Mobile Safari/537.36",
        'X-Requested-With': 'XMLHttpRequest'
}

response =requests.post(url=url,headers=headers,data=querry_string)#返回的是字符串
# response =requests.get(url)
# response.encoding ="UTF-8"
# print(response.content.decode())
# print(response.text)
# print(response.content.decode())
det = response.content.decode() #json字符串
print(det)
ret =json.loads(det) #提取
result = ret['trans'][0]['dst']
print(type(result))
print(query,"的翻译结果是",result)

