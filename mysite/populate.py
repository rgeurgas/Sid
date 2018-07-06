from course.models import Teacher, Course
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

Site.objects.all().delete()
SocialApp.objects.all().delete()
Teacher.objects.all().delete()
Course.objects.all().delete()

site = Site(id=0, domain='localhost:8000', name='localhost')
site.save()

google = SocialApp(
    provider='google',
    name='Google',
    client_id='391769807258-1m9ojltdvphurdmuslv4\
aoriq4jkc5p5.apps.googleusercontent.com',
    secret='KtzOBNQTsof9fkGlB8iC5rLK'
)
google.save()
google.sites.set([site.id])

print(f'Default domain is localhost:8000 if you want to \
change it run "make changedomain DOMAIN=your_domain"')

# SCC
roseli = Teacher(name='Roseli Ap. Francelin Romero')
ponce = Teacher(name='André Carlos Ponce de Leon Ferreira de Carvalho')
caetano = Teacher(name='Caetano Traina Junior')
agma = Teacher(name='Agma Juci Machado Traina')
mariac = Teacher(name='Maria Cristina Ferreira de Oliveira')
mariag = Teacher(name='Maria da Graça Campos Pimentel')
rosa = Teacher(name='João Luis Garcia Rosa')
rudinei = Teacher(name='Rudinei Goularte')
dilvan = Teacher(name='Dilvan de Abreu Moreira')
renata = Teacher(name='Renata Pontin de Mattos Fortes')
thiago = Teacher(name='Thiago Alexandre Salgueiro Pardo')
ciferri = Teacher(name='Cristina Dutra de Aguiar Ciferri')
mello = Teacher(name='Rodrigo Fernandes de Mello')
minghim = Teacher(name='Rosane Minghim')
jfernando = Teacher(name='José Fernando Rodrigues Júnior')
gbatista = Teacher(name='Gustavo Enrique de Almeida Prado Alves Batista')
solange = Teacher(name='Solange Oliveira Rezende')
moacir = Teacher(name='Moacir Antonelli Ponti')
manzato = Teacher(name='Marcelo Garcia Manzato')
robson = Teacher(name='Robson Leonardo Ferreira Cordeiro')
jbatista = Teacher(name='João do Espírito Santo Batista Neto')
amancio = Teacher(name='Diego Raphael Amâncio')
alneu = Teacher(name='Alneu de Andrade Lopes')
hruschka = Teacher(name='Eduardo Raul Hruschka')
elaine = Teacher(name='Elaine Parros Machado de Sousa')
paulovich = Teacher(name='Fernando Vieira Paulovich')
monard = Teacher(name='Maria Carolina Monard')
marian = Teacher(name='Maria das Graças Volpe Nunes')
campello = Teacher(name='Ricardo José Gabrielli Barreto Campello')
aluisio = Teacher(name='Sandra Maria Aluísio')

roseli.save()
ponce.save()
caetano.save()
agma.save()
mariac.save()
mariag.save()
rosa.save()
rudinei.save()
dilvan.save()
renata.save()
thiago.save()
ciferri.save()
mello.save()
minghim.save()
jfernando.save()
gbatista.save()
solange.save()
moacir.save()
manzato.save()
robson.save()
jbatista.save()
amancio.save()
alneu.save()
hruschka.save()
elaine.save()
paulovich.save()
monard.save()
marian.save()
campello.save()
aluisio.save()

# SSC
simao = Teacher(name='Adenilso da Silva Simão')
delbem = Teacher(name='Adenilso da Silva Simão')
claudio = Teacher(name='Cláudio Fabiano Motta Toledo')
denis = Teacher(name='Denis Fernando Wolf')
edson = Teacher(name='Edson dos Santos Moreira')
simoes = Teacher(name='Eduardo do Valle Simões')
emarques = Teacher(name='Eduardo Marques')
elisa = Teacher(name='Elisa Yumi Nakagawa')
ellen = Teacher(name='Ellen Francine Barbosa')
osorio = Teacher(name='Fernando Santos Osório')
monaco = Teacher(name='Francisco José Monaco')
jo = Teacher(name='Jo Ueyama')
jporto = Teacher(name='João Porto de Albuquerque Pereira')
jluiz = Teacher(name='Jorge Luiz e Silva')
maldonado = Teacher(name='José Carlos Maldonado')
estrella = Teacher(name='Júlio Cézar Estrella')
kalinka = Teacher(name='Kalinka Regina Lucas Jaquie Castelo Branco')
delamaro = Teacher(name='Marcio Eduardo Delamaro')
onofre = Teacher(name='Onofre Trindade Junior')
masiero = Teacher(name='Paulo Cesar Masiero')
psergio = Teacher(name='Paulo Sergio Lopes de Souza')
rosana = Teacher(name='Rosana Teresinha Vaccare Braga')
bruschi = Teacher(name='Sarita Mazzini Bruschi')
seiji = Teacher(name='Seiji Isotani')
simone = Teacher(name='Simone do Rocio Senger de Souza')
bonato = Teacher(name='Vanderlei Bonato')

simao.save()
delbem.save()
claudio.save()
denis.save()
edson.save()
simoes.save()
emarques.save()
elisa.save()
ellen.save()
osorio.save()
monaco.save()
jo.save()
jporto.save()
jluiz.save()
maldonado.save()
estrella.save()
kalinka.save()
delamaro.save()
onofre.save()
masiero.save()
psergio.save()
rosana.save()
bruschi.save()
seiji.save()
simone.save()
bonato.save()

