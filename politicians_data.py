from datetime import date
from enums import Party, Gender


POLITICIANS_DATA = {
    "BURGUM": {
        "full_name": "Doug Burgum",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1956, 8, 1)
    },
    "HUTCHINSON": {
        "full_name": "Asa Hutchinson",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1950, 12, 3)
    },
    "KEYES": {
        "full_name": "Alan Keyes",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1950, 8, 7)
    },
    "FERRARO": {
        "full_name": "Geraldine Ferraro",
        "party": Party.DEMOCRAT,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1935, 8, 26)
    },
    "STOCKDALE": {
        "full_name": "James Stockdale",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1923, 12, 23)
    },
    "KENNEDY": {
        "full_name": "John F. Kennedy",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1917, 5, 29)
    },
    "NIXON": {
        "full_name": "Richard Nixon",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1913, 1, 9)
    },
    "HUMPHREY": {
        "full_name": "Hubert Humphrey",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1911, 5, 27)
    },
    "CARTER": {
        "full_name": "Jimmy Carter",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1924, 10, 1)
    },
    "FORD": {
        "full_name": "Gerald Ford",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1913, 7, 14)
    },
    "REAGAN": {
        "full_name": "Ronald Reagan",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1911, 2, 6)
    },
    "ANDERSON": {
        "full_name": "John B. Anderson",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1922, 2, 15)
    },
    "MONDALE": {
        "full_name": "Walter Mondale",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1928, 1, 5)
    },
    "BUSH": {
        "full_name": "George H. W. Bush",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1924, 6, 12)
    },
    "JACKSON": {
        "full_name": "Jesse Jackson",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1941, 10, 8)
    },
    "DUKAKIS": {
        "full_name": "Michael Dukakis",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1933, 11, 3)
    },
    "HART": {
        "full_name": "Gary Hart",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1936, 11, 28)
    },
    "CLINTON": {
        "full_name": "Bill Clinton",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1946, 8, 19)
    },
    "PEROT": {
        "full_name": "Ross Perot",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1930, 6, 27)
    },
    "DOLE": {
        "full_name": "Bob Dole",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1923, 7, 22)
    },
    "KEMP": {
        "full_name": "Jack Kemp",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1935, 7, 13)
    },
    "QUAYLE": {
        "full_name": "Dan Quayle",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1947, 2, 4)
    },
    "BENTSEN": {
        "full_name": "Lloyd Bentsen",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1921, 2, 11)
    },
    "GORE": {
        "full_name": "Al Gore",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1948, 3, 31)
    },
    "FORBES": {
        "full_name": "Steve Forbes",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1947, 7, 18)
    },
    "BUCHANAN": {
        "full_name": "Pat Buchanan",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1938, 11, 2)
    },
    "ALEXANDER": {
        "full_name": "Lamar Alexander",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1940, 7, 3)
    },
    "BAUER": {
        "full_name": "Gary Bauer",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1946, 5, 4)
    },
    "MCCAIN": {
        "full_name": "John McCain",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1936, 8, 29)
    },
    "BRADLEY": {
        "full_name": "Bill Bradley",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1943, 7, 28)
    },
    "CHENEY": {
        "full_name": "Dick Cheney",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1941, 1, 30)
    },
    "LIEBERMAN": {
        "full_name": "Joe Lieberman",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1942, 2, 24)
    },
    "KERRY": {
        "full_name": "John Kerry",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1943, 12, 11)
    },
    "EDWARDS": {
        "full_name": "John Edwards",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1953, 6, 10)
    },
    "DEAN": {
        "full_name": "Howard Dean",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1948, 11, 17)
    },
    "CLARK": {
        "full_name": "Wesley Clark",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1944, 12, 23)
    },
    "KUCINICH": {
        "full_name": "Dennis Kucinich",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1946, 10, 8)
    },
    "SHARPTON": {
        "full_name": "Al Sharpton",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1954, 10, 3)
    },
    "OBAMA": {
        "full_name": "Barack Obama",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1961, 8, 4)
    },
    "BIDEN": {
        "full_name": "Joe Biden",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1942, 11, 20)
    },
    "RICHARDSON": {
        "full_name": "Bill Richardson",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1947, 11, 15)
    },
    "DODD": {
        "full_name": "Chris Dodd",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1944, 5, 27)
    },
    "GRAVEL": {
        "full_name": "Mike Gravel",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1930, 5, 13)
    },
    "ROMNEY": {
        "full_name": "Mitt Romney",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1947, 3, 12)
    },
    "GIULIANI": {
        "full_name": "Rudy Giuliani",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1944, 5, 28)
    },
    "HUCKABEE": {
        "full_name": "Mike Huckabee",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1955, 8, 24)
    },
    "THOMPSON": {
        "full_name": "Fred Thompson",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1942, 8, 19)
    },
    "PAUL": {
        "full_name": "Ron Paul",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1935, 8, 20)
    },
    "TANCREDO": {
        "full_name": "Tom Tancredo",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1945, 12, 20)
    },
    "BROWNBACK": {
        "full_name": "Sam Brownback",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1956, 9, 12)
    },
    "HUNTER": {
        "full_name": "Duncan Hunter",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1948, 5, 31)
    },
    "PALIN": {
        "full_name": "Sarah Palin",
        "party": Party.REPUBLICAN,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1964, 2, 11)
    },
    "SANTORUM": {
        "full_name": "Rick Santorum",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1958, 5, 10)
    },
    "GINGRICH": {
        "full_name": "Newt Gingrich",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1943, 6, 17)
    },
    "BACHMANN": {
        "full_name": "Michele Bachmann",
        "party": Party.REPUBLICAN,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1956, 4, 6)
    },
    "PERRY": {
        "full_name": "Rick Perry",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1950, 3, 4)
    },
    "CAIN": {
        "full_name": "Herman Cain",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1945, 12, 13)
    },
    "HUNTSMAN": {
        "full_name": "Jon Huntsman",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1960, 3, 26)
    },
    "PAWLENTY": {
        "full_name": "Tim Pawlenty",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1960, 11, 27)
    },
    "RYAN": {
        "full_name": "Paul Ryan",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1970, 1, 29)
    },
    "TRUMP": {
        "full_name": "Donald Trump",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1946, 6, 14)
    },
    "SANDERS": {
        "full_name": "Bernie Sanders",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1941, 9, 8)
    },
    "CRUZ": {
        "full_name": "Ted Cruz",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1970, 12, 22)
    },
    "RUBIO": {
        "full_name": "Marco Rubio",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1971, 5, 28)
    },
    "CARSON": {
        "full_name": "Ben Carson",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1951, 9, 18)
    },
    "CHRISTIE": {
        "full_name": "Chris Christie",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1962, 9, 6)
    },
    "KASICH": {
        "full_name": "John Kasich",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1952, 5, 13)
    },
    "FIORINA": {
        "full_name": "Carly Fiorina",
        "party": Party.REPUBLICAN,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1954, 9, 6)
    },
    "WALKER": {
        "full_name": "Scott Walker",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1967, 11, 2)
    },
    "JINDAL": {
        "full_name": "Bobby Jindal",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1971, 6, 10)
    },
    "GRAHAM": {
        "full_name": "Lindsey Graham",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1955, 7, 9)
    },
    "PATAKI": {
        "full_name": "George Pataki",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1945, 6, 24)
    },
    "GILMORE": {
        "full_name": "Jim Gilmore",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1949, 10, 6)
    },
    "O_MALLEY": {
        "full_name": "Martin O'Malley",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1963, 1, 18)
    },
    "WEBB": {
        "full_name": "Jim Webb",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1946, 2, 9)
    },
    "CHAFEE": {
        "full_name": "Lincoln Chafee",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1953, 3, 26)
    },
    "PENCE": {
        "full_name": "Mike Pence",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1959, 6, 7)
    },
    "KAINE": {
        "full_name": "Tim Kaine",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1958, 2, 26)
    },
    "HARRIS": {
        "full_name": "Kamala Harris",
        "party": Party.DEMOCRAT,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1964, 10, 20)
    },
    "WARREN": {
        "full_name": "Elizabeth Warren",
        "party": Party.DEMOCRAT,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1949, 6, 22)
    },
    "BUTTIGIEG": {
        "full_name": "Pete Buttigieg",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1982, 1, 19)
    },
    "KLOBUCHAR": {
        "full_name": "Amy Klobuchar",
        "party": Party.DEMOCRAT,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1960, 5, 25)
    },
    "YANG": {
        "full_name": "Andrew Yang",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1975, 1, 13)
    },
    "BOOKER": {
        "full_name": "Cory Booker",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1969, 4, 27)
    },
    "CASTRO": {
        "full_name": "Julián Castro",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1974, 9, 16)
    },
    "GABBARD": {
        "full_name": "Tulsi Gabbard",
        "party": Party.DEMOCRAT,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1981, 4, 12)
    },
    "BETO": {
        "full_name": "Beto O'Rourke",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1972, 9, 26)
    },
    "INSLEE": {
        "full_name": "Jay Inslee",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1951, 2, 9)
    },
    "DE_BLASIO": {
        "full_name": "Bill de Blasio",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1961, 5, 8)
    },
    "GILLIBRAND": {
        "full_name": "Kirsten Gillibrand",
        "party": Party.DEMOCRAT,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1966, 12, 9)
    },
    "HICKENLOOPER": {
        "full_name": "John Hickenlooper",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1952, 2, 7)
    },
    "BENNET": {
        "full_name": "Michael Bennet",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1964, 11, 28)
    },
    "CLINTON_H": {
        "full_name": "Hillary Clinton",
        "party": Party.DEMOCRAT,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1947, 10, 26)
    },
    "BUSH_J": {
        "full_name": "Jeb Bush",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1953, 2, 11)
    },
    "BUSH_G": {
        "full_name": "George W. Bush",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1946, 7, 6)
    },
    "RYAN_T": {
        "full_name": "Tim Ryan",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1973, 7, 16)
    },
    "SWALWELL": {
        "full_name": "Eric Swalwell",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1980, 11, 16)
    },
    "WILLIAMSON": {
        "full_name": "Marianne Williamson",
        "party": Party.DEMOCRAT,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1952, 7, 8)
    },
    "DELANEY": {
        "full_name": "John Delaney",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1963, 4, 16)
    },
    "BULLOCK": {
        "full_name": "Steve Bullock",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1966, 4, 11)
    },
    "MESSAM": {
        "full_name": "Wayne Messam",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1974, 6, 6)
    },
    "SESTAK": {
        "full_name": "Joe Sestak",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1951, 12, 12)
    },
    "STEYER": {
        "full_name": "Tom Steyer",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1957, 6, 27)
    },
    "BLOOMBERG": {
        "full_name": "Michael Bloomberg",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1942, 2, 14)
    },
    "HALEY": {
        "full_name": "Nikki Haley",
        "party": Party.REPUBLICAN,
        "gender": Gender.FEMALE,
        "date_of_birth": date(1972, 1, 20)
    },
    "DESANTIS": {
        "full_name": "Ron DeSantis",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1978, 9, 14)
    },
    "RAMASWAMY": {
        "full_name": "Vivek Ramaswamy",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1985, 8, 9)
    },
    "SCOTT": {
        "full_name": "Tim Scott",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1965, 9, 19)
    },
    "VANCE": {
        "full_name": "J.D. Vance",
        "party": Party.REPUBLICAN,
        "gender": Gender.MALE,
        "date_of_birth": date(1984, 8, 2)
    },
    "WALZ": {
        "full_name": "Tim Walz",
        "party": Party.DEMOCRAT,
        "gender": Gender.MALE,
        "date_of_birth": date(1964, 4, 6)
    },
}



def get_politician_info(name):
    return POLITICIANS_DATA.get(name)

def is_politician(name):
    return name in POLITICIANS_DATA
