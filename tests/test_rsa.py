"""Tests for rsa.py and keys.py."""

from deniable.rsa import decryption, encryption
from deniable.keys import generate_keypair

def test_encrypt_message():
    """Can we properly encrypt a message?"""
    pub = """-----BEGIN PUBLIC KEY-----
MCEwDQYJKoZIhvcNAQEBBQADEAAwDQIGAstna9HBAgMBAAE=
-----END PUBLIC KEY-----"""
    mes = "foo"
    cipher = encryption(mes, pub)
    assert cipher == "002877160453915"

def test_decrypt_message():
    """Can we properly decrypt a message?"""
    sec = """-----BEGIN RSA PRIVATE KEY-----
MC8CAQACBgLLZ2vRwQIDAQABAgUOx3XPUQIDHAz3AgMZgQcCAwWnGwICfDsCAxe2
1g==
-----END RSA PRIVATE KEY-----"""
    cipher = "002877160453915"
    mes = decryption(cipher, sec)
    assert mes == "foo"

def test_cryptosystem_char():
    """Can we properly use the cryptosystem?"""
    keys = generate_keypair()
    (pub, sec) = (keys['pub'], keys['sec'])
    mes1 = """a"""
    cipher = encryption(mes1, pub)
    mes2 = decryption(cipher, sec)
    assert mes1 == mes2

def test_cryptosystem_hello():
    """Can we properly use the cryptosystem?"""
    keys = generate_keypair()
    (pub, sec) = (keys['pub'], keys['sec'])
    mes1 = """Hello world, my name is Victor"""
    cipher = encryption(mes1, pub)
    mes2 = decryption(cipher, sec)
    assert mes1 == mes2

def test_cryptosystem_music():
    """Can we properly use the cryptosystem?"""
    keys = generate_keypair()
    (pub, sec) = (keys['pub'], keys['sec'])
    mes1 = """
    An-nyong-ha-se-yo!
Sometimes you gotta bleed to know
That you're alive and have a soul
But it takes someone to come around
To show you how

She's the tear in my heart
I'm alive
She's the tear in my heart
I'm on fire
She's the tear in my heart
Take me higher
Than I've ever been

The songs on the radio are okay
But my taste in music is your face
And it takes a song to come around
To show you how

She's the tear in my heart
I'm alive
She's the tear in my heart
I'm on fire
She's the tear in my heart
Take me higher
Than I've ever been
Than I've ever been
Than I've ever been
Than I've ever been

You fell asleep in my car I drove the whole time
But that's okay I'll just avoid the holes so you sleep fine
I'm driving here I sit
Cursing my government
For not using my taxes
To fill holes with more cement

You fell asleep in my car I drove the whole time
But that's okay I'll just avoid the holes so you sleep fine
I'm driving here I sit
Cursing my government
For not using my taxes
To fill holes with more cement
Sometimes you gotta bleed to know, oh, oh
That you're alive and have a soul, oh, oh
But it takes someone to come around
To show you how

She's the tear in my heart
I'm alive
She's the tear in my heart
I'm on fire
She's the tear in my heart
Take me higher
Than I've ever been
My heart is my armor
She's the tear in my heart
She's a carver
She's a butcher with a smile

Cut me farther
Than I've ever been
Than I've ever been
Than I've ever been
Than I've ever been
My heart is my armor
She's the tear in my heart
She's a carver
She's a butcher with a smile
Cut me farther
Than I've ever been
    """
    cipher = encryption(mes1, pub)
    mes2 = decryption(cipher, sec)
    assert mes1 == mes2

def test_cryptosystem_lorem_ipsum():
    """Can we properly use the cryptosystem?"""
    keys = generate_keypair()
    (pub, sec) = (keys['pub'], keys['sec'])
    mes1 = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi imperdiet, neque quis finibus rhoncus, nunc nisi lobortis nisl, id sodales magna dui ac nulla. Morbi id eleifend urna. Nam augue massa, mollis eu ipsum ac, congue convallis ligula. Nulla sed ultricies orci, vitae iaculis enim. In id placerat est, sit amet tempor mauris. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus eu velit eleifend, consectetur justo non, sollicitudin dolor. Nullam non nunc nec nisi auctor maximus. Nullam in libero eu urna lobortis sollicitudin sed id nunc. Nulla id elit non libero consectetur lobortis eget vel risus. Curabitur ultrices sagittis molestie. Integer porttitor aliquet tristique. Etiam facilisis sem eu tellus finibus tempus.