# SME
kamimuri = Teacher(name='Adriano Kamimura Suzuki')
afonso = Teacher(name='Afonso Paiva Neto')
castelo = Teacher(name='Antonio Castelo Filho')
cibele = Teacher(name='Cibele Maria Russo Noveli')
cynthia = Teacher(name='Cynthia de Oliveira Lage Ferreira')
loao = Teacher(name='Dorival Leão Pinto Junior')
fontoura = Teacher(name='Eduardo Fontoura Costa')
salomao = Teacher(name='Elias Salomão Helou Neto')
everaldo = Teacher(name='Everaldo de Mello Bonotto')
simeoni = Teacher(name='Fabrício Simeoni de Sousa')
aparecido = Teacher(name='Francisco Aparecido Rodrigues')
louzada = Teacher(name='Francisco Louzada Neto')
franklina = Teacher(name='Franklina Maria Bragion de Toledo')
buscaglia = Teacher(name='Gustavo Carlos Buscaglia')
guzman = Teacher(name='Jorge Luis Bazan Guzman')
cuminato = Teacher(name='José Alberto Cuminato')
cobre = Teacher(name='Juliana Cobre')
katiane = Teacher(name='Katiane Silva Conceição')
leando = Teacher(name='Leandro Franco de Souza')
nonato = Teacher(name='Luis Gustavo Nonato')
gameiro = Teacher(name='Marcio Fuzeto Gameiro')
bambozzi = Teacher(name='Maria Luísa Bambozzi de Oliveira')
curi = Teacher(name='Mariana Cúri')
andretta = Teacher(name='Marina Andretta')
marinho = Teacher(name='Marinho Gomes de Andrade Filho')
castro = Teacher(name='Mário de Castro Andrade Filho')
maristela = Teacher(name='Maristela Oliveira dos Santos')
santini = Teacher(name='Miguel Vinícius Santini Frasson')
tome = Teacher(name='Murilo Francisco Tomé')
pablo = Teacher(name='Pablo Martín Rodriguez')
afonso = Teacher(name='Paulo Afonso Faria da Veiga')
reiko = Teacher(name='Reiko Aoki')
ehlers = Teacher(name='Ricardo Sandes Ehlers')
federico = Teacher(name='Roberto Federico Ausas')
tpereira = Teacher(name='Tiago Pereira da Silva')
marar = Teacher(name='Ton Marar')
garibay = Teacher(name='Vicente Garibay Cancho')

kamimuri.save()
afonso.save()
castelo.save()
cibele.save()
cynthia.save()
loao.save()
fontoura.save()
salomao.save()
everaldo.save()
simeoni.save()
aparecido.save()
louzada.save()
franklina.save()
buscaglia.save()
guzman.save()
cuminato.save()
cobre.save()
katiane.save()
leando.save()
nonato.save()
gameiro.save()
bambozzi.save()
curi.save()
andretta.save()
marinho.save()
castro.save()
maristela.save()
santini.save()
tome.save()
pablo.save()
afonso.save()
reiko.save()
ehlers.save()
federico.save()
tpereira.save()
marar.save()
garibay.save()

# SMA
bergamasco = Teacher(name='Adalberto Panobianco Bergamasco')
sasha = Teacher(name='Alexandre Ananin')
nolasco = Teacher(name='Alexandre Nolasco de Carvalho')
tahzibi = Teacher(name='Ali Tahzibi')
nabarro = Teacher(name='Ana Claudia Nabarro')
peron = Teacher(name='Ana Paula Peron')
mirzaii = Teacher(name='Behrooz Mirzaii')
apaza = Teacher(name='Carlos Alberto Maquera Apaza')
grossi = Teacher(name='Carlos Henrique Grossi Ferreira')
levcovitz = Teacher(name='Daniel Levcovitz')
smania = Teacher(name='Daniel Smania Brandão')
mattos = Teacher(name='Denise de Mattos')
costa = Teacher(name='Eder Ritis Aragão Costa')
moreira = Teacher(name='Ederson Moreira dos Santos')
zuffi = Teacher(name='Edna Maura Zuffi')
almeida = Teacher(name='Esther de Almeida Prado Rodrigues')
massa = Teacher(name='Eugenio Tommaso Massa')
raimundo = Teacher(name='Evandro Raimundo da Silva')
tari = Teacher(name='Farid Tari')
manfio = Teacher(name='Fernando Manfio')
borges = Teacher(name='Herivelto Martins Borges Filho')
hermano = Teacher(name='Hermano de Souza Ribeiro')
mencattini = Teacher(name='Igor Mencattini')
onnis = Teacher(name='Irene Ignazia Onnis')
ires = Teacher(name='Ires Dias')
janete = Teacher(name='Janete Crema Simal')
prado = Teacher(name='José Eduardo Prado Pires de Campos')
aurichi = Teacher(name='Leandro Fiorini Aurichi')
matofu = Teacher(name='Ma To Fu')
saia = Teacher(name='Marcelo José Saia')
federson = Teacher(name='Marcia Cristina Anderson Braz Federson')
carbinatto = Teacher(name='Maria do Carmo Carbinatto')
miriam = Teacher(name='Miriam Garcia Manoel')
nivlado = Teacher(name='Nivaldo de Goes Grulha Junior')
manzoli = Teacher(name='Oziride Manzoli Neto')
dattori = Teacher(name='Paulo Leandro Dattori da Silva')
magalhaes = Teacher(name='Pedro Paulo de Magalhães Rios')
nonato = Teacher(name='Raimundo Nonato Araújo dos Santos')
delazari = Teacher(name='Regilene Delazari dos Santos Oliveira')
meneghetti = Teacher(name='Renata Cristina Geromel Meneghetti')
atique = Teacher(name='Roberta Godoi Wik Atique')
monari = Teacher(name='Sérgio Henrique Monari Soares')
zani = Teacher(name='Sérgio Luís Zani')
tanaka = Teacher(name='Sueli Mieko Tanaka Aki')
jordao = Teacher(name='Thaís Jordão')
menegatto = Teacher(name='Valdir Antonio Menegatto')
perez = Teacher(name='Victor Hugo Jorge Pérez')
leite = Teacher(name='Wagner Vieira Leite Nunes')
luke = Teacher(name='Luke Skywalker')

bergamasco.save()
sasha.save()
nolasco.save()
tahzibi.save()
nabarro.save()
peron.save()
mirzaii.save()
apaza.save()
grossi.save()
levcovitz.save()
smania.save()
mattos.save()
costa.save()
moreira.save()
zuffi.save()
almeida.save()
massa.save()
raimundo.save()
tari.save()
manfio.save()
borges.save()
hermano.save()
mencattini.save()
onnis.save()
ires.save()
janete.save()
prado.save()
aurichi.save()
matofu.save()
saia.save()
federson.save()
carbinatto.save()
miriam.save()
nivlado.save()
manzoli.save()
dattori.save()
magalhaes.save()
nonato.save()
delazari.save()
meneghetti.save()
atique.save()
monari.save()
zani.save()
tanaka.save()
jordao.save()
menegatto.save()
perez.save()
leite.save()
luke.save()

