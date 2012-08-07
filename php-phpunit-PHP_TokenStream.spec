%define		status		stable
%define		pearname	PHP_TokenStream
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Wrapper around PHP's tokenizer extension
Name:		php-phpunit-PHP_TokenStream
Version:	1.1.3
Release:	2
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	a97af36d83d30ea14f28ed72ad5e3309
URL:		http://pear.phpunit.de/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(tokenizer)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-ezc-ConsoleTools >= 1.6
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper around PHP's tokenizer extension.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/PHP_TokenStream/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/PHP/Token.php
%{php_pear_dir}/PHP/Token