Donec sed neque mauris. Praesent nibh ex, hendrerit ut efficitur et, maximus id ligula. Donec tempor turpis id orci mollis ornare. Cras semper eros justo, volutpat condimentum turpis ultricies sit amet. Donec euismod elit nisl, ut aliquet odio scelerisque sit amet. Aliquam consectetur nisl a vestibulum dignissim. Ut placerat justo sit amet ligula molestie, ac vestibulum diam feugiat. Sed molestie urna vel ligula maximus mattis. Curabitur faucibus, quam a ultrices sodales, quam erat porta quam, nec placerat libero purus dictum leo.

Nullam ut lacinia tortor. In nec arcu aliquam, interdum leo molestie, dictum sem. Proin luctus congue massa, eu molestie sapien sodales sed. Sed sollicitudin vehicula ex sit amet gravida. Sed non nibh sed odio consequat venenatis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus vitae dignissim eros. Vestibulum volutpat lorem nisl, id interdum lacus interdum vitae. Sed consectetur arcu lobortis mauris hendrerit, a tristique tortor scelerisque. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut ac rutrum purus. Sed at enim ut odio tincidunt vehicula id et felis. Morbi eget eros sed dolor blandit bibendum.

Suspendisse massa leo, placerat sed pellentesque scelerisque, dignissim ac urna. Nulla vehicula fringilla iaculis. Maecenas arcu ligula, porta ac risus sit amet, vulputate fermentum ex. Quisque convallis dui metus, non venenatis augue placerat ullamcorper. Nullam viverra neque nec lectus commodo, ac facilisis arcu suscipit. Praesent euismod erat sit amet tristique aliquet. Nam efficitur, nisl vitae tincidunt aliquet, elit diam dictum ipsum, ac laoreet lorem turpis malesuada metus. Nam vel feugiat libero, at lobortis nulla. Sed mollis purus leo, convallis eleifend tellus porta ac. Ut sit amet risus quis erat scelerisque laoreet sed id lorem. Ut non bibendum purus. Integer orci tortor, pellentesque nec tortor eget, laoreet rhoncus nisi.

Nullam placerat augue a nulla eleifend pellentesque. Aliquam id aliquam arcu. Curabitur feugiat diam in bibendum bibendum. Nunc semper, mi at finibus condimentum, libero ligula interdum augue, a imperdiet lorem justo pretium tortor. Quisque sit amet posuere felis. Donec tempus lectus a lorem scelerisque viverra. Phasellus eget lectus nulla. Maecenas lacinia consectetur malesuada. Pellentesque scelerisque neque facilisis semper vehicula. Sed vitae enim id mauris feugiat scelerisque.

Pellentesque ornare laoreet congue. Integer erat risus, eleifend at ultrices et, interdum quis tortor. Nam sed enim accumsan, mattis enim id, mattis odio. Phasellus ut lacus sit amet enim lacinia vulputate. Sed eu efficitur quam. Phasellus varius magna turpis, ut semper ex sodales eu. Suspendisse eleifend nisi sit amet metus facilisis semper. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla facilisi. Mauris felis nulla, blandit eget sapien ac, tempus pellentesque turpis. Praesent congue egestas mi et sollicitudin. Donec tincidunt ac diam vitae commodo. Curabitur aliquam euismod sem, nec condimentum tellus. Aliquam eu orci sit amet justo tempor porttitor quis sed risus.

Nunc lectus libero, gravida ut lectus iaculis, mollis ultricies ex. Duis eleifend volutpat nisi nec tincidunt. Nunc fermentum felis sit amet urna iaculis congue nec in leo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec sodales dignissim erat ac auctor. Aliquam consectetur leo vel commodo faucibus. Morbi accumsan diam sit amet varius tristique.

Praesent congue aliquam massa id tempus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam posuere blandit felis id fermentum. Sed mattis mauris eget sapien eleifend ultricies. Pellentesque at purus et mi lobortis convallis. Praesent egestas dui sed nibh finibus convallis vitae et diam. Integer vitae augue eget diam semper rhoncus. Etiam ac ex nec risus auctor varius. Pellentesque ac ante quis erat blandit bibendum nec hendrerit massa. Nulla id arcu condimentum, sodales eros in, efficitur elit. Morbi ante nisi, finibus a urna ac, bibendum suscipit nulla. Sed metus risus, ornare quis finibus non, posuere at eros.