course = Course(
    name='Sistemas Evolutivos e Aplicados à Robótica',
    code='SCC-713',
)
course.save()
course.teachers.set([simoes.id])

course = Course(
    name='Informação Profissional e Tutoria \
          Acadêmica em Ciências da Computação',
    code='SCC-200',
)
course.save()
course.teachers.set([thiago.id, jfernando.id])

course = Course(
    name='Introdução à Ciência de Computação I',
    code='SCC-221',
)
course.save()
course.teachers.set([mello.id, jbatista.id, simoes.id, moacir.id])

course = Course(
    name='Laboratório de Introdução à Ciência de Computação I',
    code='SCC-222',
)
course.save()
course.teachers.set([roseli.id, manzato.id])

course = Course(
    name='Geometria Analítica',
    code='SMA-300',
)
course.save()
course.teachers.set([carbinatto.id, sasha.id, apaza.id, tari.id,
                     hermano.id, prado.id, miriam.id, magalhaes.id,
                     perez.id])

course = Course(
    name='Cálculo I',
    code='SMA-353',
)
course.save()
course.teachers.set([nabarro.id, peron.id, moreira.id, mencattini.id, ires.id,
                     federson.id, nonato.id, atique.id, menegatto.id])

course = Course(
    name='Evolução Histórica da Computação e Aplicações',
    code='SSC-104',
)
course.save()
course.teachers.set([thiago.id, monaco.id])

course = Course(
    name='Prática em Lógica Digital',
    code='SSC-109',
)
course.save()
course.teachers.set([bonato.id])

course = Course(
    name='Introdução à Lógica Digital',
    code='SSC-117',
)
course.save()
course.teachers.set([emarques.id])

course = Course(
    name='Eletrônica para Computação',
    code='SSC-180',
)
course.save()
course.teachers.set([simoes.id, monaco.id])

course = Course(
    name='Introdução à Ciência de Computação II',
    code='SCC-201',
)
course.save()
course.teachers.set([mello.id, jbatista.id, simoes.id])

course = Course(
    name='Algoritmos e Estruturas de Dados I',
    code='SCC-202',
)
course.save()

course = Course(
    name='Matemática Discreta I',
    code='SMA-180',
)
course.save()

course = Course(
    name='Cálculo II',
    code='SMA-354',
)
course.save()

course = Course(
    name='Prática em Sistemas Digitais',
    code='SSC-108',
)
course.save()

course = Course(
    name='Sistemas Digitais',
    code='SSC-118',
)
course.save()

course = Course(
    name='Organização de Arquivos',
    code='SCC-215',
)
course.save()

course = Course(
    name='Modelagem Computacional em Grafos',
    code='SCC-216',
)
course.save()

course = Course(
    name='Cálculo III',
    code='SMA-355',
)
course.save()

course = Course(
    name='Programação Orientada a Objetos',
    code='SSC-103',
)
course.save()

course = Course(
    name='Organização de Computadores Digitais I',
    code='SSC-112',
)
course.save()

course = Course(
    name='Algoritmos Avançados e Aplicações',
    code='SCC-218',
)
course.save()

course = Course(
    name='Cálculo IV',
    code='SMA-356',
)
course.save()

course = Course(
    name='Estatística',
    code='SME-123',
)
course.save()

course = Course(
    name='Álgebra Linear e Equações Diferenciais',
    code='SME-141',
)
course.save()

course = Course(
    name='Análise e Projeto Orientados a Objetos',
    code='SSC-124',
)
course.save()

course = Course(
    name='Sistemas Operacionais I',
    code='SSC-140',
)
course.save()

course = Course(
    name='Bases de Dados',
    code='SCC-240',
)
course.save()
course.teachers.set([elaine.id])

course = Course(
    name='Computação Gráfica',
    code='SCC-250',
)
course.save()
course.teachers.set([agma.id])

course = Course(
    name='Cálculo Numérico',
    code='SME-104',
)
course.save()

course = Course(
    name='Processos Estocásticos',
    code='SME-121',
)
course.save()
course.teachers.set([pablo.id])

course = Course(
    name='Engenharia de Software',
    code='SSC-130',
)
course.save()
course.teachers.set([simone.id])

course = Course(
    name='Redes de Computadores',
    code='SSC-142',
)
course.save()
course.teachers.set([kalinka.id, jo.id])

course = Course(
    name='Teoria da Computação e Linguagens Formais',
    code='SCC-205',
)
course.save()

course = Course(
    name='Computadores e Sociedade I',
    code='SCC-207',
)
course.save()

course = Course(
    name='Inteligência Artificial',
    code='SCC-230',
)
course.save()

course = Course(
    name='Programação Matemática',
    code='SME-110',
)
course.save()

course = Course(
    name='Arquitetura de Computadores',
    code='SSC-114',
)
course.save()

course = Course(
    name='Programação Concorrente',
    code='SSC-143',
)
course.save()

course = Course(
    name='Linguagens de Programação e Compiladores',
    code='SCC-217',
)
course.save()

course = Course(
    name='Introdução ao Desenvolvimento Web',
    code='SCC-219',
)
course.save()

course = Course(
    name='Sistemas de Informação',
    code='SSC-120',
)
course.save()

course = Course(
    name='Estágio Supervisionado I',
    code='SCC-291',
)
course.save()

course = Course(
    name='Estágio Supervisionado II',
    code='SCC-292',
)
course.save()

course = Course(
    name='Humanidades e Ciências Sociais',
    code='IAU-126',
)
course.save()

course = Course(
    name='Laboratório de Introdução à Ciência da Computação II',
    code='SCC-220',
)
course.save()

course = Course(
    name='Prática em Organização de Computadores',
    code='SSC-119',
)
course.save()

course = Course(
    name='Metodologia de Pesquisa em Computação',
    code='SCC-213',
)
course.save()

