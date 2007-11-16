Summary:        Gets notifications from the prelude manager
Name:           brouette
Version:        0.1
Release:        %mkrel 0.10045.2
Epoch:          0
License:        GPL
Group:          System/Servers
URL:            http://www.prelude-ids.org/
Source0:        brouette-10045.tar.bz2
BuildRequires:  libnotify-devel
BuildRequires:  prelude-devel
Requires:       prelude-manager
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Brouette gets notifications from the prelude manager.

%prep
%setup -q -n %{name}
%{_bindir}/find . -type d -name .svn | %{_bindir}/xargs %{__rm} -r
./autogen.sh

%{__cat} > README.urpmi << EOF
In order to start the brouette service you must configure it first.
This is not done automatically. To make a basic configuration,
please run:

%{_bindir}/prelude-adduser register brouette "idmef:r admin:r" localhost --uid 500 --gid 500

Then run:

%{_bindir}/brouette localhost

at desktop startup.
EOF

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.urpmi doc/*
%attr(0755,root,root) %{_bindir}/brouette
%{_datadir}/brouette
%dir %{_sysconfdir}/brouette
%config(noreplace) %{_sysconfdir}/brouette/brouette.conf