Morbi et pretium orci, vel viverra dolor. Nam porttitor lobortis nisl, id congue turpis posuere sit amet. Pellentesque volutpat, mi id rutrum semper, dui est ultrices erat, quis dignissim arcu turpis ac nunc. Pellentesque eget ante non odio congue vehicula. Aliquam tristique velit in tincidunt maximus. Ut id turpis et ipsum gravida tincidunt quis a tortor. Proin turpis massa, accumsan a libero quis, porta lacinia elit. Cras ante lorem, blandit quis placerat molestie, ullamcorper et sapien. Pellentesque egestas efficitur lacus, vel suscipit urna aliquam a. Vestibulum elit mi, scelerisque a commodo eget, pretium et sem. Praesent at nunc vestibulum, auctor nisl nec, euismod urna. Nunc vitae metus eu velit ullamcorper vestibulum. Nulla ac metus eget libero vulputate lobortis. Integer bibendum dui non metus tincidunt dapibus. Nam posuere iaculis ipsum, pellentesque ultricies leo congue ultricies. Sed pellentesque eros ac dui sodales imperdiet.

Fusce a felis consectetur mi ullamcorper accumsan vitae faucibus ligula. Donec vulputate pellentesque nibh quis maximus. Donec feugiat gravida fringilla. Duis non mauris in mi finibus porta sit amet et diam. Donec vel erat lacinia, venenatis nibh nec, accumsan ipsum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque nec nunc convallis, venenatis urna id, cursus ligula. Curabitur mattis magna ac mauris dapibus suscipit. Nunc eget lorem at enim pretium cursus a quis dolor. Suspendisse auctor vestibulum rhoncus. Fusce gravida volutpat magna, ac accumsan lectus mollis in. Maecenas luctus tellus pharetra efficitur tincidunt. Maecenas auctor nisl vitae mauris facilisis, eu tempus felis consequat. Etiam vel tellus augue. Curabitur ultricies ac enim quis sodales.

Fusce ut tellus vitae purus finibus ornare in eu velit. Vestibulum id vulputate lectus. Morbi facilisis commodo nisi, et convallis diam fermentum eu. Duis ut metus nibh. Sed nec tempor nulla, eget tempor velit. Aliquam pharetra erat elit, ac pharetra lectus fermentum eget. Vivamus euismod facilisis metus. In egestas nisl non rutrum interdum. Vestibulum pharetra ultrices justo, non efficitur metus convallis vel. Curabitur vulputate augue justo, eget scelerisque diam blandit vel. Cras congue massa at tristique facilisis. Nullam laoreet id arcu nec hendrerit. Donec eros enim, elementum ut tempor ac, blandit ut felis. Integer elementum euismod magna, quis dictum leo pulvinar in.

Nam ullamcorper blandit est non efficitur. Praesent et justo vitae eros faucibus sagittis. Nulla in auctor nibh, ac laoreet ex. Nullam congue sapien nulla, eget volutpat enim consectetur id. Vestibulum gravida nisi vitae interdum laoreet. Quisque eget lobortis eros. Vivamus lectus enim, dictum sed interdum at, tincidunt sed neque.

In eget odio dolor. Sed aliquam fringilla enim, a scelerisque lacus maximus vel. Ut mattis est lectus, sit amet lacinia lacus condimentum mattis. Nullam non posuere lorem. Duis non iaculis sem. Nunc laoreet enim libero, ut congue metus auctor at. Nunc ante sapien, ullamcorper a facilisis sit amet, condimentum quis ex. Donec rutrum nibh a lorem interdum laoreet. Integer vitae pharetra nulla. Cras nec orci viverra, lobortis erat eget, maximus ex. Nullam at dapibus urna.

Fusce vel tellus magna. Praesent ultricies viverra aliquam. Aenean elementum id arcu sit amet blandit. Cras dolor nibh, dapibus nec felis a, lacinia ornare sapien. Nunc euismod massa erat, eu mollis lorem gravida quis. Mauris et tincidunt felis. Suspendisse dictum mi elementum justo posuere, vel convallis diam rhoncus. Sed fermentum libero at iaculis volutpat. Etiam nec vehicula lectus. Donec interdum justo ante, nec aliquet tortor porttitor a. Sed ut consectetur justo. Nunc convallis quam vitae eros molestie, et tempor mauris lacinia. Sed ac sapien quis ipsum placerat aliquam eget nec nisi. Donec vitae fermentum felis. Suspendisse elementum orci nec lorem dapibus, vitae placerat lacus pellentesque.

In tincidunt nunc vitae ligula bibendum, non faucibus urna euismod. Aenean ultricies vitae libero quis ultricies. Nam eget nibh felis. Sed nec orci ligula. Quisque eu sem velit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque iaculis nec ligula sed feugiat. Morbi sed volutpat elit, eu egestas tortor. Ut malesuada dui nisi, sed venenatis nisl elementum ac. Nulla ut varius mi, non rhoncus velit.