course = Course(
    name='Seminários em Computação I',
    code='SCC-227',
)
course.save()

course = Course(
    name='Atividades Acadêmicas Científicas, de Extensão e Culturais I',
    code='SCC-295',
)
course.save()

course = Course(
    name='Algoritmos Avançados',
    code='SCC-210',
)
course.save()

course = Course(
    name='Seminários em Computação II',
    code='SCC-228',
)
course.save()

course = Course(
    name='Atividades Acadêmicas Científicas, de Extensão e Culturais II',
    code='SCC-296',
)
course.save()

course = Course(
    name='Laboratório de Algoritmos Avançados',
    code='SCC-211',
)
course.save()

course = Course(
    name='Seminários em Computação III',
    code='SCC-229',
)
course.save()

course = Course(
    name='Introdução à Ciência de Dados',
    code='SCC-275',
)
course.save()

course = Course(
    name='Introdução ao Desenvolvimento de Jogos Eletrônicos',
    code='SSC-770',
)
course.save()

course = Course(
    name='Empreendedores em Informática',
    code='SCC-209',
)
course.save()

course = Course(
    name='Tópicos Avançados em Inteligência Artificial',
    code='SCC-232',
)
course.save()

course = Course(
    name='Aplicações de Aprendizado de Máquina e Mineração de Dados',
    code='SCC-233',
)
course.save()

course = Course(
    name='Seminários Avançados de Inteligência Artificial I',
    code='SCC-238',
)
course.save()

course = Course(
    name='Laboratório de Bases de Dados',
    code='SCC-241',
)
course.save()

course = Course(
    name='Arquitetura de Sistemas Gerenciadores de Bases de Dados',
    code='SCC-243',
)
course.save()

course = Course(
    name='Seminários Avançados em Banco de Dados I',
    code='SCC-248',
)
course.save()

course = Course(
    name='Processamento de Imagens',
    code='SCC-251',
)
course.save()

course = Course(
    name='Ética e Legislação em Computação: Teoria e Prática',
    code='SCC-257',
)
course.save()

course = Course(
    name='Seminários Avançados em Computação Visual I',
    code='SCC-258',
)
course.save()

course = Course(
    name='Interação Usuário-computador',
    code='SCC-260',
)
course.save()

course = Course(
    name='Multimídia',
    code='SCC-261',
)
course.save()

course = Course(
    name='Técnicas de Programação para Web',
    code='SCC-263',
)
course.save()

course = Course(
    name='Sistemas Interativos Web',
    code='SCC-265',
)
course.save()

course = Course(
    name='Seminários em Informática e Saúde',
    code='SCC-267',
)
course.save()

course = Course(
    name='Seminários Avançados em Sistemas Hipermídia e Multimídia I',
    code='SCC-268',
)
course.save()

course = Course(
    name='Introdução à Redes Neurais',
    code='SCC-270',
)
course.save()

course = Course(
    name='Introdução à Computação Bioinspirada',
    code='SCC-272',
)
course.save()

course = Course(
    name='Robôs Móveis Inteligentes',
    code='SCC-273',
)
course.save()

course = Course(
    name='Aprendizado de Máquina',
    code='SCC-276',
)
course.save()

course = Course(
    name='Seminários Avançados de Redes Neurais I',
    code='SCC-278',
)
course.save()

course = Course(
    name='Sistemas de Recomendação',
    code='SCC-284',
)
course.save()

course = Course(
    name='Análise de Séries Temporais e Aplicações Computacionais',
    code='SCC-285',
)
course.save()

course = Course(
    name='Processamento de Linguagem Natural',
    code='SCC-633',
)
course.save()

course = Course(
    name='Seminários Avançados de Matemática Computacional I',
    code='SME-102',
)
course.save()

course = Course(
    name='Redes Complexas',
    code='SME-130',
)
course.save()

course = Course(
    name='Planejamento de Experimentos',
    code='SME-265',
)
course.save()

course = Course(
    name='Estatística Computacional',
    code='SME-806',
)
course.save()

course = Course(
    name='Tópicos Especiais em Hardware',
    code='SSC-115',
)
course.save()

course = Course(
    name='Gerência de Projetos',
    code='SSC-128',
)
course.save()

course = Course(
    name='Prática em Sistemas Operacionais',
    code='SSC-141',
)
course.save()

course = Course(
    name='Sistemas Computacionais Distribuídos',
    code='SSC-150',
)
course.save()

course = Course(
    name='Seminários Avançados em Sistemas \
          Distribuídos e Programação Concorrente I',
    code='SSC-154',
)
course.save()

course = Course(
    name='Computação Pervasiva',
    code='SSC-156',
)
course.save()

course = Course(
    name='Tópicos Avançados em Comunicação',
    code='SSC-157',
)
course.save()

course = Course(
    name='Computação em Nuvem e Arquitetura Orientadas a Serviços',
    code='SSC-158',
)
course.save()

course = Course(
    name='Modelagem e Simulação de Sistemas Computacionais',
    code='SSC-160',
)
course.save()

course = Course(
    name='Co-projeto de Hardware/Software para Sistemas Embarcados',
    code='SSC-711',
)
course.save()

course = Course(
    name='Programação de Robôs Móveis',
    code='SSC-712',
)
course.save()

course = Course(
    name='Robôs Móveis Autônomos',
    code='SSC-714',
)
course.save()

course = Course(
    name='Teste e Inspeção de Software',
    code='SSC-721',
)
course.save()

course = Course(
    name='Métodos e Técnicas para Análise e Projeto de Sistemas Reativos',
    code='SSC-722',
)
course.save()

course = Course(
    name='Sistemas Colaborativos: Fundamentos e Aplicações',
    code='SSC-723',
)
course.save()

course = Course(
    name='Arquitetura de Software',
    code='SSC-725',
)
course.save()

course = Course(
    name='Sistemas Embarcados',
    code='SSC-740',
)
course.save()

course = Course(
    name='Engenharia de Segurança',
    code='SSC-747',
)
course.save()

course = Course(
    name='Computadores e Sociedade II',
    code='SCC-208',
)
course.save()

