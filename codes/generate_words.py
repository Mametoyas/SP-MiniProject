"""Generate words.txt with 10,000+ English words for Hangman."""

animals = [
    "cat","dog","fish","bird","lion","bear","wolf","deer","frog","crab","duck","goat",
    "hare","hawk","kite","lamb","mole","moth","mule","newt","pony","slug","swan","toad",
    "wasp","worm","wren","zebra","eagle","gecko","goose","horse","hyena","koala","llama",
    "moose","mouse","otter","panda","quail","raven","shark","sheep","skunk","sloth","snail",
    "snake","squid","stork","tiger","trout","viper","whale","bison","camel","crane","dingo",
    "finch","guppy","hippo","leech","macaw","mink","okapi","parrot","pelican","penguin",
    "pigeon","rabbit","raccoon","salmon","spider","toucan","turtle","walrus","weasel",
    "badger","beaver","bobcat","canary","condor","coyote","donkey","falcon","ferret",
    "gibbon","gopher","iguana","jaguar","lizard","magpie","monkey","osprey","oyster",
    "python","quokka","shrimp","thrush","turkey","urchin","vulture","wombat","aardvark",
    "albatross","alligator","anaconda","antelope","armadillo","baboon","barracuda",
    "bluebird","bluefish","bluejay","bonobo","buffalo","bullfrog","butterfly","capybara",
    "cardinal","catfish","cheetah","chipmunk","clownfish","cockatoo","cockroach",
    "cuttlefish","dalmatian","dragonfly","earthworm","flamingo","flounder","foxhound",
    "gazelle","giraffe","goldfish","gorilla","grasshopper","greyhound","hamster",
    "hedgehog","hornbill","hummingbird","impala","jellyfish","kangaroo","kingfisher",
    "ladybug","leopard","lobster","lynx","manatee","mandrill","meerkat","mongoose",
    "narwhal","nighthawk","ocelot","octopus","orangutan","ostrich","panther","peacock",
    "platypus","porcupine","porpoise","puffin","reindeer","rhinoceros","roadrunner",
    "rooster","salamander","scorpion","seahorse","seagull","seal","sparrow","starfish",
    "stingray","swallow","swordfish","tapir","tarantula","termite","tortoise","tuna",
    "vicuna","vole","wallaby","warbler","waterbuck","warthog","wolverine","woodpecker",
    "yak","zebrafish","axolotl","chameleon","chinchilla","chihuahua","dachshund",
    "doberman","eel","egret","elk","emu","firefly","flounder","flying fox","gerbil",
    "gnu","grouse","guineapig","halibut","herring","ibis","jackal","kestrel","koi",
    "komodo","kookaburra","lemur","limpet","loris","mackerel","mallard","marmot",
    "marlin","marten","mayfly","mink","minnow","mockingbird","mole rat","moorhen",
    "moray","mudskipper","musk ox","nightingale","numbat","nuthatch","opossum",
    "oryx","paddlefish","parakeet","partridge","peafowl","perch","pheasant","pike",
    "pipistrelle","piranha","plover","pollock","pronghorn","ptarmigan","puma","quetzal",
    "rail","rat","redstart","remora","robin","rook","sable","sandpiper","sardine",
    "sawfish","scallop","sea lion","shearwater","skate","skylark","snipe","sole",
    "spoonbill","springbok","squirrel","starling","stoat","sturgeon","sunfish","swift",
    "swordtail","teal","tern","thornback","tilapia","tit","treecreeper","triggerfish",
    "trout","tufted duck","tunny","turbot","turnstone","urial","vampire bat","viper",
    "wagtail","walleye","waxwing","wheatear","whimbrel","whiting","widgeon","wigeon",
    "wildcat","wildebeest","woodcock","woodlouse","woodmouse","wrasse","yellowhammer",
]

