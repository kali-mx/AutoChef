


# add cipher_recipe from list of strings
cipher_recipe = (
  '{\"op\":\"JWT Decode\",\"args\":[]}]}',  
  '{"op":"Decode text","args":["UTF-8 (65001)"]}',
  '{"op":"AES Decrypt","args":[{"option":"Hex","string":""},{"option":"Hex","string":""},"CBC","Hex","Raw",{"option":"Hex","string":""},{"option":"Hex","string":""}]}',
  '{"op":"Bcrypt","args":[10]}',
  '{"op":"Blowfish Decrypt","args":[{"option":"Hex","string":""},{"option":"Hex","string":""},"CBC","Hex","Raw"]}',
  '{"op":"Bombe","args":["3-rotor","LEYJVCNIXWPBQMDRTAKZGFUHOS","EKMFLGDQVZNTOWYHXUSPAIBRCJ<R","AJDKSIRUXBLHWTMCQGZNPYFVOE<F","BDFHJLCPRTXVZNYEIWGAKMUSQO<W","AY BR CU DH EQ FS GL IP JX KN MO TZ VW","",0,true]}',
  '{"op":"CMAC","args":[{"option":"Hex","string":""},"AES"]}',
  '{"op":"ChaCha","args":[{"option":"Hex","string":""},{"option":"Hex","string":""},0,"20","Hex","Raw"]}',
  '{"op":"Colossus","args":["","KH Pattern","","","","None","Select Program","","","","","","","",false,"","","","","","",false,"","","","","","",false,"",false,"",false,false,false,false,false,"",false,false,"","",0,"","",1,1,1,1,1,1,1,1,1,1,1,1]}',
  '{"op":"Enigma","args":["3-rotor","LEYJVCNIXWPBQMDRTAKZGFUHOS","A","A","EKMFLGDQVZNTOWYHXUSPAIBRCJ<R","A","A","AJDKSIRUXBLHWTMCQGZNPYFVOE<F","A","A","BDFHJLCPRTXVZNYEIWGAKMUSQO<W","A","A","AY BR CU DH EQ FS GL IP JX KN MO TZ VW","",true]}',
  '{"op":"GOST hash","args":["D-A"]}',
  '{"op":"LS47 Decrypt","args":["",10]}',
  '{"op":"Lorenz","args":["SZ40","KH Pattern",false,"Send","Plaintext","Plaintext","5/8/9",1,1,1,1,1,1,1,1,1,1,1,1,".x...xx.x.x..xxx.x.x.xxxx.x.x.x.x.x..x.xx.x",".xx.x.xxx..x.x.x..x.xx.x.xxx.x....x.xx.x.x.x..x",".x.x.x..xxx....x.x.xx.x.x.x..xxx.x.x..x.x.xx..x.x.x",".xx...xxxxx.x.x.xx...x.xx.x.x..x.x.xx.x..x.x.x.x.x.x.","xx...xx.x..x.xx.x...x.x.x.x.x.x.x.x.xx..xxxx.x.x...xx.x..x.","x.x.x.x.x.x...x.x.x...x.x.x...x.x....",".xxxx.xxxx.xxx.xxxx.xx....xxx.xxxx.xxxx.xxxx.xxxx.xxx.xxxx...",".x...xxx.x.xxxx.x...x.x..xxx....xx.xxxx..","x..xxx...x.xxxx..xx..x..xx.xx..","..xx..x.xxx...xx...xx..xx.xx.","xx..x..xxxx..xx.xxx....x..","xx..xx....xxxx.x..x.x.."]}',
  '{"op":"RC4","args":[{"option":"UTF8","string":""},"Latin1","Latin1"]}',
  '{"op":"ROT13","args":[true,true,false,13]}',
  '{"op":"ROT47","args":[47]}',
  '{"op":"RC2 Decrypt","args":[{"option":"Hex","string":""},{"option":"Hex","string":""},"Hex","Raw"]}',
  '{"op":"Rabbit","args":[{"option":"Hex","string":""},{"option":"Hex","string":""},"Big","Raw","Raw"]}',
  '{"op":"SIGABA","args":["SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","SRGWANHPJZFXVIDQCEUKBYOLMT",false,"A","6201348957","0","6201348957","0","6201348957","0","6201348957","0","6201348957","0","Encrypt"]}',
  '{"op":"SM4 Decrypt","args":[{"option":"Hex","string":""},{"option":"Hex","string":""},"CBC","Raw","Hex"]}',
  '{"op":"Snefru","args":[128,"8"]}',
  '{"op":"Substitute","args":["ABCDEFGHIJKLMNOPQRSTUVWXYZ","XYZABCDEFGHIJKLMNOPQRSTUVW",false]}',
  '{"op":"Typex","args":["MCYLPQUVRXGSAOWNBJEZDTFKHI<BFHNQUW",false,"A","A","KHWENRCBISXJQGOFMAPVYZDLTU<BFHNQUW",false,"A","A","BYPDZMGIKQCUSATREHOJNLFWXV<BFHNQUW",false,"A","A","ZANJCGDLVHIXOBRPMSWQUKFYET<BFHNQUW",false,"A","A","QXBGUTOVFCZPJIHSWERYNDAMLK<BFHNQUW",false,"A","A","AN BC FG IE KD LU MH OR TS VZ WQ XJ YP","","None",true]}',
  '{"op":"Vigenère Decode","args":[""]}',
)

recipe_value = [
    {"op": "From Base32", "args": ["A-Z2-7=", True]},
    {"op": "From Base64", "args": ["A-Za-z0-9+/=", True, False]},
    {
        "op": "RC2 Decrypt",
        "args": [
            {"option": "Hex", "string": ""},
            {"option": "Hex", "string": ""},
            "Hex",
            "Raw",
        ],
    },
]
