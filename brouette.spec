Summary:        Gets notifications from the prelude manager
Name:           brouette
Version:        0.0
Release:        %mkrel 0.8575.1
Epoch:          0
License:        GPL
Group:          System/Servers
URL:            http://www.prelude-ids.org/
Source0:        brouette-8575.tar.bz2
BuildRequires:  libnotify-devel
BuildRequires:  libprelude-devel >= 0:0.9.10
Requires:       prelude-manager
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Brouette gets notifications from the prelude manager.

%prep
%setup -q -n %{name}
%{_bindir}/find . -type d -name .svn | %{_bindir}/xargs %{__rm} -rf

%build
%{make} CC=%{__cc} CFLAGS="%{optflags} `%{_bindir}/libprelude-config --cflags` `%{_bindir}/pkg-config libnotify --cflags`"

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a brouette %{buildroot}%{_bindir}/brouette

%{__cat} > README.urpmi << EOF
In order to start the brouette service you must configure it first.
This is not done automatically. To make a basic configuration,
please run:

%{_bindir}/prelude-adduser register brouette "idmef:r admin:r" localhost --uid 500 --gid 500

Then run:

%{_bindir}/brouette localhost

at desktop startup.
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc INSTALL README README.urpmi doc/foobar.jpg
%attr(0755,root,root) %{_bindir}/brouette


