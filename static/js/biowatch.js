const getOsInfo = () => {
  if (typeof window === "undefined") {
    return { os: null, url: "", text: "Download Biowatch" };
  }

  const userAgent = window.navigator.userAgent;

  if (userAgent.indexOf("Win") !== -1) {
    return {
      os: "windows",
      url: "https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch-1.0.14-setup.exe",
      text: "Download for Windows",
    };
  } else if (userAgent.indexOf("Mac") !== -1) {
    return {
      os: "mac",
      url: "https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch-1.0.14.dmg",
      text: "Download for macOS",
    };
  } else if (userAgent.indexOf("Linux") !== -1) {
    return {
      os: "linux",
      url: "https://github.com/earthtoolsmaker/biowatch/releases/latest/download/biowatch-1.0.14.AppImage",
      text: "Download for Linux",
    };
  } else {
    return {
      os: null,
      url: "https://github.com/earthtoolsmaker/biowatch/releases/latest",
      text: "Download Biowatch",
    };
  }
};

window.addEventListener(
  "load",
  function() {
    // Need to be loaded
    Lightense(".lightense-enabled", {});
  },
  false,
);