Praesent sem ligula, venenatis rhoncus semper in, egestas et ex. Mauris fringilla fringilla justo, sit amet blandit velit porttitor at. Fusce egestas erat at elit fringilla luctus. Suspendisse quis vestibulum augue, in lacinia purus. Duis augue sapien, tempus efficitur lacinia ut, pulvinar sodales ipsum. Etiam dictum lorem quis sem pharetra, sed finibus eros dignissim. Suspendisse sollicitudin leo est, eu maximus velit posuere sit amet. Pellentesque nec nibh a sapien posuere sollicitudin ac vel lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla a diam pulvinar, congue sem eget, luctus purus. Fusce dolor metus, blandit vel nulla non, feugiat facilisis arcu. Sed ex nibh, pharetra eget dui et, commodo pretium lacus. Donec sed neque diam.

Fusce hendrerit volutpat libero, vitae blandit tellus rutrum nec. Vivamus eget velit fringilla, laoreet erat ut, hendrerit neque. Donec quis nisi et enim dignissim rutrum in vel neque. Mauris a risus in ex auctor tincidunt eget sed leo. Mauris mauris massa, blandit eget semper eget, pretium volutpat nibh. Proin nec ultricies ex, at aliquet mauris. Morbi ac risus et lacus vehicula finibus a sit amet urna. Pellentesque dictum pretium enim id dignissim. Nunc hendrerit porttitor leo, in bibendum metus egestas iaculis. Praesent a hendrerit odio. Etiam at commodo mi.

Proin at ipsum risus. Duis interdum aliquam felis, vitae finibus libero lacinia in. Nullam efficitur volutpat interdum. Nulla pharetra quis ligula ut finibus. Duis dignissim venenatis nisl, eleifend faucibus orci. Fusce in ipsum nec odio finibus scelerisque tincidunt vitae erat. Phasellus ut diam at sapien scelerisque molestie. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

In at arcu lacinia, iaculis purus at, vulputate mauris. Integer accumsan risus urna, sed venenatis quam pellentesque maximus. Mauris ullamcorper cursus orci, ut aliquet nisl ullamcorper id. Praesent vestibulum risus sed sem accumsan faucibus. Suspendisse vel nibh a lectus vehicula blandit vel nec sapien. Suspendisse ut iaculis quam. Nam faucibus lacus ac dolor finibus varius. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec commodo felis at consectetur sodales. Vivamus aliquet in enim vitae bibendum. Nullam a lorem vel urna dapibus scelerisque quis at sapien. Vestibulum tristique suscipit sapien vel accumsan. Donec maximus in urna id aliquam.

Aenean ornare congue nisl, in ornare sapien rhoncus id. Praesent ut commodo nibh, bibendum finibus ante. Ut tincidunt enim diam, eget blandit nisl maximus a. Aenean at ex sit amet dolor suscipit mattis non non quam. Vivamus placerat eros eu varius auctor. Nullam porta urna sit amet ipsum bibendum consequat. Aliquam erat volutpat. Donec metus augue, sodales ac felis mattis, venenatis feugiat felis. Aliquam sed libero ut nisi convallis bibendum.

Phasellus malesuada risus vitae arcu dapibus consequat ac sed purus. Donec sodales tristique est at eleifend. Donec id odio elementum, dapibus tellus eu, blandit lectus. Vestibulum vitae quam suscipit metus egestas tincidunt. Donec auctor dictum orci, sed maximus massa dignissim eget. Nullam sed ipsum nec mi blandit interdum. Sed ut fringilla augue, in finibus dolor. Maecenas massa eros, faucibus nec pretium vitae, scelerisque iaculis metus. In sit amet odio sapien. Donec laoreet cursus orci, ut malesuada quam fringilla tincidunt. Quisque turpis erat, cursus id vestibulum at, efficitur sed lorem. Pellentesque sem turpis, posuere eget feugiat nec, rutrum vitae erat. Quisque consequat augue at dolor vulputate, sed imperdiet sapien scelerisque. Duis eu tortor eu magna faucibus pharetra.

Nunc vel mi elementum, mollis ipsum non, blandit leo. Fusce a augue eget leo iaculis imperdiet. Phasellus leo arcu, fermentum in gravida ac, pulvinar commodo orci. Ut vitae congue turpis, nec convallis arcu. Phasellus suscipit, mi ut elementum sollicitudin, mauris lorem ultricies quam, vitae cursus velit orci posuere nibh. Sed in ex sit amet massa bibendum mollis vel et elit. Proin eget ex at metus cursus blandit. Fusce quis bibendum erat. Sed libero nunc, pretium sit amet mollis quis, mattis et neque. Nam hendrerit, felis ac venenatis suscipit, augue libero rhoncus augue, vulputate ultricies lectus orci id dolor. Pellentesque porta quam urna, a vulputate arcu sagittis et. Praesent eu eleifend felis. Duis quam lorem, porta sit amet libero id, dignissim suscipit lectus. Donec odio lorem, placerat nec sem eget, rutrum facilisis nulla. Integer volutpat elit vel ante pulvinar interdum.

