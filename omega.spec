Summary:	Old and very difficult roguelike game
Summary(pl.UTF-8):   Stara i bardzo trudna gra roguelike
Name:		omega
Version:	0.80.2
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://yarws.kid.waw.pl/files/%{name}.tar.gz
# Source0-md5:	b5dafc2f2e41cc40e3eb356074f3a152
Source1:	http://yarws.kid.waw.pl/files/%{name}_spoiler.zip
# Source1-md5:	cb9564f6def21e91ab0824f3f23b4c34
Source2:	http://yarws.kid.waw.pl/files/%{name}_faq.zip
# Source2-md5:	744607cd937ca8478881204c901e00eb
Patch0:		%{name}-config.patch
Patch1:		%{name}-shit.patch
URL:		http://www.alcyone.com/max/projects/omega/
BuildRequires:	ncurses-devel
BuildRequires:	unzip
Requires:	gzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
(ESTABLISHING SHOT) A weary ADVENTURER, wearing battered armor and 10
glowing rings, clutching a potion bottle, and laden with all manner of
weapons, magical devices, and sacks of gold, lies panting on the
ground outside of the seedy-looking entrance to a grimy Dungeon. The
nearby scenery is uniformly grey and uninteresting.

Bluff Male Voice: Retrieved the Amulet of Yendor too many times to
count?

Sultry Female Voice: Can't see anything in the Eye of Larn?

BMV: Eaten one too many Zombie corpses?

SFV: Run out of Greater Gods to kill?

CLOSE-UP: The ADVENTURER's sweat-streaked face, which is nicked and
bruised. He has a black eye.

The ADVENTURER nods wearily, and, it seems, with some boredom.

MBV+SFV: Then take the ultimate challenge ... The final quest ...
OMEGA!

(PAN VERTICALLY TOWARD SKY) The Mormon Tabernacle Choir: Ooooooo --
mega!

A shaft of brilliant sunlight pierces the overcast sky, revealing a
Mystic Portal in the sky. A rainbow bridge lances from the portal
toward the ADVENTURER. As the ADVENTURER hesitantly sets foot on the
bridge, he (with the viewer) is swept through the M.P. in a
masterpiece of computer animation. There is a flash of light, and a
TRANSFORMED ADVENTURER, in newly polished and chromed armor, wielding
a flaming sword, strides confidently toward an edifice that makes the
Castle of Ultimate Darkness look like a sandcastle. The landscape is
vibrantly colored, and we feel that there are new challenges awaiting
just over the horizon.

TMTC: Magnificat! Magnificat! Magnificat!

BMV: Coming Soon to a site near you!

SFV: Challenge Omega -- The Final Quest!

As the ADVENTURER passes through the entrance to the AWESOME CASTLE, a
giant portcullis slams shut behind him with the force of a Death Star
bulkhead, and we hear a muffled scream, soon cut off.

Satanic Male Voice: If you dare! <laughs insanely>

%description -l pl.UTF-8
(UJĘCIE POCZĄTKOWE) Zmęczony POSZUKIWACZ PRZYGÓD w poobijanej zbroi,
noszący 10 świecących pierścieni, ściskający w dłoni butelkę z
napojem, i załadowany wszelakimi rodzajami broni, magicznych urządzeń
oraz sakw ze złotem sapie leżąc przed złowieszczym wejściem do
ponurego Lochu. Okoliczna sceneria jest jednako szara i
nieinteresująca.

Szorstki Męski Głos: Odzyskałeś Amulet Yendoru zbyt wiele razy, by móc
zliczyć?

Zmysłowy Kobiecy Głos: Nie widzisz nic w Oku Larna?

SMG: Zjadłeś zbyt dużo Zombich?

ZKG: Skończyli się Wyżsi Bogowie do zabicia?

ZBLIŻENIE: Twarz POSZUKIWACZA PRZYGÓD, spływająca strużkami potu, jest
pocięta i posiniaczona. Łypie z niej czarne oko.

POSZUKIWACZ PRZYGÓD skinął głową ze zmęczeniem, a także, jak można
zauważyć, z pewnym znudzeniem.

SMG+ZKG: Zatem podejmij się ostatecznego wyzwania... Ostatniego
zadania... OMEGA!

(SPOJRZENIE W KIERUNKU NIEBA) Chór Mormońskiej Świątyni: Ooooooo --
mega!

Jasny słoneczny promień przebija się przez zachmurzone niebo, ukazując
Mistyczny Portal w niebie. Tęczowy most pędzi od portalu ku
POSZUKIWACZOWI PRZYGÓD. Gdy POSZUKIWACZ PRZYGÓD niepewnie stawia stopę
na moście, zostaje (wraz z oglądającym) zmieciony poprzez M.P. w
mistrzowskiej animacji komputerowej. Następuje błysk światła i
ODMIENIONY POSZUKIWACZ PRZYGÓD, w świeżo wypolerowanej, błyszczącej
zbroi, trzymający płonący miecz, kroczy pewny siebie ku gmachowi, przy
którym Zamek Ostatecznej Ciemnoty wygląda jak zamek z piasku.
Otaczający teren jest pełen żywych kolorów. Czuje się, że nowe
wyzwania czekają tuż nad horyzontem.

CMŚ: Wspaniałość! Wspaniałość! Wspaniałość!

SMG: Wkrótce na pobliskich maszynach!

ZKG: Podejmij się Omegi -- Ostatecznego Zadania!

Gdy POSZUKIWACZ PRZYGÓD przekracza wejście do STRASZLIWEGO ZAMKU,
ogromna krata zatrzaskuje się za nim z siłą grodzi Gwiazdy Śmierci, po
czym słychać głuchy krzyk, szybko ucięty.

Szatański Męski Głos: Jeżeli się odważysz! <szalony śmiech>

%prep
%setup -q -a1 -a2 -n %{name}
%patch0 -p1
%patch1 -p1

%build
cd src
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DSYSV -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_datadir}/omega,/var/games/omega}

install src/omega $RPM_BUILD_ROOT%{_bindir}
install omegalib/* $RPM_BUILD_ROOT%{_datadir}/omega
install docs/omega.6 $RPM_BUILD_ROOT%{_mandir}/man6

touch $RPM_BUILD_ROOT/var/games/omega/omega.{hi,log}
rm -f $RPM_BUILD_ROOT%{_datadir}/omega/omega*
ln -sf /var/games/omega/omega.hi $RPM_BUILD_ROOT%{_datadir}/omega/omega.hi
ln -sf /var/games/omega/omega.log $RPM_BUILD_ROOT%{_datadir}/omega/omega.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc omega_faq.txt omega_spoiler.txt
%attr(2755,root,games) %{_bindir}/omega
%{_datadir}/omega
%dir /var/games/omega
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/omega/omega.hi
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/omega/omega.log
%{_mandir}/man6/*
