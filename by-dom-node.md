## By DOM Node

```
div#main

div#main > div#jp-top-panel
div#main > div#jp-top-panel > div#jp-MainLogo
div#main > div#jp-top-panel > div#jp-menu-panel > div#jp-MainMenu > ul[role="menubar"]

div#main > div#jp-main-content-panel
div#main > div#jp-main-content-panel > div[aria-label="main sidebar"] > ul[aria-label="main sidebar"]
div#main > div#jp-main-content-panel > div#jp-main-vsplit-panel > div#jp-main-split-panel > div#jp-left-stack
div#main > div#jp-main-content-panel > div#jp-main-vsplit-panel > div#jp-main-split-panel > div#jp-main-dock-panel
div#main > div#jp-main-content-panel > div#jp-main-vsplit-panel > div#jp-main-split-panel > div#jp-right-stack
div#main > div#jp-main-content-panel > div#jp-main-vsplit-panel > div#jp-down-stack
div#main > div#jp-main-content-panel > div[aria-label="alternate sidebar"]
div#main > div#jp-main-content-panel > div[aria-label="alternate sidebar"] > ul[aria-label="alternate-sidebar"]

div#main > div#jp-bottom-panel
div#main > div#jp-bottom-panel > div#jp-main-statusbar

div#modal-command-palette
div#modal-command-palette > div#command-palette
div#modal-command-palette > div#command-palette > div.lm-CommandPalette-search
div#modal-command-palette > div#command-palette > div.lm-CommandPalette-content
```

### Shell

Id #main

```html
<div class="lm-Widget p-Widget jp-LabShell" id="main" data-direction="top-to-bottom" data-alignment="start" data-shell-mode="multiple-document" style="min-width: 450px; min-height: 217px;">
```

#### Top area

Id #jp-top-panel
    topHandler.panel.id = 'jp-top-panel';

```html
<div class="lm-Widget p-Widget lm-Panel p-Panel" role="banner" id="jp-top-panel" style="position: absolute; top: 0px; left: 0px; width: 897px; height: 28px;">
```

##### Logo

Id #jp-MainLogo

##### Menu panel

Id #jp-menu-panel

###### Menu bar

Id #jp-MainMenu

Within this you have a `ul[role="menubar"]` with `li[role="menuitem"]`. When you click a menu item, it opens a:

    div#jp-mainmenu-* > ul[role="menu"] > li[role="menuitem"]

as a direct child node of the shell node (div#main).

#### Main content panel

Id #jp-main-content-panel
    hboxPanel.id = 'jp-main-content-panel';

    vsplitPanel.addWidget(hsplitPanel);
    vsplitPanel.addWidget(downPanel);

    hboxPanel.addWidget(leftHandler.sideBar);
    hboxPanel.addWidget(vsplitPanel);
    hboxPanel.addWidget(rightHandler.sideBar);

```html
<div class="lm-Widget p-Widget lm-Panel p-Panel lm-BoxPanel p-BoxPanel" data-direction="left-to-right" data-alignment="start" id="jp-main-content-panel" style="position: absolute; top: 28px; left: 0px; width: 897px; height: 904px; min-width: 450px; min-height: 165px;">
```

##### Left sidebar

class .jp-mod-left

aria-label="main sidebar"

    leftHandler.sideBar.addClass('jp-mod-left');
    leftHandler.sideBar.node.setAttribute(
      'aria-label',
      trans.__('main sidebar')
    );

```html
<div class="lm-Widget p-Widget lm-TabBar p-TabBar jp-SideBar jp-mod-left lm-BoxPanel-child p-BoxPanel-child" data-orientation="vertical" aria-label="main sidebar" role="complementary" style="position: absolute; top: 0px; left: 0px; width: 33px; height: 904px;">
```

##### Main vertically split panel

Id #jp-main-vsplit-panel

```html
<div class="lm-Widget p-Widget lm-Panel p-Panel lm-SplitPanel p-SplitPanel lm-BoxPanel-child p-BoxPanel-child" data-orientation="vertical" data-alignment="start" id="jp-main-vsplit-panel" style="position: absolute; top: 0px; left: 33px; width: 831px; height: 904px; min-width: 384px; min-height: 165px;">
```

###### Main horizontally split panel

Id #jp-main-split-panel

####### Left stack

Id #jp-left-stack

####### Main dock panel

Id #jp-main-dock-panel

Underneath this node, tab bars are div.lm-DockPanel-tabBar and content panels are div.lm-DockPanel-widget, whose visibility get toggled with .lm-mod-hidden

Underneath a notebook, we have:

    div[role=navigation][aria-label="notebook actions"]
    div[role=region][aria-label="notebook content"]


####### Right stack

Id #jp-right-stack

###### Down stack

Id #jp-down-stack

This is where the Log Console is shown. Underneath this node you have two nodes: a Lumino tab bar and panel.

##### Right sidebar

class .jp-mod-right

    rightHandler.sideBar.addClass('jp-mod-right');
    rightHandler.sideBar.node.setAttribute(
      'aria-label',
      trans.__('alternate sidebar')
    );

```html
<div class="lm-Widget p-Widget lm-TabBar p-TabBar jp-SideBar jp-mod-right lm-BoxPanel-child p-BoxPanel-child" data-orientation="vertical" aria-label="alternate sidebar" role="complementary" style="position: absolute; top: 0px; left: 864px; width: 33px; height: 904px;">
```

#### Bottom area

Id #jp-bottom-panel
    bottomPanel.id = 'jp-bottom-panel';

```html
<div class="lm-Widget p-Widget lm-Panel p-Panel lm-BoxPanel p-BoxPanel" data-direction="bottom-to-top" data-alignment="start" role="contentinfo" id="jp-bottom-panel" style="position: absolute; top: 932px; left: 0px; width: 897px; height: 24px; min-width: 0px; min-height: 24px;">
```

##### Status bar

Id #jp-main-statusbar

```html
<div class="lm-Widget p-Widget f14byud0 lm-BoxPanel-child p-BoxPanel-child" id="jp-main-statusbar" style="position: absolute; top: 0px; left: 0px; width: 897px; height: 24px;">
```

###### Status bar left panel

No id, no specific class or aria attribute

####### Document mode toggle

Id #jp-single-document-mode

```html
<div class="lm-Widget p-Widget fk1s8g9" id="jp-single-document-mode">
```

### Command Palette

Id #modal-command-palette

```html
<div class="lm-Widget p-Widget lm-Panel p-Panel jp-ModalCommandPalette lm-mod-hidden p-mod-hidden" id="modal-command-palette" tabindex="0" aria-hidden="true">
```
