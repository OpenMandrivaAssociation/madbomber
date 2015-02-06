%define	name	madbomber
%define	version	0.2.5
%define release	8
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
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL-devel
Patch0:		madbomber-0.1.8-fix-CFLAGS.patch
Patch1:		madbomber-0.2.4-add-keypad-keys.patch

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

cat << EOF > mandriva-%{name}.desktop
[Desktop Entry]
Name=MadBomber
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%build
%make CFLAGS="%{optflags} %{ldflags}" DATA_PREFIX=%{_gamesdatadir}/%{name}/

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


%changelog
* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 0.2.5-7mdv2011.0
+ Revision: 636077
- tighten BR
- bunzip2 the patch

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.5-6mdv2011.0
+ Revision: 612790
- the mass rebuild of 2010.1 packages

* Fri Dec 04 2009 Jérôme Brenier <incubusss@mandriva.org> 0.2.5-5mdv2010.1
+ Revision: 473420
- number the first patch to fix build

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.2.5-4mdv2009.0
+ Revision: 251640
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.2.5-2mdv2008.1
+ Revision: 140934
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - import madbomber


* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 0.2.5-2mdv2007.0
- switch to XDG menu

* Mon May 29 2006 Emmanuel Andry <eandry@mandriva.org> 0.2.5-1mdk
- 0.2.5
- mkrel

* Tue Oct 11 2005 Pixel <pixel@mandriva.com> 0.2.4-7mdk
- rebuild

* Fri Jun  4 2004 Pixel <pixel@mandrakesoft.com> 0.2.4-6mdk
- rebuild

* Sun Mar 23 2003 Pixel <pixel@mandrakesoft.com> 0.2.4-5mdk
- removed lurking .xvpics directories

* Thu Nov 12 2002 Per �yvind Karlsen <peroyvind@delonic.no> 0.2.4-4mdk
- Removed obsolete Prefix tag
- Removed redundant BuildRequires
- Cleanups
- Added menuitem
- Added icons
- Moved stuff to the correct places

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2.4-3mdk
- rebuild

* Sun Jul 21 2002 Pixel <pixel@mandrakesoft.com> 0.2.4-2mdk
- recompile against new vorbis stuff

* Thu Jun 27 2002 Pixel <pixel@mandrakesoft.com> 0.2.4-1mdk
- new release

* Mon Apr 29 2002 Pixel <pixel@mandrakesoft.com> 0.1.8-12mdk
- rebuild for new libasound (alsa)

* Tue Jan 22 2002 Stefan van der Eijk <stefan@eijk.nu> 0.1.8-11mdk
- BuildRequires

* Thu Oct 11 2001 Pixel <pixel@mandrakesoft.com> 0.1.8-10mdk
- rebuilding for libpng3

* Thu Sep 13 2001 Stefan van der Eijk <stefan@eijk.nu> 0.1.8-9mdk
- BuildRequires: libSDL-devel

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 0.1.8-8mdk
- fix rights
- rebuild

* Mon Jul  2 2001 Pixel <pixel@mandrakesoft.com> 0.1.8-7mdk
- fix description

* Mon May 14 2001 Pixel <pixel@mandrakesoft.com> 0.1.8-6mdk
- rebuild with new SDL

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-5mdk
- rebuild with new libSDL_mixer

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-4mdk
- rebuild, build req

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-3mdk
- capitalize summary

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-2mdk
- rebuild

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 0.1.8-1mdk
- initial spec
