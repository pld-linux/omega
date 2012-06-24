Summary:	Old and very difficult roguelike game
Summary(pl):	Stara i bardzo trudna gra roguelike
Name:		omega
Version:	0.80.2
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://yarws.kid.waw.pl/files/%{name}.tar.gz
Source1:	http://yarws.kid.waw.pl/files/%{name}_spoiler.zip
Source2:	http://yarws.kid.waw.pl/files/%{name}_faq.zip
Patch0:		%{name}-config.patch
Patch1:		%{name}-shit.patch
URL:		http://www.alcyone.com/max/projects/omega/
BuildRequires:	ncurses-devel
Requires:	gzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_prefix}/games

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

%description -l pl
(UJ�CIE POCZ�TKOWE) Zm�czony POSZUKIWACZ PRZYG�D w poobijanej zbroi,
nosz�cy 10 �wiec�cych pier�cieni, �ciskaj�cy w d�oni butelk�
z napojem, i za�adowany wszelakimi rodzajami broni, magicznych
urz�dze� oraz sakw ze z�otem sapie le��c przed z�owieszczym wej�ciem
do ponurego Lochu. Okoliczna sceneria jest jednako szara
i nieinteresuj�ca.

Szorstki M�ski G�os: Odzyska�e� Amulet Yendoru zbyt wiele razy, by m�c
zliczy�?

Zmys�owy Kobiecy G�os: Nie widzisz nic w Oku Larna?

SMG: Zjad�e� zbyt du�o Zombich?

ZKG: Sko�czyli si� Wy�si Bogowie do zabicia?

ZBLI�ENIE: Twarz POSZUKIWACZA PRZYG�D, sp�ywaj�ca stru�kami potu,
jest poci�ta i posiniaczona. �ypie z niej czarne oko.

POSZUKIWACZ PRZYG�D skin�� g�ow� ze zm�czeniem, a tak�e, jak mo�na
zauwa�y�, z pewnym znudzeniem.

SMG+ZKG: Zatem podejmij si� ostatecznego wyzwania... Ostatniego
zadania... OMEGA!

(SPOJRZENIE W KIERUNKU NIEBA) Ch�r Mormo�skiej �wi�tyni: Ooooooo --
mega!

Jasny s�oneczny promie� przebija si� przez zachmurzone niebo, ukazuj�c
Mistyczny Portal w niebie. T�czowy most p�dzi od portalu ku
POSZUKIWACZOWI PRZYG�D. Gdy POSZUKIWACZ PRZYG�D niepewnie stawia stop�
na mo�cie, zostaje (wraz z ogl�daj�cym) zmieciony poprzez M.P.
w mistrzowskiej animacji komputerowej. Nast�puje b�ysk �wiat�a
i ODMIENIONY POSZUKIWACZ PRZYG�D, w �wie�o wypolerowanej, b�yszcz�cej
zbroi, trzymaj�cy p�on�cy miecz, kroczy pewny siebie ku gmachowi, przy
kt�rym Zamek Ostatecznej Ciemnoty wygl�da jak zamek z piasku.
Otaczaj�cy teren jest pe�en �ywych kolor�w. Czuje si�, �e nowe
wyzwania czekaj� tu� nad horyzontem.

CM�: Wspania�o��! Wspania�o��! Wspania�o��!

SMG: Wkr�tce na pobliskich maszynach!

ZKG: Podejmij si� Omegi -- Ostatecznego Zadania!

Gdy POSZUKIWACZ PRZYG�D przekracza wej�cie do STRASZLIWEGO ZAMKU,
ogromna krata zatrzaskuje si� za nim z si�� grodzi Gwiazdy �mierci, po
czym s�ycha� g�uchy krzyk, szybko uci�ty.

Szata�ski M�ski G�os: Je�eli si� odwa�ysz! <szalony �miech>

%prep
%setup -q -a1 -a2 -n %{name}
%patch0 -p1
%patch1 -p1

%build
cd src
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DSYSV -I%{_includedir}/ncurses" \
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
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) /var/games/omega/omega.hi
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) /var/games/omega/omega.log
%{_mandir}/man6/*
