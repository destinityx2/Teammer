/*
 * jQuery liCover v 2.2
 *
 * Copyright 2012, Linnik Yura | LI MASS CODE | http://masscode.ru
 * http://masscode.ru/index.php/k2/item/45-lifullsize
 * Free to use
 * 
 * last update 17.04.2014
 *
 * BUGFIX:
 * 17.04.14 Коррекция размеров min и max
 * 17.04.14 Исправлен баг с определением родительского блока
 */

(function ($) {
	var methods = {
		init: function (options) {
			var p = {
				parent: $(window),
				position:'absolute',	//'absolute' or 'fixed'
				veticalAlign:'middle',	//'top','bottom' or 'middle' - default
				align:'center'			//'left','right' or 'center' - default
			};
			if (options) {
				$.extend(p, options);
			}
			return this.each(function () {
				var positionEl;
				if(p.position == 'absolute' || p.position == 'fixed'){
					positionEl = p.position;	
				}else{
					positionEl = 'absolute';	
				}
				var 
				elWrap = $('<div>').addClass('fullsizeWrap').css({left:'0',top:'0',width:'100%',height:'100%',overflow:'hidden',position:positionEl}),
				el = $(this).css({position:'absolute',maxWidth:'none',minWidth:0,maxHeight:'none',minHeight:0}).wrap(elWrap),
				parent = el.closest(p.parent).addClass('coverParent');
				if($.isWindow(p.parent[0])){
					parent = $(window)
				}
					
				var
				elClone = el.clone().removeAttr('class').removeAttr('width').removeAttr('height').css({left:'-9999px',top:'-9999px'}).appendTo('body'),
				elCloneW = elClone.width(),
				elCloneH = elClone.height(),
				wW = parent.width(),
				wH = parent.height(),
				elFactor = elCloneW / elCloneH,
				wFactor = wW/wH;
				
				var fullSizeFunc = function(){
					if(elFactor < wFactor){
						
						
						
						var 
						elH = wW / elFactor,
						elTop = (elH - wH) / 2;
						el.css({width:wW,height:elH, top:-elTop, left:'0'});
					}else{
						
						
						
						var 
						elW = wH * elFactor,
						elLeft = (elW - wW) / 2;
						el.css({height:wH,width:elW, left:-elLeft, top:'0'});	
					}
					
					if(p.veticalAlign == 'top'){
						el.css({top:0,bottom:'auto'})	
					}
					if(p.veticalAlign == 'bottom'){
						el.css({top:'auto',bottom:'0'})	
					}
					if(p.align == 'left'){
						el.css({right:'auto',left:'0'})		
					}
					if(p.align == 'right'){
						el.css({left:'auto',right:'0'})		
					}
					
				};
				elClone.remove();
				fullSizeFunc();
				el.fadeTo(500,1)
				$(window).on('resize redraw',function(){
					wW = parent.width();
					wH = parent.height();
					wFactor = wW/wH;
					fullSizeFunc();
				});
				
			});
		}
	};
	$.fn.liCover = function (method) {
		if (methods[method]) {
			return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		} else if (typeof method === 'object' || !method) {
			return methods.init.apply(this, arguments);
		} else {
			$.error('Метод ' + method + ' в jQuery.liCover не существует');
		}
	};
})(jQuery);