Vestibulum pretium orci libero, ut iaculis leo ultrices a. In at feugiat neque. Praesent nec ultricies magna. In hac habitasse platea dictumst. Praesent ut nisi velit. Morbi ac venenatis mauris. Quisque tincidunt justo eget est ultrices pharetra. Sed elementum velit ac augue convallis vestibulum. Cras sodales at mauris a tincidunt. Nam vel faucibus velit.

Donec aliquet ac massa id auctor. Donec aliquet nulla non dolor pulvinar, aliquam rhoncus enim dapibus. Phasellus sit amet sodales nunc. Donec sit amet auctor tortor, id molestie massa. Vivamus a tincidunt sapien, porttitor tristique velit. Curabitur viverra in dolor vel vestibulum. Duis id luctus elit. Morbi a eleifend turpis, vitae lobortis nisi. Donec interdum iaculis felis et luctus. Duis at interdum eros. Quisque suscipit euismod tempus.

Nullam ultricies blandit mi sed rutrum. Integer ac lorem odio. Vestibulum in finibus sapien. Etiam porta eget nisi vel lobortis. Nunc turpis urna, accumsan nec vehicula in, tristique eu metus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras nec hendrerit purus, a auctor enim.

Maecenas ut scelerisque nisl. Aliquam nisi est, suscipit vel efficitur nec, hendrerit tristique urna. Etiam lacinia tortor malesuada, pulvinar dolor eget, suscipit orci. Cras pulvinar hendrerit felis at dictum. In hac habitasse platea dictumst. Nulla vel scelerisque ipsum. Suspendisse dictum orci ac auctor iaculis. Mauris tempor aliquet ullamcorper.

Phasellus luctus purus eu enim porta, ut aliquam augue condimentum. Fusce egestas libero a aliquet iaculis. Nam efficitur id purus vitae varius. Mauris id tortor non justo pretium mollis. Sed nec vehicula metus. Etiam blandit nunc ex, sed interdum magna placerat sed. Vivamus sit amet felis ut lacus aliquam dapibus. Ut a ipsum porta, lacinia odio nec, tristique neque. Cras lacinia dapibus nisl id luctus. Fusce posuere efficitur ipsum, at porttitor ante convallis id.

Nulla facilisi. Maecenas sit amet hendrerit est. Aenean efficitur tortor at felis ultrices, non vestibulum urna posuere. Maecenas at accumsan urna. Aliquam quis mauris a nisl mollis porttitor. In quis ipsum quis eros vehicula pulvinar. Ut feugiat lacus a neque imperdiet sodales. Nulla commodo ex id metus venenatis consequat. Aenean et neque vitae libero bibendum pharetra non dapibus enim. Praesent lorem nisl, congue nec nisl eu, efficitur ullamcorper est. Proin urna dolor, feugiat quis nisl vitae, luctus rutrum diam. Nam tempor hendrerit sodales. Praesent risus nisi, vehicula non nunc sit amet, elementum facilisis risus. Integer consequat, sem nec sagittis condimentum, lorem enim molestie nunc, sit amet pretium lacus lectus ut augue. Pellentesque a neque dolor. Vivamus porta massa non facilisis luctus.

Nam egestas, magna id tristique lacinia, elit justo ultricies neque, lobortis bibendum tortor augue in ligula. Cras lobortis placerat ligula a posuere. Maecenas elementum ipsum diam, quis volutpat nisi faucibus et. Vestibulum sagittis ac nisi ac dignissim. Nullam consectetur tempus tempor. In congue aliquet justo et eleifend. Suspendisse fermentum nisi eget facilisis aliquet. Quisque in consectetur elit. In dapibus, eros molestie cursus luctus, tortor urna cursus massa, vel convallis mi enim et urna. Maecenas quis magna sit amet felis lobortis sodales. Nulla porttitor tellus in sapien maximus, nec luctus leo mattis.

Nulla facilisi. Integer quis felis enim. Pellentesque ex tortor, iaculis sit amet mattis ac, placerat id leo. Mauris at rhoncus sem. Morbi ullamcorper sodales est, nec feugiat ante vulputate quis. Mauris rutrum cursus facilisis. Phasellus eget massa vel ex accumsan rutrum. Aliquam erat volutpat.