course = Course(
    name='Laboratório de desenvolvimento \
          de aplicações para dispositivos móveis',
    code='SCC-225',
)
course.save()

course = Course(
    name='Introdução a Sistemas Inteligentes',
    code='SCC-231',
)
course.save()

course = Course(
    name='Tópicos Especiais em Banco de Dados',
    code='SCC-242',
)
course.save()

course = Course(
    name='Mineração a partir de Grandes Bases de Dados',
    code='SCC-244',
)
course.save()

course = Course(
    name='Processamento Analítico de Dados',
    code='SCC-245',
)
course.save()

course = Course(
    name='Recuperação de Dados por Conteúdo',
    code='SCC-246',
)
course.save()

course = Course(
    name='Visualização Computacional',
    code='SCC-252',
)
course.save()

course = Course(
    name='Tópicos Especiais em Computação Gráfica I',
    code='SCC-253',
)
course.save()

course = Course(
    name='Hipermídia',
    code='SCC-262',
)
course.save()

course = Course(
    name='Técnicas de Programação para Middleware',
    code='SCC-264',
)
course.save()

course = Course(
    name='Padrões de Projeto em Desenvolvimento Web',
    code='SCC-266',
)
course.save()

course = Course(
    name='Introdução à Bioinformática',
    code='SCC-271',
)
course.save()

course = Course(
    name='Agrupamento de Dados',
    code='SCC-274',
)
course.save()

course = Course(
    name='Competições de Ciências de Dados',
    code='SCC-277',
)
course.save()

course = Course(
    name='Acessibilidade em Sistemas Computacionais',
    code='SCC-280',
)
course.save()

course = Course(
    name='Recursos Computacionais de Tecnologia Assistiva',
    code='SCC-281',
)
course.save()

course = Course(
    name='Recuperação da Informação',
    code='SCC-282',
)
course.save()

course = Course(
    name='Introdução à Web Semântica',
    code='SCC-283',
)
course.save()

course = Course(
    name='Mineração de redes complexas',
    code='SCC-286',
)
course.save()

course = Course(
    name='Mineração de Dados Não Estruturados',
    code='SCC-287',
)
course.save()

course = Course(
    name='Seminários em Informática e Meio Ambiente',
    code='SCC-288',
)
course.save()

course = Course(
    name='Seminários de Otimização I',
    code='SME-111',
)
course.save()

course = Course(
    name='Séries Temporais',
    code='SME-808',
)
course.save()

course = Course(
    name='Análise Multivariada',
    code='SME-822',
)
course.save()

course = Course(
    name='Modelos Lineares Generalizados',
    code='SME-823',
)
course.save()

course = Course(
    name='Microprocessadores e Microcomputadores I',
    code='SSC-116',
)
course.save()

course = Course(
    name='Tópicos Especiais em Engenharia de Software',
    code='SSC-123',
)
course.save()

course = Course(
    name='Administração e Gerenciamento de Redes',
    code='SSC-152',
)
course.save()

course = Course(
    name='Tópicos Avançados em Computação de Alto Desempenho',
    code='SSC-159',
)
course.save()

course = Course(
    name='Tópicos Avançados em Sistemas Embarcados e Evolutivos',
    code='SSC-171',
)
course.save()

course = Course(
    name='Avaliação de Desempenho de Sistemas Computacionais',
    code='SSC-643',
)
course.save()

course = Course(
    name='Sistemas Evolutivos e Aplicados à Robótica',
    code='SSC-713',
)
course.save()

course = Course(
    name='Sensores Inteligentes',
    code='SSC-715',
)
course.save()

course = Course(
    name='Engenharia de Software para Sistemas Embarcados',
    code='SSC-720',
)
course.save()

course = Course(
    name='Sistemas Educacionais Avançados',
    code='SSC-724',
)
course.save()

course = Course(
    name='Reuso de Software',
    code='SSC-726',
)
course.save()

course = Course(
    name='Projeto e Implementação de Sistemas Embarcados I',
    code='SSC-741',
)
course.save()

course = Course(
    name='Computação Distribuída',
    code='SSC-744',
)
course.save()

course = Course(
    name='Sistemas Computacionais de Tempo-Real',
    code='SSC-745',
)
course.save()

course = Course(
    name='Sistemas Computacionais Tolerantes a Faltas',
    code='SSC-746',
)
course.save()

course = Course(
    name='Redes Móveis',
    code='SSC-748',
)
course.save()

course = Course(
    name='Projeto em Intercâmbio I',
    code='SCC-289',
)
course.save()

course = Course(
    name='Projeto de Graduação I',
    code='SCC-293',
)
course.save()

course = Course(
    name='Mineração Estatística de Dados',
    code='SME-878',
)
course.save()

course = Course(
    name='Projeto em Intercâmbio II',
    code='SCC-290',
)
course.save()

course = Course(
    name='Projeto de Graduação II',
    code='SCC-294',
)
course.save()

course = Course(
    name='Cálculo I',
    code='SMA-301',
)
course.save()
course.teachers.set([dattori.id])

course = Course(
    name='Fundamentos para a Matemática do Ensino Superior',
    code='SMA-334',
)
course.save()
course.teachers.set([aurichi.id])

course = Course(
    name='Introdução à Programação de Computadores',
    code='SME-230',
)
course.save()
course.teachers.set([andretta.id])

course = Course(
    name='Acompanhamento Profissional I',
    code='SME-280',
)
course.save()
course.teachers.set([andretta.id])

course = Course(
    name='Estruturas de dados I',
    code='SCC-223',
)
course.save()

course = Course(
    name='Cálculo II',
    code='SMA-332',
)
course.save()

course = Course(
    name='Elementos de Matemática',
    code='SMA-341',
)
course.save()

course = Course(
    name='Álgebra Linear',
    code='SMA-375',
)
course.save()

course = Course(
    name='Acompanhamento Profissional II',
    code='SME-281',
)
course.save()

course = Course(
    name='Estruturas de dados II',
    code='SCC-224',
)
course.save()

course = Course(
    name='Álgebra I',
    code='SMA-305',
)
course.save()

course = Course(
    name='Cálculo III',
    code='SMA-333',
)
course.save()

