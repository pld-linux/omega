Summary:	Complex roguelike game
Summary(pl):	Rozbudowana gra roguelike
Name:		omega
Version:	0.80.2
Release:	0.9
License:	GPL
Group:		Applications/Games
Source0:	http://yarws.kid.waw.pl/files/%{name}.tar.gz
Source1:	http://yarws.kid.waw.pl/files/%{name}_spoiler.zip
Source2:	http://yarws.kid.waw.pl/files/%{name}_faq.zip
Patch0:		%{name}-config.patch
Patch1:		%{name}-shit.patch
URL:		http://www.alcyone.com/max/projects/omega/
Requires:	gzip
BuildRequires:	ncurses-devel
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_datadir}/omega}

install src/omega $RPM_BUILD_ROOT%{_bindir}
install omegalib/* $RPM_BUILD_ROOT%{_datadir}/omega
install docs/omega.6 $RPM_BUILD_ROOT%{_mandir}/man6

gzip -9nf omega_faq.txt omega_spoiler.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/omega
%{_mandir}/man6/*