Nam rutrum quam vel enim fringilla pulvinar. Nam auctor, leo nec aliquet cursus, nisi tortor ornare est, eu viverra justo leo vel felis. Aenean mauris nisl, sodales et odio sed, rhoncus pharetra nunc. Curabitur sed sodales eros. Fusce rutrum non tortor at dignissim. Sed aliquam vestibulum nisi id dapibus. Aliquam in velit ipsum. Ut sem lorem, euismod pellentesque lacus sed, aliquet scelerisque erat. Phasellus viverra nunc in tellus iaculis, dignissim facilisis nunc bibendum. Vivamus tristique felis et tellus maximus, id euismod erat pulvinar. Aenean in ex ipsum.

Morbi lobortis mi nec libero cursus, a eleifend libero dapibus. Morbi sit amet leo nec ipsum consectetur auctor. Nullam vel enim aliquet, iaculis odio ut, molestie augue. Proin vel ante iaculis, fringilla sapien eu, pharetra orci. Nunc vel mauris sed magna iaculis porttitor sit amet vitae dolor. Cras id leo non neque lacinia placerat a eget diam. Nullam libero urna, hendrerit vitae arcu at, tristique eleifend magna. Nulla sollicitudin metus ut urna pellentesque finibus. Nullam egestas lectus eu sem auctor lobortis. Quisque in pulvinar ex, vitae dapibus sem. Proin volutpat sapien consectetur, consequat metus id, vulputate mauris. Ut vel augue condimentum, porta lorem id, molestie turpis. Nunc nec vehicula neque, at malesuada augue. Mauris non commodo lacus. Suspendisse feugiat neque et metus dignissim, tempus sodales odio sodales. Mauris rutrum molestie ligula, et mollis lacus tincidunt non.

Aenean et maximus dolor. Aliquam quis ullamcorper nulla, bibendum pulvinar quam. Maecenas sodales lobortis semper. Pellentesque malesuada commodo blandit. Proin iaculis rhoncus augue eget placerat. Nulla dignissim elementum posuere. Nunc ipsum leo, ornare eget pharetra et, vulputate nec quam. Donec justo mauris, pulvinar sit amet enim ut, condimentum vulputate dolor. Nam imperdiet arcu enim, vel eleifend dolor aliquam eget. Nullam at mattis lectus.

Morbi imperdiet odio sit amet nulla auctor, et ultrices tortor fermentum. In a maximus ex. Donec id viverra erat. Maecenas a malesuada nulla. Vestibulum id est ut nisi fermentum aliquet non non diam. Morbi sed ornare tellus, quis scelerisque tortor. Nulla convallis rutrum posuere. Donec gravida dolor a nulla aliquet, consectetur mollis lacus consequat. Morbi eget justo bibendum, ullamcorper tellus vel, consectetur dolor. Nullam eu tortor condimentum, eleifend tellus ut, venenatis tortor.

Duis eu est ex. Integer consectetur, sapien id molestie fermentum, quam mauris pharetra justo, at commodo diam mauris quis nisl. Donec rhoncus nunc ornare sapien mollis, vitae vestibulum nunc placerat. Nunc a libero vel dolor viverra imperdiet. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Fusce dui massa, dictum ac nunc in, malesuada hendrerit sapien. Pellentesque luctus, libero id rhoncus sodales, tellus tellus pretium erat, condimentum placerat augue tellus ac tellus. Vivamus at lorem ante. Nulla nec varius ex. Curabitur mi nisl, ultrices at interdum sit amet, eleifend id felis. In viverra sapien justo, sit amet varius urna dictum et. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Etiam vitae dui eu purus laoreet laoreet. Curabitur in tincidunt lectus, non feugiat eros. Phasellus suscipit nisi eget mauris malesuada imperdiet. Sed in aliquet lectus. Vivamus id congue enim. Praesent vitae metus imperdiet, consequat neque at, bibendum dui. Pellentesque venenatis massa felis, id mattis mi cursus vitae. Pellentesque eu mauris venenatis, congue purus vel, feugiat nisl. Nullam a velit sed elit lacinia aliquam et a magna. Vestibulum non massa tincidunt, blandit massa eu, tristique ligula.

In hac habitasse platea dictumst. Pellentesque nibh sapien, accumsan sed libero ac, bibendum vulputate nisl. In turpis mi, porta sed urna quis, venenatis lacinia eros. Duis mauris nibh, ornare quis augue id, condimentum venenatis lacus. Sed varius ante et orci porta tincidunt. Proin leo lectus, convallis ut augue vulputate, pharetra dignissim eros. Praesent quis nisi pulvinar odio tempor porta sit amet at sem.