course = Course(
    name='Equações Diferenciais Ordinárias',
    code='SME-240',
)
course.save()

course = Course(
    name='Introdução à Modelagem Matemática',
    code='SME-241',
)
course.save()

course = Course(
    name='Métodos do Cálculo Numérico I',
    code='SME-205',
)
course.save()

course = Course(
    name='Otimização Linear',
    code='SME-211',
)
course.save()

course = Course(
    name='Introdução à Teoria das Probabilidades',
    code='SME-220',
)
course.save()

course = Course(
    name='Funções de Variável Complexa',
    code='SME-245',
)
course.save()

course = Course(
    name='Programação Orientada a Objetos',
    code='SCC-204',
)
course.save()

course = Course(
    name='Equações Diferenciais Parciais',
    code='SMA-169',
)
course.save()

course = Course(
    name='Análise I',
    code='SMA-307',
)
course.save()

course = Course(
    name='Métodos do Cálculo Numérico II',
    code='SME-206',
)
course.save()

course = Course(
    name='Introdução à Inferência Estatística',
    code='SME-221',
)
course.save()

course = Course(
    name='Espaços Métricos',
    code='SMA-343',
)
course.save()

course = Course(
    name='Métodos Numéricos em Equações Diferenciais',
    code='SME-202',
)
course.save()

course = Course(
    name='Geometria Diferencial',
    code='SMA-175',
)
course.save()

course = Course(
    name='Teoria Espectral de Matrizes',
    code='SME-243',
)
course.save()

course = Course(
    name='Estágio Supervisionado',
    code='SME-284',
)
course.save()

course = Course(
    name='Algoritmos e Estruturas de Dados II',
    code='SCC-203',
)
course.save()

course = Course(
    name='Fundamentos da Mecânica dos Fluidos',
    code='SEM-403',
)
course.save()

course = Course(
    name='Otimização Inteira',
    code='SME-213',
)
course.save()

course = Course(
    name='Métodos Numéricos para Geração de Malhas',
    code='SME-250',
)
course.save()

course = Course(
    name='Método dos Elementos Finitos Aplicados à Mecânica dos Fluídos',
    code='SME-254',
)
course.save()

course = Course(
    name='Tópicos de Matemática Aplicada I',
    code='SME-273',
)
course.save()

course = Course(
    name='Análise Exploratória de Dados',
    code='SME-803',
)
course.save()
course.teachers.set([katiane.id])

course = Course(
    name='Transferência de Calor e Massa',
    code='SEM-550',
)
course.save()

course = Course(
    name='Análise II',
    code='SMA-308',
)
course.save()

course = Course(
    name='Otimização Não Linear',
    code='SME-212',
)
course.save()

course = Course(
    name='Sistemas Estocásticos',
    code='SME-222',
)
course.save()

course = Course(
    name='Mecânica dos Fluidos Computacional I',
    code='SME-251',
)
course.save()

course = Course(
    name='Análise de Séries Temporais em Finanças',
    code='SME-262',
)
course.save()

course = Course(
    name='Tópicos em Matemática Aplicada II',
    code='SME-274',
)
course.save()

course = Course(
    name='Processos Estocásticos',
    code='SME-805',
)
course.save()

course = Course(
    name='Inferência Bayesiana',
    code='SME-809',
)
course.save()

course = Course(
    name='Análise de Regressão',
    code='SME-820',
)
course.save()

course = Course(
    name='Matemática Discreta II',
    code='SMA-181',
)
course.save()

course = Course(
    name='Laboratório de Otimização',
    code='SME-215',
)
course.save()

course = Course(
    name='Modelagem Matemática',
    code='SME-242',
)
course.save()

course = Course(
    name='Sistemas Esparsos e Computação Paralela',
    code='SME-252',
)
course.save()

course = Course(
    name='Simulação Computacional de Fluidos',
    code='SME-255',
)
course.save()

course = Course(
    name='Tópicos de Matemática Aplicada III',
    code='SME-275',
)
course.save()

course = Course(
    name='Análise de Dados Categorizados',
    code='SME-811',
)
course.save()

course = Course(
    name='Planejamento de Experimentos I',
    code='SME-816',
)
course.save()

course = Course(
    name='Análise de Sobrevivência e Confiabilidade',
    code='SME-821',
)
course.save()

course = Course(
    name='Gestão da Qualidade',
    code='SME-824',
)
course.save()

course = Course(
    name='Bioestatística',
    code='SME-871',
)
course.save()

course = Course(
    name='Econometria',
    code='SME-873',
)
course.save()

course = Course(
    name='Fluxos em Redes',
    code='SME-214',
)
course.save()

course = Course(
    name='Tópicos de Otimização Combinatória',
    code='SME-216',
)
course.save()

course = Course(
    name='Mecânica dos Fluidos Computacional II',
    code='SME-253',
)
course.save()

course = Course(
    name='Modelos Lineares Generalizados',
    code='SME-264',
)
course.save()

course = Course(
    name='Modelagem Geométrica',
    code='SME-271',
)
course.save()

course = Course(
    name='Introdução à Geometria Computacional',
    code='SME-272',
)
course.save()

course = Course(
    name='Tópicos em Matemática Aplicada IV',
    code='SME-276',
)
course.save()

course = Course(
    name='Projeto de Graduação',
    code='SME-285',
)
course.save()

course = Course(
    name='Modelos Lineares',
    code='SME-812',
)
course.save()

course = Course(
    name='Planejamento de Experimentos II',
    code='SME-817',
)
course.save()

course = Course(
    name='Matrizes, Vetores e Geometria Analítica',
    code='SMA-505',
)
course.save()
course.teachers.set([mirzaii.id])

course = Course(
    name='Matemática Discreta',
    code='SMA-508',
)
course.save()
course.teachers.set([levcovitz.id])

course = Course(
    name='Introdução à Ciência de Computação I',
    code='SSC-501',
)
course.save()
course.teachers.set([claudio.id])

course = Course(
    name='Laboratório de Introdução à Ciência de Computação I',
    code='SSC-502',
)
course.save()
course.teachers.set([claudio.id])

