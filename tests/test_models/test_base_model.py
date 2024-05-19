





<!DOCTYPE html>
<html class="gl-light ui-neutral with-header with-top-bar " lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="width=device-width, initial-scale=1" name="viewport">
<title>tests/test_models/test_base_model.py · master · Hagos Mehari / AirBnB_clone · GitLab</title>
<script nonce="LZ24xD8IvXP1KEY7U+tvLQ==">
//<![CDATA[
window.gon={};gon.math_rendering_limits_enabled=true;gon.features={"explainCodeChat":false};gon.licensed_features={"remoteDevelopment":true};
//]]>
</script>


<script nonce="LZ24xD8IvXP1KEY7U+tvLQ==">
//<![CDATA[
var gl = window.gl || {};
gl.startup_calls = null;
gl.startup_graphql_calls = [{"query":"query getBlobInfo(\n  $projectPath: ID!\n  $filePath: String!\n  $ref: String!\n  $refType: RefType\n  $shouldFetchRawText: Boolean!\n) {\n  project(fullPath: $projectPath) {\n    __typename\n    id\n    repository {\n      __typename\n      empty\n      blobs(paths: [$filePath], ref: $ref, refType: $refType) {\n        __typename\n        nodes {\n          __typename\n          id\n          webPath\n          name\n          size\n          rawSize\n          rawTextBlob @include(if: $shouldFetchRawText)\n          fileType\n          language\n          path\n          blamePath\n          editBlobPath\n          gitpodBlobUrl\n          ideEditPath\n          forkAndEditPath\n          ideForkAndEditPath\n          codeNavigationPath\n          projectBlobPathRoot\n          forkAndViewPath\n          environmentFormattedExternalUrl\n          environmentExternalUrlForRouteMap\n          canModifyBlob\n          canCurrentUserPushToBranch\n          archived\n          storedExternally\n          externalStorage\n          externalStorageUrl\n          rawPath\n          replacePath\n          pipelineEditorPath\n          simpleViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n          richViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n        }\n      }\n    }\n  }\n}\n","variables":{"projectPath":"hkm2023/AirBnB_clone","ref":"master","refType":"","filePath":"tests/test_models/test_base_model.py","shouldFetchRawText":true}}];