Morbi sit amet rutrum nulla, eu laoreet nunc. Cras venenatis eros vitae fringilla luctus. Nam quis dolor tortor. Donec nec mollis ipsum, eget consequat risus. Etiam ipsum nulla, aliquet id molestie ac, viverra sit amet purus. Vivamus feugiat mollis metus, in sodales risus. Nunc tincidunt ex vel sapien maximus, in accumsan lorem posuere. Donec vel maximus purus. Donec dapibus vulputate metus, nec blandit tellus dignissim a. Nunc at volutpat magna. Proin vehicula semper lorem ac rhoncus. Donec est augue, faucibus et libero at, congue elementum nibh. Aenean finibus blandit eros, vitae vehicula ligula tincidunt eget.

Sed eu imperdiet lectus. Aenean sit amet leo id felis tristique blandit a non nibh. Nunc libero neque, semper at molestie at, cursus eget lectus. Morbi suscipit sem quis volutpat ullamcorper. Donec at nibh non ipsum pharetra consequat. Sed sagittis pretium quam a pulvinar. Quisque tincidunt ligula dui, in iaculis lorem fringilla eu. Nullam dui dolor, auctor eu ornare in, lobortis in nibh. Suspendisse ultrices mauris ac purus iaculis elementum. Morbi ut fermentum nunc. Aliquam cursus ex sed viverra maximus. Pellentesque viverra vitae neque a viverra. Phasellus mollis convallis eros ac blandit. Donec imperdiet dolor lorem, ac tincidunt magna consectetur a.

Curabitur maximus fringilla pellentesque. Mauris dapibus dapibus velit in lobortis. Phasellus id commodo diam, nec consequat velit. Morbi id libero eget dui vestibulum tincidunt eget sed urna. Nam efficitur condimentum justo, at tempor nulla rhoncus in. Mauris rutrum risus neque, nec pretium sem interdum et. Integer tellus ex, viverra sed leo non, ornare elementum orci. Etiam hendrerit ligula ut augue dapibus, in pretium dui gravida.

Sed consectetur erat nibh, varius molestie lacus pulvinar sed. Aenean dictum ex ut nunc accumsan sollicitudin. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam eleifend dictum massa ut sodales. Vestibulum sapien elit, ultrices et elit vitae, commodo auctor lacus. Aenean nec eleifend magna. Donec ut iaculis elit. Maecenas metus quam, sollicitudin nec pretium fringilla, tempor a nisl. Donec iaculis metus magna, lobortis faucibus tortor dictum accumsan. Praesent quis congue quam, eget pulvinar enim. Etiam dictum ex nec felis faucibus accumsan. Cras vel dapibus mauris. Etiam hendrerit mi arcu, nec lacinia arcu auctor id. Pellentesque rhoncus arcu id felis elementum venenatis at id mi.

Quisque nec nisl justo. Pellentesque ac est ut nulla malesuada lacinia a at erat. Morbi vitae enim condimentum, luctus arcu in, tempus mi. Donec pellentesque mauris metus, id pretium tellus porta at. Aenean suscipit velit massa, eu tincidunt ex vestibulum vel. Curabitur mi urna, vestibulum id arcu ac, pulvinar euismod lorem. Vestibulum vel enim non mi semper facilisis vel interdum lectus. Aenean convallis tellus vitae odio rutrum tristique. Nunc nec tristique velit. Donec enim neque, convallis in orci nec, fringilla semper lectus. Phasellus auctor, lorem et malesuada malesuada, justo turpis consequat quam, nec malesuada dolor est eu lacus. Nullam egestas molestie elit, a vestibulum augue varius at. Phasellus malesuada cursus tellus in malesuada. Donec luctus dolor nunc, ac commodo est luctus id. Quisque lobortis leo elit, vel luctus ex sagittis ut. Suspendisse eget lacus posuere, egestas turpis non, condimentum metus.

Fusce pharetra lobortis mauris, nec vestibulum dolor blandit vitae. Nulla imperdiet magna ac lacus dapibus, quis blandit arcu pretium. Praesent pellentesque turpis in felis blandit molestie. Mauris sem ipsum, egestas sed fermentum eu, cursus nec est. Donec rhoncus hendrerit purus, non lacinia neque placerat in. Nam pretium pharetra justo, ut malesuada justo ultricies in. Ut eget iaculis arcu, ultrices sodales urna. Nulla facilisi. Ut in arcu auctor, euismod nunc id, venenatis orci.

