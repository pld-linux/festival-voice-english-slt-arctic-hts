Summary:	US English female speaker "SLT" for Festival
Summary(pl.UTF-8):	Angielski (amerykański) głos żeński "SLT" dla Festivala
Name:		festival-voice-english-slt-arctic-hts
Version:	2.1
Release:	3
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/downloads/festival/%{version}/festvox_cmu_us_slt_arctic_hts.tar.gz
# Source0-md5:	a9b53441968f6bc612b85c04bbc4cf0f
URL:		http://www.cstr.ed.ac.uk/projects/festival/
Requires:	festival >= 2.1
Provides:	festival-voice
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
US English female speaker ("SLT") voice for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the
Nagoya Institute of Technology, trained using the CMU ARCTIC database.
This voice is based on 1132 utterances spoken by a US English female
speaker. The speaker is experienced in building synthetic voices. This
was recorded at 16bit 32kHz, in a sound proof room, in stereo, one
channel was the waveform, the other EGG. The database was
automatically labelled using CMU Sphinx using the FestVox labelling
scripts. No hand correction has been made.

%description
Angielski (amerykański) głos żeński "SLT" dla syntezatora Festival.

Jest to głos oparty na systemie syntezy mowy HMM (HTS) stworzony w
Nagoya Institute of Technology, uczony przy użyciu bazy danych CMU
ARCTIC. Głos jest oparty na 1132 wyrażeniach mówionych w amerykańskiej
odmianie języka angielskiego przez kobietę mającą doświadczenie w
tworzeniu głosów syntetycznych. Nagranie wykonano w 16 bitach przy
32kHz, w dźwiękoszczelnym pomieszczeniu, stereofonicznie - jeden kanał
był właściwą falą, drugi EGG. Baza danych była automatycznie oznaczana
przez CMU Sphinx przy użyciu skryptów oznaczających FestVox. Nie były
wykonywane żadne ręczne korekty.

%prep
%setup -q -c

%{__mv} festival/lib/voices/us/cmu_us_slt_arctic_hts/{COPYING,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

cp -pr festival $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%{_datadir}/festival/lib/voices/us/cmu_us_slt_arctic_hts
