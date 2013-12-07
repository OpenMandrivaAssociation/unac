%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Summary: A command that removes accents
Name: unac
Version: 1.8.0
Release: 8
License: GPLv2+
Group: Text tools
Source0: http://ftp.de.debian.org/debian/pool/main/u/unac/unac_%version.orig.tar.gz
Patch0: unac-automake-1.13.patch
URL: http://www.nongnu.org/unac/
BuildRequires: gettext-devel

%description
unac is a C library and command that remove accents from a string.
For instance the string été will become ete.  It provides a command
line interface that removes accents from a string given in argument
(unaccent command). In the library function and the command, the
charset of the input string is specified as an argument. The input
string is converted to UTF-16 using iconv(3), accents are stripped and
the result is converted back to the original charset. The iconv --list
command on GNU/Linux will show all charset supported.

%package -n %libname
Group:System/Libraries
Summary: A C library that removes accents

%description -n %libname
unac is a C library and command that remove accents from a string.
For instance the string été will become ete.  It provides a command
line interface that removes accents from a string given in argument
(unaccent command). In the library function and the command, the
charset of the input string is specified as an argument. The input
string is converted to UTF-16 using iconv(3), accents are stripped and
the result is converted back to the original charset. The iconv --list
command on GNU/Linux will show all charset supported.

%package -n %develname
Group: Development/C
Summary: A C library that removes accents
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
unac is a C library and command that remove accents from a string.
For instance the string été will become ete.  It provides a command
line interface that removes accents from a string given in argument
(unaccent command). In the library function and the command, the
charset of the input string is specified as an argument. The input
string is converted to UTF-16 using iconv(3), accents are stripped and
the result is converted back to the original charset. The iconv --list
command on GNU/Linux will show all charset supported.

%prep
%setup -q -n %name-%version.orig
%apply_patches
touch config.rpath
autoreconf -fi

%build

%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_bindir}/unaccent
%_mandir/man1/unaccent.1*

%files -n %libname
%defattr(-,root,root)
%_libdir/libunac.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/libunac*a
%_libdir/libunac*so
%_libdir/pkgconfig/unac.pc
%{_includedir}/unac.h
%{_mandir}/man3/unac.3*



%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.0-3mdv2011.0
+ Revision: 670743
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.0-2mdv2011.0
+ Revision: 608104
- rebuild

* Fri Jan 01 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.8.0-1mdv2010.1
+ Revision: 484860
- import unac


* Fri Jan  1 2010 Götz Waschk <waschk@mandriva.org> 1.8.0-1mdv2010.1
- adapt for mandriva

* Fri Sep 21 2000 Loic Dachary <loic@senga.org>
- Create