course = Course(
    name='Elementos de Lógica Digital',
    code='SSC-512',
)
course.save()
course.teachers.set([delbem.id])

course = Course(
    name='Introdução a Sistemas de Informação',
    code='SSC-530',
)
course.save()
course.teachers.set([ellen.id])

course = Course(
    name='Evolução Histórica da Computação e Aplicações',
    code='SSC-571',
)
course.save()
course.teachers.set([rosana.id])

course = Course(
    name='Algoritmos e Estruturas de Dados I',
    code='SCC-502',
)
course.save()

course = Course(
    name='Cálculo I',
    code='SMA-501',
)
course.save()

course = Course(
    name='Introdução à Ciência de Computação II',
    code='SSC-503',
)
course.save()

course = Course(
    name='Organização de Computadores Digitais',
    code='SSC-511',
)
course.save()

course = Course(
    name='Algoritmos e Estruturas de Dados II',
    code='SCC-503',
)
course.save()

course = Course(
    name='Programação Orientada a Objetos',
    code='SCC-504',
)
course.save()

course = Course(
    name='Introdução à Teoria da Computação',
    code='SCC-505',
)
course.save()

course = Course(
    name='Interação Usuário-Computador',
    code='SCC-560',
)
course.save()

course = Course(
    name='Cálculo Numérico',
    code='SME-500',
)
course.save()

course = Course(
    name='Introdução à Estatística',
    code='SME-520',
)
course.save()

course = Course(
    name='Atividades Acadêmicas Científicas e Culturais I',
    code='SSC-581',
)
course.save()

course = Course(
    name='Bases de Dados',
    code='SCC-540',
)
course.save()

course = Course(
    name='Contabilidade para Computação',
    code='SEP-584',
)
course.save()

course = Course(
    name='Introdução à Pesquisa Operacional',
    code='SME-510',
)
course.save()

course = Course(
    name='Arquitetura de Computadores',
    code='SSC-510',
)
course.save()

course = Course(
    name='Análise e Projeto Orientados a Objetos',
    code='SSC-526',
)
course.save()

course = Course(
    name='Sistemas Operacionais I',
    code='SSC-541',
)
course.save()

course = Course(
    name='Atividades Acadêmicas Científicas e Culturais II',
    code='SSC-582',
)
course.save()

course = Course(
    name='Inteligência Artificial',
    code='SCC-530',
)
course.save()

course = Course(
    name='Laboratório de Bases de Dados',
    code='SCC-541',
)
course.save()

course = Course(
    name='Modelagem da Produção',
    code='SEP-301',
)
course.save()

course = Course(
    name='Engenharia de Software',
    code='SSC-527',
)
course.save()

course = Course(
    name='Redes de Computadores',
    code='SSC-540',
)
course.save()

course = Course(
    name='Atividades Acadêmicas Científicas e Culturais III',
    code='SSC-583',
)
course.save()

course = Course(
    name='Prática e Gerenciamento de Projetos',
    code='SEP-172',
)
course.save()

course = Course(
    name='Modelagem da Organização',
    code='SEP-324',
)
course.save()

course = Course(
    name='Fundamentos de Economia',
    code='SEP-566',
)
course.save()

course = Course(
    name='Gestão de Sistemas de Informação',
    code='SSC-531',
)
course.save()

course = Course(
    name='Engenharia de Segurança',
    code='SSC-547',
)
course.save()

course = Course(
    name='Empreendedorismo',
    code='SSC-570',
)
course.save()

course = Course(
    name='Computadores, Sociedade e Ética Profissional',
    code='SSC-572',
)
course.save()

course = Course(
    name='Atividades Acadêmicas Científicas e Culturais IV',
    code='SSC-584',
)
course.save()

course = Course(
    name='Estágio Supervisionado I',
    code='SSC-591',
)
course.save()

course = Course(
    name='Estágio Supervisionado II',
    code='SSC-592',
)
course.save()

course = Course(
    name='Seminários em Computação I',
    code='SSC-576',
)
course.save()

course = Course(
    name='Seminários Avançados de Engenharia de Software I',
    code='SSC-126',
)
course.save()

course = Course(
    name='Seminários em Computação II',
    code='SSC-577',
)
course.save()

course = Course(
    name='Seminários Avançados de Inteligência Artificial II',
    code='SCC-239',
)
course.save()

course = Course(
    name='Seminários Avançados em Banco de Dados II',
    code='SCC-249',
)
course.save()

course = Course(
    name='Seminários Avançados em Computação Visual II',
    code='SCC-259',
)
course.save()

course = Course(
    name='Seminários Avançados em Sistemas Hipermídia e Multimídia II',
    code='SCC-269',
)
course.save()

course = Course(
    name='Seminários Avançados de Redes Neurais II',
    code='SCC-279',
)
course.save()

course = Course(
    name='Tópicos Especiais em Banco de Dados',
    code='SCC-542',
)
course.save()

course = Course(
    name='Hipermídia',
    code='SCC-562',
)
course.save()

course = Course(
    name='Seminários Avançados de Matemática Computacional II',
    code='SME-103',
)
course.save()

course = Course(
    name='Seminários de Otimização II',
    code='SME-112',
)
course.save()

course = Course(
    name='Seminários Avançados de Engenharia de Software II',
    code='SSC-127',
)
course.save()

course = Course(
    name='Seminários Avançados em Sistemas \
          Distribuídos e Programação Concorrente II',
    code='SSC-155',
)
course.save()

course = Course(
    name='Verificação, Validação e Teste de Software',
    code='SSC-524',
)
course.save()

course = Course(
    name='Sistemas Computacionais Distribuídos',
    code='SSC-543',
)
course.save()

course = Course(
    name='Introdução à Bioinformática',
    code='SSC-575',
)
course.save()

course = Course(
    name='Seminários em Computação III',
    code='SSC-578',
)
course.save()

course = Course(
    name='Multimídia',
    code='SCC-561',
)
course.save()

course = Course(
    name='Introdução a Redes Neurais',
    code='SCC-570',
)
course.save()

course = Course(
    name='Sistemas Colaborativos: Fundamentos e Aplicações',
    code='SSC-528',
)
course.save()

