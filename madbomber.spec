%define	name	madbomber
%define	version	0.2.5
%define release	%mkrel 2
%define summary	Catch the bombs

Summary:	%{summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Url:		http://newbreedsoftware.com/madbomber
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/madbomber/%{name}-%{version}.tar.bz2
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
License:	GPL
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	SDL_mixer-devel SDL_image-devel X11-devel libalsa-devel esound-devel
Patch:		madbomber-0.1.8-fix-CFLAGS.patch.bz2
Patch1:		madbomber-0.2.4-add-keypad-keys.patch.bz2

%description
The Mad Bomber is loose in the city and he's dropping bombs everywhere! It's
your job to catch them before they hit the ground and explode. Luckily, you
have a set of trusty buckets to extinguish them with.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -z .pix
chmod a+r -R .
# remove .xvpics directories
find . -type d -name .xvpics | xargs rm -rf

cat <<EOF > %{name}.menu
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		  icon=%{name}.png \
		  needs="x11" \
		  section="More Applications/Games/Arcade" \
		  title="MadBomber"\
		  longtitle="%{summary}" xdg="true"
EOF

cat << EOF > mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=MadBomber
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%build
%make CFLAGS="%{optflags}" DATA_PREFIX=%{_gamesdatadir}/%{name}/

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
install -d $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
cp -a data/* $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}

install -D -m644 mandriva-%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop
install -D -m644 %SOURCE6 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m644 %SOURCE5 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -D -m644 %SOURCE7 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS.txt CHANGES.txt README.txt
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png