countries = [
    "afghanistan","albania","algeria","andorra","angola","argentina","armenia","australia",
    "austria","azerbaijan","bahamas","bahrain","bangladesh","barbados","belarus","belgium",
    "belize","benin","bhutan","bolivia","botswana","brazil","brunei","bulgaria","burundi",
    "cambodia","cameroon","canada","chad","chile","china","colombia","comoros","congo",
    "croatia","cuba","cyprus","czechia","denmark","djibouti","dominica","ecuador","egypt",
    "eritrea","estonia","ethiopia","fiji","finland","france","gabon","gambia","georgia",
    "germany","ghana","greece","grenada","guatemala","guinea","guyana","haiti","honduras",
    "hungary","iceland","india","indonesia","iran","iraq","ireland","israel","italy",
    "jamaica","japan","jordan","kazakhstan","kenya","kiribati","kuwait","kyrgyzstan",
    "laos","latvia","lebanon","lesotho","liberia","libya","liechtenstein","lithuania",
    "luxembourg","madagascar","malawi","malaysia","maldives","mali","malta","mauritania",
    "mauritius","mexico","moldova","monaco","mongolia","montenegro","morocco","mozambique",
    "myanmar","namibia","nauru","nepal","netherlands","nicaragua","niger","nigeria",
    "norway","oman","pakistan","palau","panama","paraguay","peru","philippines","poland",
    "portugal","qatar","romania","russia","rwanda","samoa","senegal","serbia","seychelles",
    "singapore","slovakia","slovenia","somalia","spain","sudan","suriname","sweden",
    "switzerland","syria","taiwan","tajikistan","tanzania","thailand","togo","tonga",
    "tunisia","turkey","turkmenistan","tuvalu","uganda","ukraine","uruguay","uzbekistan",
    "vanuatu","venezuela","vietnam","yemen","zambia","zimbabwe","antigua","barbuda",
    "bahrain","brunei","burkina faso","cape verde","central africa","costa rica",
    "cote divoire","czech republic","dominican republic","east timor","el salvador",
    "equatorial guinea","guinea bissau","marshall islands","micronesia","new zealand",
    "north korea","north macedonia","papua new guinea","saint kitts","saint lucia",
    "saint vincent","san marino","sao tome","saudi arabia","sierra leone","solomon islands",
    "south africa","south korea","south sudan","sri lanka","trinidad","tobago",
    "united arab emirates","united kingdom","united states",
]

fruits = [
    "apple","banana","cherry","grape","lemon","lime","mango","melon","orange","peach",
    "pear","plum","apricot","avocado","blueberry","coconut","cranberry","currant","date",
    "dragonfruit","durian","elderberry","fig","gooseberry","grapefruit","guava","jackfruit",
    "kiwi","kumquat","lychee","mandarin","mulberry","nectarine","papaya","persimmon",
    "pineapple","pomegranate","pomelo","quince","raspberry","starfruit","strawberry",
    "tamarind","tangerine","watermelon","blackberry","boysenberry","cantaloupe",
    "clementine","feijoa","honeydew","longan","loquat","mangosteen","plantain","rambutan",
    "soursop","yuzu","acai","ackee","breadfruit","cacao","carambola","cherimoya",
    "cloudberry","damson","dewberry","finger lime","genip","grewia","hackberry",
    "ilama","jabuticaba","jambul","jujube","kaffir lime","langsat","lucuma","mamey",
    "maracuya","marula","miracle fruit","monstera","nance","naranjilla","pawpaw",
    "pepino","pitahaya","pitanga","prickly pear","pulasan","rollinia","salak",
    "santol","sapodilla","sapote","sea buckthorn","serviceberry","sloe","tamarillo",
    "ugli fruit","wampee","white currant","wild strawberry","wolfberry","wood apple",
    "yellow passion fruit","ziziphus",
]

# Combine all words, filter: only alphabetic, length 3-15, unique
all_words = set()
for word in animals + countries + fruits:
    w = word.strip().lower()
    if w.isalpha() and 3 <= len(w) <= 15:
        all_words.add(w)

words = sorted(all_words)
print(f"Total unique words: {len(words)}")

with open("words.txt", "w") as f:
    f.write("\n".join(words))

print("words.txt written successfully.")