Aenean id commodo erat. Pellentesque lobortis vulputate augue ac semper. Fusce eget dolor eleifend metus fringilla eleifend. Sed lacinia neque orci, sed blandit nulla dignissim id. Quisque faucibus accumsan ligula et egestas. Morbi eu efficitur augue. Nulla facilisis felis et ornare convallis. Nulla vehicula purus vulputate, hendrerit quam a, venenatis ligula. Ut imperdiet enim nec felis luctus dignissim. Pellentesque a orci in orci iaculis auctor. Praesent eget volutpat purus.

Quisque convallis lorem eu augue venenatis tempor. Cras et est lobortis, auctor ipsum cursus, dignissim arcu. Quisque commodo, est vel suscipit posuere, diam libero imperdiet sem, sit amet pulvinar lorem velit id enim. Vivamus in consequat metus, sed blandit nunc. Mauris finibus libero porta sollicitudin ultricies. Aliquam eu semper metus, pulvinar tempus orci. Nunc risus est, imperdiet ac luctus ac, tincidunt sit amet ligula. Maecenas non justo fringilla, tempus quam in, malesuada nisi. Nam pretium sagittis bibendum. Vivamus euismod sit amet ipsum eget commodo. Pellentesque lacinia eleifend tortor, in pretium ligula tincidunt nec.

Cras laoreet ipsum tortor, at placerat elit scelerisque a. Nunc et ultricies dolor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed tristique ac ligula at semper. Aenean malesuada hendrerit euismod. Curabitur suscipit mauris ac euismod maximus. Praesent dapibus ipsum eros, venenatis tincidunt libero faucibus ut. Pellentesque tristique non nisi vel fermentum. Pellentesque vel quam nulla. In nec cursus ex. Aliquam erat volutpat. Nulla egestas eros in metus pellentesque, vel hendrerit eros euismod. Fusce vulputate vitae odio et mollis. Sed eget ornare ante.

Curabitur maximus nulla eget purus accumsan, vitae ullamcorper purus auctor. Maecenas elit risus, facilisis nec elit eget, pulvinar hendrerit augue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris a neque vulputate, aliquam tellus vel, blandit turpis. Nullam tempus, eros nec molestie tempus, nibh metus sodales leo, at condimentum urna enim sit amet mauris. Morbi ante mauris, elementum viverra dictum in, maximus sit amet sapien. Praesent ultrices feugiat massa nec placerat. Donec lacus orci, viverra sed posuere sed, ultricies eget ex. Pellentesque feugiat aliquet felis et venenatis. Etiam semper ex vitae nisl lacinia consequat. Donec eleifend odio nec eros volutpat efficitur. Maecenas vitae orci vel mi ultricies gravida ac non dui. Pellentesque ultrices nec neque ut luctus.

Morbi id est condimentum, eleifend neque non, volutpat turpis. Praesent vel pharetra eros, et tempus nibh. Etiam semper lacinia euismod. Duis suscipit lectus eu elit porta dignissim. Nam justo lectus, imperdiet id magna at, consequat congue sem. Donec neque enim, sagittis non placerat non, mollis at nunc. Curabitur nec ornare enim. Praesent luctus hendrerit nisi, et molestie libero imperdiet in. Praesent ac sem nec orci iaculis sodales sit amet in ligula. Curabitur posuere elit vitae dolor congue, egestas posuere sapien congue.

Proin bibendum metus sed mauris fringilla dictum. Nulla faucibus libero sit amet posuere imperdiet. Phasellus tempus consectetur odio, nec porttitor diam tincidunt in. Fusce vel tellus vitae dui accumsan sodales. Ut augue augue, posuere nec finibus eleifend, hendrerit eu nibh. Nullam cursus, mi eget pulvinar dictum, felis elit tristique mi, sed bibendum sapien sem ac quam. Nulla tristique non leo et laoreet. Fusce pellentesque ultricies diam a sodales. Mauris est arcu, tincidunt sed nisl eu, venenatis molestie urna.

Cras aliquet purus ut nisi molestie laoreet. Nulla at rutrum augue. Nunc dictum tincidunt suscipit. Curabitur ut enim ut leo dignissim lobortis. Vestibulum ullamcorper massa urna, a blandit ante vulputate gravida. Etiam velit orci, imperdiet sit amet elit sed, pretium ultricies diam. Pellentesque mollis ante eu sapien pharetra faucibus. Aenean placerat nulla eu erat pretium facilisis et sed dui.
    """
    cipher = encryption(mes1, pub)
    mes2 = decryption(cipher, sec)
    assert mes1 == mes2
