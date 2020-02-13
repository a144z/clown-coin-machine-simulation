string="sadfakshsaagdasffasgdfasadafdsfdfadfaaafasdssaassssafddsdahsadsassdssdaddsaasassdddhsdaddahssaadsafkhaasadaaagsagsdsjdshsaddkasfsdfdaaaagagsdsdadadasasassdadadfhaafaadafdddfsdssfgdaadfdaaasasgsddddssasfddfagafdsddsddaasssadaaadafasadasaadssaadsadsasasaaasgsfsdasfsdsdadhadaahssaaasaaadasssgddfsaagasgaassaaassshaafsasfhfahdaaggjssdsassdddassdaasssasaasassshgadaahssadssfsggdadasffsfsdaadsssasgsfsfsasdasaahddassaasasaaaddsaaadadaffsdsaasgskdsasdasasaadaasdsfddafsdaaaasgddaafsaaadsadsafdsadsfhaasasasfadssfdafaadadsaaaaaasshadfdaddshdaaddssdghfsdadddsasasajaaaafaadaasdsaaaaasggssassssasaaaafdassahasaffagasaahdsadaadadsafassdgsdsadsdsaaaaddafssfahdsaaadfaaasadsgasaaaddsafsfsagdagadaddssaaddafdafdfafsaadaaadagshfsdfadasfassaaadfgaddsdfddasaaddjdaassassshgasasaaagdadasfhasfsasafdfdadaaadasafasfssssasaadfasaffdfasfddsfaaadfssdaasaagfasaddjadsadassafsadsafddfgaasaadfgasfssassggsgsdhhaagfssadaafssfdssaadasdasaafdasasadhadfaaaaaddsaaafaasafdgaadsfsasgaaafadsadsdaddsssfgassjgggsssssddagdasaahddasgasffajhsafasaafafsdjasdasdaaafdafsassfdadsasaaasssfasfsgaaaahdaasadhfasadafafasfsdfdfadaafssaaaasffdaasddfddsfdssfdgsaaaagafaadddaddasfsddsfsdsaajafsgdasasaadassdfsdssadsasfaaasadgasasaffasaaasgahfajsfsafdsdgsasasadgahdsdafafsaaagdddsasadsdfsssssafdgkaddfsadassssgfaffsaaasffhdssgasagdssasdshsdshafa"
counter=[0,0,0,0,0,0,0,0]
for _ in string:
    if _=="a":
        counter[0]+=1
    elif _=="s":
        counter[1]+=1
    elif _=="d":
        counter[2]+=1
    elif _=="f":
        counter[3]+=1
    elif _=="g":
        counter[4]+=1
    elif _=="h":
        counter[5]+=1
    elif _=="j":
        counter[6]+=1
    elif _=="k":
        counter[7]+=1
        
print(counter)
print(len(string))
for each in counter:
    print(each/len(string))