course = Course(
    name='Sistemas Educacionais Avançados',
    code='SSC-529',
)
course.save()

course = Course(
    name='Administração e Gerenciamento de Redes',
    code='SSC-542',
)
course.save()

course = Course(
    name='Projeto de Graduação I',
    code='SSC-593',
)
course.save()

course = Course(
    name='Projeto Empreendedor I',
    code='SSC-595',
)
course.save()

course = Course(
    name='Projeto em Intercâmbio I',
    code='SSC-597',
)
course.save()

course = Course(
    name='Introdução a Sistemas Inteligentes',
    code='SCC-531',
)
course.save()

course = Course(
    name='Tópicos Avançados em Inteligência Artificial',
    code='SCC-532',
)
course.save()

course = Course(
    name='Técnicas de Programação para Web',
    code='SCC-563',
)
course.save()

course = Course(
    name='Sistemas Interativos WEB',
    code='SCC-565',
)
course.save()

course = Course(
    name='Agrupamento de Dados',
    code='SCC-574',
)
course.save()

course = Course(
    name='Tópicos Especiais em Engenharia de Software',
    code='SSC-523',
)
course.save()

course = Course(
    name='Tópicos Avançados em Sistemas Distribuídos',
    code='SSC-544',
)
course.save()

course = Course(
    name='Redes de Alto Desempenho',
    code='SSC-545',
)
course.save()

course = Course(
    name='Avaliação de Sistemas Computacionais',
    code='SSC-546',
)
course.save()

course = Course(
    name='Redes Móveis',
    code='SSC-548',
)
course.save()

course = Course(
    name='Projeto de Graduação II',
    code='SSC-594',
)
course.save()

course = Course(
    name='Projeto Empreendedor II',
    code='SSC-596',
)
course.save()

course = Course(
    name='Projeto em Intercâmbio II',
    code='SSC-598',
)
course.save()

course = Course(
    name='Geometria Analítica',
    code='SMA-800',
)
course.save()
course.teachers.set([sasha.id])

course = Course(
    name='Cálculo I',
    code='SMA-801',
)
course.save()
course.teachers.set([apaza.id])

course = Course(
    name='Tópicos de Matemática',
    code='SMA-805',
)
course.save()
course.teachers.set([bergamasco.id])

course = Course(
    name='Metodologia Científica I',
    code='SME-825',
)
course.save()
course.teachers.set([marar.id])

course = Course(
    name='Direcionamento Acadêmico I',
    code='SME-890',
)
course.save()
course.teachers.set([louzada.id])

course = Course(
    name='Cálculo II',
    code='SMA-802',
)
course.save()

course = Course(
    name='Álgebra Linear',
    code='SMA-804',
)
course.save()

course = Course(
    name='Probabilidade I',
    code='SME-800',
)
course.save()

course = Course(
    name='Direcionamento Acadêmico II',
    code='SME-891',
)
course.save()

course = Course(
    name='Introdução à Ciência de Computação I',
    code='SSC-800',
)
course.save()

course = Course(
    name='Laboratório de Introdução à Ciência de Computação I',
    code='SSC-801',
)
course.save()

course = Course(
    name='Cálculo III',
    code='SMA-803',
)
course.save()

course = Course(
    name='Probabilidade II',
    code='SME-801',
)
course.save()

course = Course(
    name='Inferência Estatística',
    code='SME-818',
)
course.save()

course = Course(
    name='Matrizes Aplicadas à Estatística',
    code='SME-819',
)
course.save()

course = Course(
    name='Métodos Não Paramétricos',
    code='SME-810',
)
course.save()

course = Course(
    name='Cálculo Numérico para Estatística',
    code='SME-892',
)
course.save()

course = Course(
    name='Técnicas de Amostragem',
    code='SME-807',
)
course.save()

course = Course(
    name='Metodologia Científica II',
    code='SME-826',
)
course.save()

course = Course(
    name='Projeto Supervisionado em Estatística I',
    code='SME-814',
)
course.save()

course = Course(
    name='Projeto Supervisionado em Estatística II',
    code='SME-815',
)
course.save()

course = Course(
    name='Consultoria Estatística',
    code='SME-882',
)
course.save()

course = Course(
    name='Cultura, Ambiente e Sustentabilidade I',
    code='IAU-314',
)
course.save()

course = Course(
    name='Projetos de Algoritmos',
    code='SCC-814',
)
course.save()

course = Course(
    name='Introdução aos Estudos da Educação I',
    code='SLC-605',
)
course.save()

course = Course(
    name='Biologia I',
    code='SLC-620',
)
course.save()

course = Course(
    name='Equações Diferenciais Ordinárias',
    code='SME-840',
)
course.save()

course = Course(
    name='Cultura, Ambiente e Sustentabilidade II',
    code='IAU-315',
)
course.save()

course = Course(
    name='Introdução aos Estudos da Educação II',
    code='SLC-606',
)
course.save()

course = Course(
    name='Biologia II',
    code='SLC-621',
)
course.save()

course = Course(
    name='Filosofia da Matemática',
    code='SMA-326',
)
course.save()

course = Course(
    name='Didática',
    code='SMA-339',
)
course.save()

course = Course(
    name='Introdução aos Estudos da Educação',
    code='SMA-340',
)
course.save()

course = Course(
    name='Programação Matemática',
    code='SME-210',
)
course.save()

course = Course(
    name='Demografia',
    code='SME-872',
)
course.save()

course = Course(
    name='Introdução à Teoria da Medida',
    code='SMA-143',
)
course.save()

course = Course(
    name='Tópicos Especiais em Estatística Aplicada I',
    code='SME-870',
)
course.save()

course = Course(
    name='Projeto de Graduação em Estatística I',
    code='SME-880',
)
course.save()

course = Course(
    name='Tópicos Especiais em Estatística Aplicada II',
    code='SME-875',
)
course.save()

course = Course(
    name='Teoria de Resposta ao Item',
    code='SME-876',
)
course.save()

course = Course(
    name='Projeto de Graduação em Estatística II',
    code='SME-881',
)
course.save()

course = Course(
    name='Introdução à Jedi',
    code='JED-101',
)
course.save()
course.teachers.set([luke.id])
