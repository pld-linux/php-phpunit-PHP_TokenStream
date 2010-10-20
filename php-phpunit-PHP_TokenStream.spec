%include	/usr/lib/rpm/macros.php
%define		status		stable
%define		pearname	PHP_TokenStream
Summary:	%{pearname} - Wrapper around PHP's tokenizer extension
Name:		php-phpunit-PHP_TokenStream
Version:	1.0.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	86625f347f55128ff0d935ab6aacba32
URL:		http://pear.phpunit.de/package/PHP_TokenStream/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
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
install -p usr/bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/phptok
%{php_pear_dir}/PHP/Token
%{php_pear_dir}/PHP/Token.php
