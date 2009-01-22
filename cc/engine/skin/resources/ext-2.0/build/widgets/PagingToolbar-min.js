/*
 * Ext JS Library 2.0
 * Copyright(c) 2006-2007, Ext JS, LLC.
 * licensing@extjs.com
 * 
 * http://extjs.com/license
 */

Ext.PagingToolbar=Ext.extend(Ext.Toolbar,{pageSize:20,displayMsg:"Displaying {0} - {1} of {2}",emptyMsg:"No data to display",beforePageText:"Page",afterPageText:"of {0}",firstText:"First Page",prevText:"Previous Page",nextText:"Next Page",lastText:"Last Page",refreshText:"Refresh",paramNames:{start:"start",limit:"limit"},initComponent:function(){Ext.PagingToolbar.superclass.initComponent.call(this);this.cursor=0;this.bind(this.store)},onRender:function(B,A){Ext.PagingToolbar.superclass.onRender.call(this,B,A);this.first=this.addButton({tooltip:this.firstText,iconCls:"x-tbar-page-first",disabled:true,handler:this.onClick.createDelegate(this,["first"])});this.prev=this.addButton({tooltip:this.prevText,iconCls:"x-tbar-page-prev",disabled:true,handler:this.onClick.createDelegate(this,["prev"])});this.addSeparator();this.add(this.beforePageText);this.field=Ext.get(this.addDom({tag:"input",type:"text",size:"3",value:"1",cls:"x-tbar-page-number"}).el);this.field.on("keydown",this.onPagingKeydown,this);this.field.on("focus",function(){this.dom.select()});this.afterTextEl=this.addText(String.format(this.afterPageText,1));this.field.setHeight(18);this.addSeparator();this.next=this.addButton({tooltip:this.nextText,iconCls:"x-tbar-page-next",disabled:true,handler:this.onClick.createDelegate(this,["next"])});this.last=this.addButton({tooltip:this.lastText,iconCls:"x-tbar-page-last",disabled:true,handler:this.onClick.createDelegate(this,["last"])});this.addSeparator();this.loading=this.addButton({tooltip:this.refreshText,iconCls:"x-tbar-loading",handler:this.onClick.createDelegate(this,["refresh"])});if(this.displayInfo){this.displayEl=Ext.fly(this.el.dom).createChild({cls:"x-paging-info"})}if(this.dsLoaded){this.onLoad.apply(this,this.dsLoaded)}},updateInfo:function(){if(this.displayEl){var A=this.store.getCount();var B=A==0?this.emptyMsg:String.format(this.displayMsg,this.cursor+1,this.cursor+A,this.store.getTotalCount());this.displayEl.update(B)}},onLoad:function(A,C,F){if(!this.rendered){this.dsLoaded=[A,C,F];return }this.cursor=F.params?F.params[this.paramNames.start]:0;var E=this.getPageData(),B=E.activePage,D=E.pages;this.afterTextEl.el.innerHTML=String.format(this.afterPageText,E.pages);this.field.dom.value=B;this.first.setDisabled(B==1);this.prev.setDisabled(B==1);this.next.setDisabled(B==D);this.last.setDisabled(B==D);this.loading.enable();this.updateInfo()},getPageData:function(){var A=this.store.getTotalCount();return{total:A,activePage:Math.ceil((this.cursor+this.pageSize)/this.pageSize),pages:A<this.pageSize?1:Math.ceil(A/this.pageSize)}},onLoadError:function(){if(!this.rendered){return }this.loading.enable()},readPage:function(C){var A=this.field.dom.value,B;if(!A||isNaN(B=parseInt(A,10))){this.field.dom.value=C.activePage;return false}return B},onPagingKeydown:function(D){var B=D.getKey(),E=this.getPageData(),C;if(B==D.RETURN){D.stopEvent();if(C=this.readPage(E)){C=Math.min(Math.max(1,C),E.pages)-1;this.doLoad(C*this.pageSize)}}else{if(B==D.HOME||B==D.END){D.stopEvent();C=B==D.HOME?1:E.pages;this.field.dom.value=C}else{if(B==D.UP||B==D.PAGEUP||B==D.DOWN||B==D.PAGEDOWN){D.stopEvent();if(C=this.readPage(E)){var A=D.shiftKey?10:1;if(B==D.DOWN||B==D.PAGEDOWN){A*=-1}C+=A;if(C>=1&C<=E.pages){this.field.dom.value=C}}}}}},beforeLoad:function(){if(this.rendered&&this.loading){this.loading.disable()}},doLoad:function(C){var B={},A=this.paramNames;B[A.start]=C;B[A.limit]=this.pageSize;this.store.load({params:B})},onClick:function(E){var B=this.store;switch(E){case"first":this.doLoad(0);break;case"prev":this.doLoad(Math.max(0,this.cursor-this.pageSize));break;case"next":this.doLoad(this.cursor+this.pageSize);break;case"last":var D=B.getTotalCount();var A=D%this.pageSize;var C=A?(D-A):D-this.pageSize;this.doLoad(C);break;case"refresh":this.doLoad(this.cursor);break}},unbind:function(A){A=Ext.StoreMgr.lookup(A);A.un("beforeload",this.beforeLoad,this);A.un("load",this.onLoad,this);A.un("loadexception",this.onLoadError,this);this.store=undefined},bind:function(A){A=Ext.StoreMgr.lookup(A);A.on("beforeload",this.beforeLoad,this);A.on("load",this.onLoad,this);A.on("loadexception",this.onLoadError,this);this.store=A}});Ext.reg("paging",Ext.PagingToolbar);