if (gl.startup_calls && window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall => {
   gl.startup_calls[apiCall] = {
      fetchCall: fetch(apiCall, {
        // Emulate XHR for Rails AJAX request checks
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        // fetch won’t send cookies in older browsers, unless you set the credentials init option.
        // We set to `same-origin` which is default value in modern browsers.
        // See https://github.com/whatwg/fetch/pull/585 for more information.
        credentials: 'same-origin'
      })
    };
  });
}
if (gl.startup_graphql_calls && window.fetch) {
  const headers = {"X-CSRF-Token":"x9Hl_7zv71sBog_EJxBvZY0-lpwPCfzMe8V_4U5fbYHGmzK76tAJZz_vt2LcPM2mX3nDYnpX4aRdny6dkgBmJQ","x-gitlab-feature-category":"source_code_management"};
  const url = `https://gitlab.com/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call => ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]>
</script>

<link rel="prefetch" href="/assets/webpack/monaco.9f9e3799.chunk.js">

<link rel="stylesheet" href="/assets/application-2f092db56dbf900e372c7f40059c05c8ef33425d35b3a01343a5c87efec14b5f.css" media="all" />
<link rel="stylesheet" href="/assets/page_bundles/tree-4d25647d03722854e14fe89644330ef783d9e6e79f75ae79c5755c11825ddfc8.css" media="all" /><link rel="stylesheet" href="/assets/page_bundles/projects-791e119ec1ea408a39e77566f01d5181ea6a33e9700a559c61d88cb179497f14.css" media="all" /><link rel="stylesheet" href="/assets/page_bundles/commit_description-b1dab9b10010cbb9c3738689b18ce46a4f58b98a8d483226fdff8a776a45caf0.css" media="all" />
<link rel="stylesheet" href="/assets/application_utilities-d42c923c5efe2cf5de15377a2e1842768a2dcc3908b27976b774553faf35d194.css" media="all" />
<link rel="stylesheet" href="/assets/tailwind-7a9a384add7f073714969b29692a668c5a75263950360bb5f211b4f019db7245.css" media="all" />


<link rel="stylesheet" href="/assets/fonts-fae5d3f79948bd85f18b6513a025f863b19636e85b09a1492907eb4b1bb0557b.css" media="all" />
<link rel="stylesheet" href="/assets/highlight/themes/white-e08c45a78f4446ec6c4226adb581d4482911bd7c85b47b7e7c003112b0c26274.css" media="all" />

<script src="/assets/webpack/runtime.06ccc8b5.bundle.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/main.4572b8e0.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/tracker.ccffc9f8.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/analytics.0da933ee.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script nonce="LZ24xD8IvXP1KEY7U+tvLQ==">
//<![CDATA[
window.snowplowOptions = {"namespace":"gl","hostname":"snowplow.trx.gitlab.net","cookieDomain":".gitlab.com","appId":"gitlab","formTracking":true,"linkClickTracking":true}

gl = window.gl || {};
gl.snowplowStandardContext = {"schema":"iglu:com.gitlab/gitlab_standard/jsonschema/1-0-10","data":{"environment":"production","source":"gitlab-rails","plan":"free","extra":{},"user_id":null,"is_gitlab_team_member":null,"namespace_id":61996112,"project_id":45627316,"feature_enabled_by_namespace_ids":null,"context_generated_at":"2024-05-19T21:30:13.534Z"}}
gl.snowplowPseudonymizedPageUrl = "https://gitlab.com/namespace61996112/project45627316/-/blob/:repository_path";


//]]>
</script>
<link rel="preload" href="/assets/application_utilities-d42c923c5efe2cf5de15377a2e1842768a2dcc3908b27976b774553faf35d194.css" as="style" type="text/css" nonce="J+1LkPcrNfHvzHLBxxiDyw==">
<link rel="preload" href="/assets/application-2f092db56dbf900e372c7f40059c05c8ef33425d35b3a01343a5c87efec14b5f.css" as="style" type="text/css" nonce="J+1LkPcrNfHvzHLBxxiDyw==">
<link rel="preload" href="/assets/highlight/themes/white-e08c45a78f4446ec6c4226adb581d4482911bd7c85b47b7e7c003112b0c26274.css" as="style" type="text/css" nonce="J+1LkPcrNfHvzHLBxxiDyw==">
<link crossorigin="" href="https://snowplow.trx.gitlab.net" rel="preconnect">
<link as="font" crossorigin="" href="/assets/gitlab-sans/GitLabSans-1e0a5107ea3bbd4be93e8ad2c503467e43166cd37e4293570b490e0812ede98b.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-sans/GitLabSans-Italic-38eaf1a569a54ab28c58b92a4a8de3afb96b6ebc250cf372003a7b38151848cc.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-08d2c5e8ff8fd3d2d6ec55bc7713380f8981c35f9d2df14e12b835464d6e8f23.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-Italic-38e58d8df29485a20c550da1d0111e2c2169f6dcbcf894f2cd3afbdd97bcc588.woff2" rel="preload">
<link rel="preload" href="/assets/fonts-fae5d3f79948bd85f18b6513a025f863b19636e85b09a1492907eb4b1bb0557b.css" as="style" type="text/css" nonce="J+1LkPcrNfHvzHLBxxiDyw==">



<script src="/assets/webpack/sentry.67d84f56.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>


<script src="/assets/webpack/commons-pages.groups.analytics.dashboards-pages.groups.analytics.dashboards.value_streams_dashboard--efdd0d8d.5c2d17d8.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/commons-pages.groups.new-pages.import.gitlab_projects.new-pages.import.manifest.new-pages.projects.n-44c6c18e.198bdb4b.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/commons-pages.search.show-super_sidebar.c2bf8995.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/super_sidebar.ad7fcfd7.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-a26344e2.9e486d4b.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/commons-pages.admin.runners.show-pages.clusters.agents.dashboard-pages.explore.catalog-pages.explore-48ba6f8c.65d4090f.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/commons-pages.groups.security.policies.edit-pages.groups.security.policies.new-pages.projects.blob.s-c8e0a3ae.bd521e94.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/111.e9037119.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/commons-pages.projects.artifacts.file-pages.projects.blob.show-pages.projects.show-pages.projects.sn-83d6e33b.136328e4.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-c684fcf6.f66fe4dc.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/136.34198558.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.49da613d.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.commits.show-pages.projects.compare.show.de7237da.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<script src="/assets/webpack/pages.projects.blob.show.ecbb118e.chunk.js" defer="defer" nonce="LZ24xD8IvXP1KEY7U+tvLQ=="></script>
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="tests/test_models/test_base_model.py · master · Hagos Mehari / AirBnB_clone · GitLab" property="og:title">
<meta content="AirBnB clone project part 1. The console" property="og:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.com/hkm2023/AirBnB_clone/-/blob/master/tests/test_models/test_base_model.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="tests/test_models/test_base_model.py · master · Hagos Mehari / AirBnB_clone · GitLab" property="twitter:title">
<meta content="AirBnB clone project part 1. The console" property="twitter:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="twitter:image">

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="G7GnRvfalgatfxq8_-SPbGapfrQVpRRSgfL4xdIayoUa-3ACoeVwOpMyohoEyC2vtO4rSmD7CTqnqKm5DkXBIQ" />
<meta name="csp-nonce" content="LZ24xD8IvXP1KEY7U+tvLQ==" />
<meta name="action-cable-url" content="/-/cable" />
<link href="/-/manifest.json" rel="manifest">
<link rel="icon" type="image/png" href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" id="favicon" data-original-href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png" />
<link href="/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">




<meta content="AirBnB clone project part 1. The console" name="description">
<meta content="#ececef" name="theme-color">
</head>

<body class="tab-width-8 gl-browser-generic gl-platform-other " data-find-file="/hkm2023/AirBnB_clone/-/find_file/master" data-namespace-id="61996112" data-page="projects:blob:show" data-page-type-id="master/tests/test_models/test_base_model.py" data-project="AirBnB_clone" data-project-full-path="hkm2023/AirBnB_clone" data-project-id="45627316">

<script nonce="LZ24xD8IvXP1KEY7U+tvLQ==">
//<![CDATA[
gl = window.gl || {};
gl.client = {"isGeneric":true,"isOther":true};


//]]>
</script>


<header class="header-logged-out" data-testid="navbar">
<a class="gl-sr-only gl-accessibility" href="#content-body">Skip to content</a>
<div class="container-fluid">
<nav aria-label="Explore GitLab" class="header-logged-out-nav gl-display-flex gl-gap-3 gl-justify-content-space-between">
<div class="gl-display-flex gl-align-items-center gl-gap-1">
<span class="gl-sr-only">GitLab</span>
<a title="Homepage" id="logo" class="header-logged-out-logo has-tooltip" aria-label="Homepage" data-track-label="main_navigation" data-track-action="click_gitlab_logo_link" data-track-property="navigation_top" href="/"><svg aria-hidden="true" role="img" class="tanuki-logo" width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path class="tanuki-shape tanuki" d="m24.507 9.5-.034-.09L21.082.562a.896.896 0 0 0-1.694.091l-2.29 7.01H7.825L5.535.653a.898.898 0 0 0-1.694-.09L.451 9.411.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 2.56 1.935 1.554 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z"
        fill="#E24329"/>
  <path class="tanuki-shape right-cheek" d="m24.507 9.5-.034-.09a11.44 11.44 0 0 0-4.56 2.051l-7.447 5.632 4.742 3.584 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z"
        fill="#FC6D26"/>
  <path class="tanuki-shape chin" d="m7.707 20.677 2.56 1.935 1.555 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935-4.743-3.584-4.755 3.584Z"
        fill="#FCA326"/>
  <path class="tanuki-shape left-cheek" d="M5.01 11.461a11.43 11.43 0 0 0-4.56-2.05L.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 4.745-3.584-7.444-5.632Z"
        fill="#FC6D26"/>
</svg>

</a></div>
<ul class="gl-list-none gl-p-0 gl-m-0 gl-display-flex gl-gap-3 gl-align-items-center gl-flex-grow-1">
<li class="header-logged-out-nav-item header-logged-out-dropdown gl-md-display-none">
<button class="header-logged-out-toggle" data-toggle="dropdown" type="button">
<span class="gl-sr-only">
Menu
</span>
<svg class="s16" data-testid="hamburger-icon"><use href="/assets/icons-0b41337f52be73f7bbf9d59b841eb98a6e790dfa1a844644f120a80ce3cc18ba.svg#hamburger"></use></svg>
</button>
<div class="dropdown-menu">
<ul>
<li>
<a href="https://about.gitlab.com/why-gitlab">Why GitLab
</a></li>
<li>
<a href="https://about.gitlab.com/pricing">Pricing
</a></li>
<li>
<a href="https://about.gitlab.com/sales">Contact Sales
</a></li>
<li>
<a href="/explore">Explore</a>
</li>
</ul>
</div>
</li>
<li class="header-logged-out-nav-item gl-display-none gl-md-display-inline-block">
<a href="https://about.gitlab.com/why-gitlab">Why GitLab
</a></li>
<li class="header-logged-out-nav-item gl-display-none gl-md-display-inline-block">
<a href="https://about.gitlab.com/pricing">Pricing
</a></li>
<li class="header-logged-out-nav-item gl-display-none gl-md-display-inline-block">
<a href="https://about.gitlab.com/sales">Contact Sales
</a></li>
<li class="header-logged-out-nav-item gl-display-none gl-md-display-inline-block">
<a class="" href="/explore">Explore</a>
</li>
</ul>
<ul class="gl-list-none gl-p-0 gl-m-0 gl-display-flex gl-gap-3 gl-align-items-center gl-justify-content-end">
<li class="header-logged-out-nav-item">
<a href="/users/sign_in?redirect_to_referer=yes">Sign in</a>
</li>
<li class="header-logged-out-nav-item">
<a class="gl-button btn btn-md btn-confirm " href="/users/sign_up"><span class="gl-button-text">
Get free trial

</span>

</a></li>
</ul>
</nav>
</div>
</header>

<div class="layout-page page-with-super-sidebar">
<aside class="js-super-sidebar super-sidebar super-sidebar-loading" data-command-palette="{&quot;project_files_url&quot;:&quot;/hkm2023/AirBnB_clone/-/files/master?format=json&quot;,&quot;project_blob_url&quot;:&quot;/hkm2023/AirBnB_clone/-/blob/master&quot;}" data-force-desktop-expanded-sidebar="" data-root-path="/" data-sidebar="{&quot;is_logged_in&quot;:false,&quot;context_switcher_links&quot;:[{&quot;title&quot;:&quot;Explore&quot;,&quot;link&quot;:&quot;/explore&quot;,&quot;icon&quot;:&quot;compass&quot;}],&quot;current_menu_items&quot;:[{&quot;id&quot;:&quot;project_overview&quot;,&quot;title&quot;:&quot;AirBnB_clone&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:45627316,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-project&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;manage_menu&quot;,&quot;title&quot;:&quot;Manage&quot;,&quot;icon&quot;:&quot;users&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/activity&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;activity&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/activity&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-project-activity&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;members&quot;,&quot;title&quot;:&quot;Members&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/project_members&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;labels&quot;,&quot;title&quot;:&quot;Labels&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/labels&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;plan_menu&quot;,&quot;title&quot;:&quot;Plan&quot;,&quot;icon&quot;:&quot;planning&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/issues&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;project_issue_list&quot;,&quot;title&quot;:&quot;Issues&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/issues&quot;,&quot;pill_count&quot;:&quot;0&quot;,&quot;link_classes&quot;:&quot;shortcuts-issues has-sub-items&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;boards&quot;,&quot;title&quot;:&quot;Issue boards&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/boards&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-issue-boards&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;milestones&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/milestones&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_wiki&quot;,&quot;title&quot;:&quot;Wiki&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/wikis/home&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-wiki&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;code_menu&quot;,&quot;title&quot;:&quot;Code&quot;,&quot;icon&quot;:&quot;code&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/merge_requests&quot;,&quot;is_active&quot;:true,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;project_merge_request_list&quot;,&quot;title&quot;:&quot;Merge requests&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/merge_requests&quot;,&quot;pill_count&quot;:&quot;0&quot;,&quot;link_classes&quot;:&quot;shortcuts-merge_requests&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;files&quot;,&quot;title&quot;:&quot;Repository&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/tree/master&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-tree&quot;,&quot;is_active&quot;:true},{&quot;id&quot;:&quot;branches&quot;,&quot;title&quot;:&quot;Branches&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/branches&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;commits&quot;,&quot;title&quot;:&quot;Commits&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/commits/master?ref_type=heads&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-commits&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;tags&quot;,&quot;title&quot;:&quot;Tags&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/tags&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;graphs&quot;,&quot;title&quot;:&quot;Repository graph&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/network/master?ref_type=heads&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-network&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;compare&quot;,&quot;title&quot;:&quot;Compare revisions&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/compare?from=master\u0026to=master&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_snippets&quot;,&quot;title&quot;:&quot;Snippets&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/snippets&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-snippets&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;build_menu&quot;,&quot;title&quot;:&quot;Build&quot;,&quot;icon&quot;:&quot;rocket&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/pipelines&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;pipelines&quot;,&quot;title&quot;:&quot;Pipelines&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/pipelines&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-pipelines&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;jobs&quot;,&quot;title&quot;:&quot;Jobs&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/jobs&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;pipeline_schedules&quot;,&quot;title&quot;:&quot;Pipeline schedules&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/pipeline_schedules&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;artifacts&quot;,&quot;title&quot;:&quot;Artifacts&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/artifacts&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;deploy_menu&quot;,&quot;title&quot;:&quot;Deploy&quot;,&quot;icon&quot;:&quot;deployments&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/releases&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;releases&quot;,&quot;title&quot;:&quot;Releases&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/releases&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-deployments-releases&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;packages_registry&quot;,&quot;title&quot;:&quot;Package Registry&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/packages&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-container-registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;container_registry&quot;,&quot;title&quot;:&quot;Container Registry&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/container_registry&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_registry&quot;,&quot;title&quot;:&quot;Model registry&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/ml/models&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;operations_menu&quot;,&quot;title&quot;:&quot;Operate&quot;,&quot;icon&quot;:&quot;cloud-pod&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/environments&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;environments&quot;,&quot;title&quot;:&quot;Environments&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/environments&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-environments&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;infrastructure_registry&quot;,&quot;title&quot;:&quot;Terraform modules&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/terraform_module_registry&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;monitor_menu&quot;,&quot;title&quot;:&quot;Monitor&quot;,&quot;icon&quot;:&quot;monitor&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/incidents&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;incidents&quot;,&quot;title&quot;:&quot;Incidents&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/incidents&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;service_desk&quot;,&quot;title&quot;:&quot;Service Desk&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/issues/service_desk&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;analyze_menu&quot;,&quot;title&quot;:&quot;Analyze&quot;,&quot;icon&quot;:&quot;chart&quot;,&quot;avatar&quot;:null,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/value_stream_analytics&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;cycle_analytics&quot;,&quot;title&quot;:&quot;Value stream analytics&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/value_stream_analytics&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-project-cycle-analytics&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;contributors&quot;,&quot;title&quot;:&quot;Contributor analytics&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/graphs/master?ref_type=heads&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;ci_cd_analytics&quot;,&quot;title&quot;:&quot;CI/CD analytics&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/pipelines/charts&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;repository_analytics&quot;,&quot;title&quot;:&quot;Repository analytics&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/graphs/master/charts&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-repository-charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_experiments&quot;,&quot;title&quot;:&quot;Model experiments&quot;,&quot;icon&quot;:null,&quot;avatar&quot;:null,&quot;entity_id&quot;:null,&quot;link&quot;:&quot;/hkm2023/AirBnB_clone/-/ml/experiments&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false}],&quot;current_context_header&quot;:&quot;Project&quot;,&quot;support_path&quot;:&quot;https://about.gitlab.com/get-help/&quot;,&quot;docs_path&quot;:&quot;/help/docs&quot;,&quot;display_whats_new&quot;:true,&quot;whats_new_most_recent_release_items_count&quot;:8,&quot;whats_new_version_digest&quot;:&quot;2b7120854845b6c57c51713a6f7a1efa9f7577a9dc84c00e2224b505a8eddae7&quot;,&quot;show_version_check&quot;:null,&quot;gitlab_version&quot;:{&quot;major&quot;:17,&quot;minor&quot;:1,&quot;patch&quot;:0,&quot;suffix_s&quot;:&quot;&quot;},&quot;gitlab_version_check&quot;:null,&quot;search&quot;:{&quot;search_path&quot;:&quot;/search&quot;,&quot;issues_path&quot;:&quot;/dashboard/issues&quot;,&quot;mr_path&quot;:&quot;/dashboard/merge_requests&quot;,&quot;autocomplete_path&quot;:&quot;/search/autocomplete&quot;,&quot;search_context&quot;:{&quot;project&quot;:{&quot;id&quot;:45627316,&quot;name&quot;:&quot;AirBnB_clone&quot;},&quot;project_metadata&quot;:{&quot;mr_path&quot;:&quot;/hkm2023/AirBnB_clone/-/merge_requests&quot;,&quot;issues_path&quot;:&quot;/hkm2023/AirBnB_clone/-/issues&quot;},&quot;code_search&quot;:true,&quot;ref&quot;:&quot;master&quot;,&quot;scope&quot;:null,&quot;for_snippets&quot;:null}},&quot;panel_type&quot;:&quot;project&quot;,&quot;shortcut_links&quot;:[{&quot;title&quot;:&quot;Snippets&quot;,&quot;href&quot;:&quot;/explore/snippets&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-snippets&quot;},{&quot;title&quot;:&quot;Groups&quot;,&quot;href&quot;:&quot;/explore/groups&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-groups&quot;},{&quot;title&quot;:&quot;Projects&quot;,&quot;href&quot;:&quot;/explore/projects/starred&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-projects&quot;}]}"></aside>

<div class="content-wrapper">
<div class="mobile-overlay"></div>

<div class="alert-wrapper gl-force-block-formatting-context">





























<div class="top-bar-fixed container-fluid" data-testid="top-bar">
<div class="top-bar-container gl-display-flex gl-align-items-center gl-gap-2">
<button class="gl-button btn btn-icon btn-md btn-default btn-default-tertiary js-super-sidebar-toggle-expand super-sidebar-toggle gl-ml-n3" aria-controls="super-sidebar" aria-expanded="false" aria-label="Primary navigation sidebar" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="sidebar-icon"><use href="/assets/icons-0b41337f52be73f7bbf9d59b841eb98a6e790dfa1a844644f120a80ce3cc18ba.svg#sidebar"></use></svg>

</button>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Hagos Mehari","item":"https://gitlab.com/hkm2023"},{"@type":"ListItem","position":2,"name":"AirBnB_clone","item":"https://gitlab.com/hkm2023/AirBnB_clone"},{"@type":"ListItem","position":3,"name":"Repository","item":"https://gitlab.com/hkm2023/AirBnB_clone/-/blob/master/tests/test_models/test_base_model.py"}]}


</script>
<nav aria-label="Breadcrumbs" class="breadcrumbs gl-breadcrumbs tmp-breadcrumbs-fix" data-testid="breadcrumb-links">
<ul class="breadcrumb gl-breadcrumb-list js-breadcrumbs-list gl-flex-grow-1">
<li class="gl-breadcrumb-item gl-display-inline-flex"><a href="/hkm2023">Hagos Mehari</a></li> <li class="gl-breadcrumb-item gl-display-inline-flex"><a class="gl-display-inline-flex!" href="/hkm2023/AirBnB_clone"><span class="js-breadcrumb-item-text">AirBnB_clone</span></a></li>

<li class="gl-breadcrumb-item" data-testid="breadcrumb-current-link">
<a href="/hkm2023/AirBnB_clone/-/blob/master/tests/test_models/test_base_model.py">Repository</a>
</li>
</ul>
</nav>



</div>
</div>

</div>
<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-testid="flash-container">
<div id="js-global-alerts"></div>
</div>






<div class="js-signature-container" data-signatures-path="/hkm2023/AirBnB_clone/-/commits/d3cea8b1539ff4c9a3851ba8883b9958ddc2f4b4/signatures?limit=1"></div>

<div class="tree-holder gl-pt-4" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder gl-max-w-26">
<div data-project-id="45627316" data-project-root-path="/hkm2023/AirBnB_clone" data-ref="master" data-ref-type="" id="js-tree-ref-switcher"></div>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/hkm2023/AirBnB_clone/-/tree/master">AirBnB_clone
</a></li>
<li class="breadcrumb-item">
<a href="/hkm2023/AirBnB_clone/-/tree/master/tests">tests</a>
</li>
<li class="breadcrumb-item">
<a href="/hkm2023/AirBnB_clone/-/tree/master/tests/test_models">test_models</a>
</li>
<li class="breadcrumb-item">
<a href="/hkm2023/AirBnB_clone/-/blob/master/tests/test_models/test_base_model.py"><strong>test_base_model.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-display-flex gl-flex-wrap gl-sm-flex-nowrap gl-align-items-baseline gl-gap-3">
<button class="gl-button btn btn-md btn-default has-tooltip shortcuts-find-file" title="Go to file, press &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;/~&lt;/kbd&gt; or &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;t&lt;/kbd&gt;" aria-keyshortcuts="/+~ t" data-html="true" type="button"><span class="gl-button-text">
Find file

</span>

</button>
<a data-event-tracking="click_blame_control_on_blob_page" class="gl-button btn btn-md btn-default js-blob-blame-link" href="/hkm2023/AirBnB_clone/-/blame/master/tests/test_models/test_base_model.py"><span class="gl-button-text">
Blame
</span>

</a>
<a data-event-tracking="click_history_control_on_blob_page" class="gl-button btn btn-md btn-default " href="/hkm2023/AirBnB_clone/-/commits/master/tests/test_models/test_base_model.py"><span class="gl-button-text">
History
</span>

</a>
<a aria-keyshortcuts="y" class="gl-button btn btn-md btn-default has-tooltip js-data-file-blob-permalink-url" data-html="true" title="Go to permalink &lt;kbd class=&#39;flat ml-1&#39; aria-hidden=true&gt;y&lt;/kbd&gt;" href="/hkm2023/AirBnB_clone/-/blob/a7474258155bc4a16c8ff4f553a19d74bd224106/tests/test_models/test_base_model.py"><span class="gl-button-text">
Permalink
</span>

</a>
</div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-d3cea8b1">
<div class="avatar-cell d-none d-sm-block">
<a href="mailto:user%20email"><img alt="user name&#39;s avatar" src="https://secure.gravatar.com/avatar/892de6c8f66ecc21aa119e25b6b0a1d921e9d2047da3727ad48bf271c1f2a0b1?s=80&amp;d=identicon" class="avatar s40 gl-display-none gl-sm-display-inline-block" title="user name"></a>
</div>
<div class="commit-detail flex-list gl-display-flex gl-justify-content-space-between gl-align-items-center gl-flex-grow-1 gl-min-w-0">
<div class="commit-content" data-testid="commit-content">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/hkm2023/AirBnB_clone/-/commit/d3cea8b1539ff4c9a3851ba8883b9958ddc2f4b4">Update tests for base models and the console</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
d3cea8b1
</span>
<div class="committer">
<a class="commit-author-link" href="mailto:user%20email">user name</a> authored <time class="js-timeago" title="Mar 10, 2023 3:42pm" datetime="2023-03-10T15:42:28Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Mar 10, 2023</time>
</div>

</div>
<div class="commit-actions flex-row">

<div class="js-commit-pipeline-status" data-endpoint="/hkm2023/AirBnB_clone/-/commit/d3cea8b1539ff4c9a3851ba8883b9958ddc2f4b4/pipelines?ref=master"></div>
<div class="commit-sha-group btn-group d-none d-sm-flex">
<div class="label label-monospace monospace">
d3cea8b1
</div>
<button class="gl-button btn btn-icon btn-md btn-default " title="Copy commit SHA" aria-label="Copy commit SHA" aria-live="polite" data-toggle="tooltip" data-placement="bottom" data-container="body" data-html="true" data-category="primary" data-size="medium" data-clipboard-text="d3cea8b1539ff4c9a3851ba8883b9958ddc2f4b4" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="copy-to-clipboard-icon"><use href="/assets/icons-0b41337f52be73f7bbf9d59b841eb98a6e790dfa1a844644f120a80ce3cc18ba.svg#copy-to-clipboard"></use></svg>

</button>

</div>
</div>
</div>
</li>

</ul>
</div>

</div>
<div class="blob-content-holder js-per-page" data-blame-per-page="1000" id="blob-content-holder">
<div data-blob-path="tests/test_models/test_base_model.py" data-can-download-code="true" data-explain-code-available="false" data-new-workspace-path="/-/remote_development/workspaces/new" data-original-branch="master" data-project-path="hkm2023/AirBnB_clone" data-ref-type="" data-resource-id="gid://gitlab/Project/45627316" data-target-branch="master" data-user-id="" id="js-view-blob-app">
<div class="gl-spinner-container" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div>
</div>
</div>

</div>
<script nonce="LZ24xD8IvXP1KEY7U+tvLQ==">
//<![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/-/ide/project/hkm2023/AirBnB_clone/edit/master/-/tests/test_models/test_base_model.py'


//]]>
</script>
<div data-ambiguous="false" data-ref="master" id="js-ambiguous-ref-modal"></div>

</main>
</div>


</div>
</div>


<script nonce="LZ24xD8IvXP1KEY7U+tvLQ==">
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded');
    img.dataset.testid = 'js-lazy-loaded-content';
  });
}

//]]>
</script>
<script nonce="LZ24xD8IvXP1KEY7U+tvLQ==">
//<![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]>
</script>

</body>
</html>

