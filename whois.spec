Name:       whois       
Version:    5.0.26
Release:    1%{?dist}
Summary:    Improved WHOIS client
Group:      Applications/Internet
License:    GPLv2+
URL:        http://www.linux.it/~md/software/
Source0:    http://ftp.debian.org/debian/pool/main/w/%{name}/%{name}_%{version}.tar.xz
BuildRequires:  gettext
BuildRequires:  libidn-devel
BuildRequires:  perl
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives


%define genname whois
%define alternative md
%define cfgfile %{name}.conf

%description
Searches for an object in a RFC 3912 database.

This version of the WHOIS client tries to guess the right server to ask for
the specified object. If no guess can be made it will connect to
whois.networksolutions.com for NIC handles or whois.arin.net for IPv4
addresses and network names.


%prep
%setup -q -n %{name}-%{version}


%build
make CONFIG_FILE="%{_sysconfdir}/%{cfgfile}" HAVE_LIBIDN=1 HAVE_ICONV=1 \
    CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}


%install
# Omit mkpasswd
make install-whois install-pos BASEDIR=$RPM_BUILD_ROOT 
install -p -m644 -D %{cfgfile} $RPM_BUILD_ROOT%{_sysconfdir}/%{cfgfile}
%find_lang %{name}

# Rename to alternative names
mv $RPM_BUILD_ROOT%{_bindir}/%{name}{,.%{alternative}}
touch $RPM_BUILD_ROOT%{_bindir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT%{_mandir}/man1/%{name}{,.%{alternative}}.1
touch $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1


%post
%{_sbindir}/update-alternatives \
    --install %{_bindir}/%{name} \
        %{genname} %{_bindir}/%{name}.%{alternative} 30 \
    --slave %{_mandir}/man1/%{name}.1.gz \
        %{genname}-man %{_mandir}/man1/%{name}.%{alternative}.1.gz 

%postun
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove \
        %{genname} %{_bindir}/%{name}.%{alternative}
fi


%files -f %{name}.lang
%doc COPYING README debian/changelog debian/copyright
%config(noreplace) %{_sysconfdir}/%{cfgfile}
%{_bindir}/%{name}.%{alternative}
%ghost %verify(not md5 size mtime) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.%{alternative}.*
%ghost %verify(not md5 size mtime) %{_mandir}/man1/%{name}.1.gz
%{_mandir}/man5/%{cfgfile}.5.gz


%changelog
* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 5.0.26-1
- 5.0.26 bump

* Mon May 13 2013 Petr Pisar <ppisar@redhat.com> - 5.0.25-1
- 5.0.25 bump

* Thu Apr 18 2013 Petr Pisar <ppisar@redhat.com> - 5.0.24-1
- 5.0.24 bump

* Mon Apr 08 2013 Petr Pisar <ppisar@redhat.com> - 5.0.23-1
- 5.0.23 bump

* Thu Apr 04 2013 Petr Pisar <ppisar@redhat.com> - 5.0.22-1
- 5.0.22 bump

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 08 2012 Petr Pisar <ppisar@redhat.com> - 5.0.20-1
- 5.0.20 bump

* Wed Sep 19 2012 Petr Pisar <ppisar@redhat.com> - 5.0.19-1
- 5.0.19 bump

* Thu Aug 02 2012 Petr Pisar <ppisar@redhat.com> - 5.0.18-1
- 5.0.18 bump

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Petr Pisar <ppisar@redhat.com> - 5.0.17-2
- .xn--mgbaam7a8 is handled by whois.aeda.net.ae (bug #839893)
- Document how to write IDN in whois.conf (bug #839898)

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 5.0.17-1
- 5.0.17 bump

* Mon Apr 30 2012 Petr Pisar <ppisar@redhat.com> - 5.0.16-1
- 5.0.16 bump

* Thu Mar 08 2012 Petr Pisar <ppisar@redhat.com> - 5.0.15-1
- 5.0.15 bump

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 02 2012 Petr Pisar <ppisar@redhat.com> - 5.0.14-1
- 5.0.14 bump

* Mon Nov 28 2011 Petr Pisar <ppisar@redhat.com> - 5.0.13-1
- 5.0.13 bump

* Wed Oct 12 2011 Petr Pisar <ppisar@redhat.com> - 5.0.12-1
- 5.0.12 bump
- Remove defattr from spec code

* Thu Mar 03 2011 Petr Pisar <ppisar@redhat.com> - 5.0.11-1
- 5.0.11 bump

* Mon Dec 06 2010 Petr Pisar <ppisar@redhat.com> - 5.0.10-1
- 5.0.10 bump

* Wed Sep 29 2010 Petr Pisar <ppisar@redhat.com> - 5.0.7-1
- 5.0.7 imported

