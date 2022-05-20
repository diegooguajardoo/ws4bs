(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');ga('create','UA-59970935-1','auto');ga('send','pageview');$(document).ready(function(){$('.onlyAlpha').on('keypress',function(event){var regex=new RegExp("^[a-zA-Z ñÑ]+$");var key=String.fromCharCode(!event.charCode?event.which:event.charCode);if(!regex.test(key)){event.preventDefault();return false;}});$(".onlyNumber").on('keypress',function(event){var regex=new RegExp("^[0-9]+$");var key=String.fromCharCode(!event.charCode?event.which:event.charCode);if(!regex.test(key)){event.preventDefault();return false;}});$(".onlyNumber").on('change',function(){if(isNaN(parseInt($(this).val()))){$(this).val("");}else{$(this).val(parseInt($(this).val()));}});$(".onlyAlpha_Num").on('keypress',function(event){var regex=new RegExp("^[a-zA-Z0-9 ñÑ]+$");var key=String.fromCharCode(!event.charCode?event.which:event.charCode);if(!regex.test(key)){event.preventDefault();return false;}});});function deleteCookie(cookieName){var date=new Date();date.setTime(date.getTime()-(1*24*60*60*1000));var expires="; expires="+date.toGMTString();document.cookie=cookieName+"="+""+expires+"; path=/";}
function GetCookie(prmCookieName){var CookieName=prmCookieName+"=";var i=0;while(i<document.cookie.length){var j=i+CookieName.length;if(document.cookie.substring(i,j)==CookieName){var leng=document.cookie.indexOf(";",j);if(leng==-1)leng=document.cookie.length;return unescape(document.cookie.substring(j,leng));}
i=document.cookie.indexOf(" ",i)+1;if(i==0)break;}
return"*";}
function parseCookie(cookieValue,index){if(cookieValue==null)return""
if(cookieValue=="*")return""
var arCookie=new Array();arCookie=cookieValue.split("`");return arCookie[index];}
function excPgm(pgm,html,formS,param,targ){if(pgm==""){return false;}
if(html==""||html==undefined){html=pgm;}
pgm=pgm+".pgm";if(param!==""&&param!==undefined){pgm=pgm+"?"+param;}
$("#frmTemporalExcPgm").remove();$('body').append('<form id="frmTemporalExcPgm" name="frmTemporalExcPgm" method="post"></form>');$("#frmTemporalExcPgm").append("<input type='hidden' name='app_h' value='"+parseCookie(GetCookie(TheCookieName),01)+"'>");$("#frmTemporalExcPgm").append("<input type='hidden' name='mod_h' value='"+parseCookie(GetCookie(TheCookieName),02)+"'>");$("#frmTemporalExcPgm").append("<input type='hidden' name='per_h' value='"+parseCookie(GetCookie(TheCookieName),03)+"'>");$("#frmTemporalExcPgm").append("<input type='hidden' name='ses_h' value='"+parseCookie(GetCookie(TheCookieName),04)+"'>");$("#frmTemporalExcPgm").append("<input type='hidden' name='cta_h' value='"+parseCookie(GetCookie(TheCookieName),05)+"'>");$("#frmTemporalExcPgm").append("<input type='hidden' name='usu_h' value='"+parseCookie(GetCookie(TheCookieName),06)+"'>");$("#frmTemporalExcPgm").append("<input type='hidden' name='men_h' value='"+html+"'>");frmTemporalExcPgm.action=pgm;if($("#"+formS).html()!==""&&$("#"+formS).html()!==undefined){$("#frmTemporalExcPgm").append($("#"+formS).html());}
frmTemporalExcPgm.target="_self";if(targ=="_blank"){frmTemporalExcPgm.target=targ;}
if(pgm.toUpperCase()=='JNTLOGIN.PGM'){if(frmTemporalExcPgm.mod_h.value!=='WMODLITE'&&frmTemporalExcPgm.mod_h.value!=='WMODSRV'){frmTemporalExcPgm.mod_h.value='';}}
frmTemporalExcPgm.submit();}
function excAjax(strURL,strParm,asyncro){strURL=strURL+".pgm";stringPar="app_h="+parseCookie(TheCookieValue,1)+"&mod_h="+parseCookie(TheCookieValue,2)+"&per_h="+parseCookie(TheCookieValue,3)+"&ses_h="+parseCookie(TheCookieValue,4)+"&cta_h="+parseCookie(TheCookieValue,5)+"&usu_h="+parseCookie(TheCookieValue,6)+"&ajax=1&"+strParm;respuesta="";if(asyncro=="async"){asyncro=true;}
else{asyncro=false;}
$.ajax({async:asyncro,type:"POST",url:strURL,data:stringPar,success:function(response){response=UTF8.decode(response);respuesta=response;},beforeSend:function(){},error:function(objXMLHttpRequest){alert("Problema con conexión, Reintente mas tarde");}});return respuesta;}
function cerrarW(){excPgm('JNTLogin');}
function permiteNum(evt){var evento=evt||window.event;var key=evento.keyCode||evento.which;return(key<=13||(key>=48&&key<=57)||key==44);}
function validaAlf(info){info=info.toUpperCase()
for(var i=0;i<info.length;i++){var1=info.charAt(i);if(var1.search("AÁBCDEÉFGHIÍJKLMNÑñOÓPQRSTUÚÜVWXYZ")<0){return false;}}
return true;}
function rmvEdit(toremoveEdit){for(var i=0;i<toremoveEdit.length;i++){if(toremoveEdit.substring(i,i+1)!=="0"&&toremoveEdit.substring(i,i+1)!=="1"&&toremoveEdit.substring(i,i+1)!=="2"&&toremoveEdit.substring(i,i+1)!=="3"&&toremoveEdit.substring(i,i+1)!=="4"&&toremoveEdit.substring(i,i+1)!=="5"&&toremoveEdit.substring(i,i+1)!=="6"&&toremoveEdit.substring(i,i+1)!=="7"&&toremoveEdit.substring(i,i+1)!=="8"&&toremoveEdit.substring(i,i+1)!=="9"&&toremoveEdit.substring(i,i+1)!=="."&&toremoveEdit.substring(i,i+1)!=="-"&&toremoveEdit.substring(i,i+1)!==""){toremoveEdit=toremoveEdit.replace(toremoveEdit.substring(i,i+1),"");i-=1;}}
if(toremoveEdit==""){toremoveEdit="0";}
return toremoveEdit;}
function rmvEditXX(toremoveEdit){negativo=false;if(toremoveEdit.substring(0,1)=="-"||toremoveEdit.substring(toremoveEdit.length,1)=="-"){negativo=true;}
toremoveEdit=fnTrim(toremoveEdit);for(var i=0;i<toremoveEdit.length;i++){if(toremoveEdit.substring(i,i+1)!=="0"&&toremoveEdit.substring(i,i+1)!=="1"&&toremoveEdit.substring(i,i+1)!=="2"&&toremoveEdit.substring(i,i+1)!=="3"&&toremoveEdit.substring(i,i+1)!=="4"&&toremoveEdit.substring(i,i+1)!=="5"&&toremoveEdit.substring(i,i+1)!=="6"&&toremoveEdit.substring(i,i+1)!=="7"&&toremoveEdit.substring(i,i+1)!=="8"&&toremoveEdit.substring(i,i+1)!=="9"&&toremoveEdit.substring(i,i+1)!=="."&&toremoveEdit.substring(i,i+1)!==","){toremoveEdit=toremoveEdit.replace(toremoveEdit.substring(i,i+1),"");i-=1;}
toremoveEdit=parseFloat(toremoveEdit);if(negativo){toremoveEdit=toremoveEdit*-1;}}
if(toremoveEdit==""){toremoveEdit="0";}
return toremoveEdit;}
function fnTrim(s){s=s.replace(/\s+/gi,' ');s=s.replace(/^\s+|\s+$/gi,'');return s;}
function chgTimeFmt(hora){if(parseInt(hora.substring(0,2))>11){hora=hora.substring(0,2)+':'+hora.substring(3,5)+' p.m.';}
else{hora=hora.substring(0,2)+':'+hora.substring(3,5)+' a.m.';}
if(parseInt(hora.substring(0,2))>12){if(parseInt(hora.substring(0,2))-12<10){hora='0'+(parseInt(hora.substring(0,2))-12)+hora.substring(2);}
else{hora=(parseInt(hora.substring(0,2))-12)+hora.substring(2);}}
if(parseInt(hora.substring(0,2))==00){hora='12'+':'+hora.substring(3);}
return hora;}
function fnCheckdate(y,m,d){return m>0&&m<13&&y>0&&y<32768&&d>0&&d<=(new Date(y,m,0)).getDate();}
function fnValidarEmail(email){expr=/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;return expr.test(email);}
function fnSustVal(variable,TReempl){valor=variable.value;valor=(fnTrim(valor)).toUpperCase();valor=valor.replace("Á","A");valor=valor.replace("É","E");valor=valor.replace("Í","I");valor=valor.replace("Ó","O");valor=valor.replace("Ú","U");valor=valor.replace("Ä","A");valor=valor.replace("Ë","E");valor=valor.replace("Ï","I");valor=valor.replace("Ö","O");valor=valor.replace("Ü","U");if(TReempl=='9'){alerta="No se Permiten caracteres que no sean numéricos";}
if(TReempl=='X'){alerta="No se Permiten caracteres que no sean alfabéticos";}
if(TReempl=='X9'){alerta="No se Permiten caracteres que no sean alfabéticos o numéricos";}
if(fnChkSCh(valor,TReempl)){alert(alerta);valor=fnChangeChEsp(valor,TReempl);setTimeout(function(){$("#"+variable.id).focus();$("#"+variable.id).select();},1)}
return valor;}
function fnChkSCh(info,TReempl){info=(fnTrim(info)).toUpperCase();if(TReempl=='9'){sting="1234567890";}
if(TReempl=='X'){sting=" AÁBCDEÉFGHIÍJKLMNÑñOÓPQRSTUÚÜVWXYZ";}
if(TReempl=='X9'){sting=" AÁBCDEÉFGHIÍJKLMNÑñOÓPQRSTUÚÜVWXYZ1234567890";}
for(var i=0;i<info.length;i++){var1=info.charAt(i);try{if(sting.search(var1)<0||sting.search(var1)>=sting.length||var1=="|"||var1=="."||var1=="^"){return true;}}
catch(e){return true;}}
return false;}
function fnChangeChEsp(info,TReempl){info=(fnTrim(info)).toUpperCase();info=info.replace("Á","A");info=info.replace("É","E");info=info.replace("Í","I");info=info.replace("Ó","O");info=info.replace("Ú","U");info=info.replace("Ä","A");info=info.replace("Ë","E");info=info.replace("Ï","I");info=info.replace("Ö","O");info=info.replace("Ü","U");if(TReempl=='9'){sting="1234567890";}
if(TReempl=='X'){sting=" AÁBCDEÉFGHIÍJKLMNÑñOÓPQRSTUÚÜVWXYZ";}
if(TReempl=='X9'){sting=" AÁBCDEÉFGHIÍJKLMNÑñOÓPQRSTUÚÜVWXYZ1234567890";}
for(var i=0;i<info.length;i++){var1=info.charAt(i);try{if(sting.search(var1)<0||sting.search(var1)>=sting.length||var1=="|"||var1=="."||var1=="^"){info=info.replace(var1,'');i--;}}
catch(e){info=info.replace(var1,'');i--;}}
return fnTrim(info);}
function fnValStrTelef(cadena){alerta='';if(cadena.length<10&&cadena.length!==0){alerta+='Digita un teléfono de 10 números.\n';}
if(fnChkSCh(cadena,'9')){alerta+='Sólo son válidos números.\n';}
if(cadena.charAt(0)=='0'){alerta+='El primer dígito no debe ser cero.\n';}
suma=0;for(var z=0;z<10;z++){for(var y=2;y<cadena.length;y++){if(cadena.charAt(y)==z){suma+=1;if(suma>=6){alerta+='El Teléfono no debe tener 6 o más números repetidos.\n';y=cadena.length;}}
else{suma=0;}}
suma=0;}
secuencia='01234567890123456789';for(var i=0;i<10;i++){stringF=secuencia.substr(i,6);if(cadena.indexOf(stringF)>0){alerta+='Teléfono con secuencia de dígitos incorrecta.\n';i=10;}}
secuencia='98765432109876543210';for(var i=0;i<10;i++){stringF=secuencia.substr(i,6);if(cadena.indexOf(stringF)>0){alerta+=' Teléfono con secuencia de dígitos incorrecta.\n';i=10;}}
return alerta;}
function fnDspWinPdf(url,titu,wid,hei){if(isNaN(parseInt(hei))){hei=450;}
$("#msgWindow").remove();newValWin='<div class="modal fade cpop" id="msgWindow" role="dialog" data-backdrop="static" data-keyboard="false">'+'<div class="modal-dialog" style="margin-top: 0px;">'+'<div class="modal-content">'+'<div class="modal-header">'+'<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">x</span></button>'+'<h4 class="modal-title" id="myModalLabel">'+titu+'</h4>'+'</div>'+'<div class="modal-body light">'+'<div>'+'<iframe src="'+url+'" frameborder="0" style="width: 100%; height: '+hei+'px;"></iframe>'+'</div>'+'</div>'+'</div>'+'</div>'+'</div>';$('body').append(newValWin);$("#anLnkMsg").trigger("click");}
function fnOpnDoc(prmDocId){prmAjax='frmAction=DspDoc&frmDocId='+prmDocId;respAjax=excAjax('JntDwnDoc',prmAjax,'sync');if(respAjax.substr(0,5)=='Error'){alert(respAjax);return false;}
window.open(respAjax,"_blank");prmAjax='frmAction=RmvDoc&frmTmpDoc='+respAjax;setTimeout(function(){respAjax=excAjax('JntDwnDoc',prmAjax,'sync');},1000);}
function isNumber(evt){evt=(evt)?evt:window.event;var charCode=(evt.which)?evt.which:evt.keyCode;if(charCode>31&&(charCode<48||charCode>57)){return false;}
return true;}
Number.prototype.formatMoney=function(decPlaces,thouSeparator,decSeparator){var n=this,decPlaces=isNaN(decPlaces=Math.abs(decPlaces))?2:decPlaces,decSeparator=decSeparator==undefined?".":decSeparator,thouSeparator=thouSeparator==undefined?",":thouSeparator,sign=n<0?"-":"",i=parseInt(n=Math.abs(+n||0).toFixed(decPlaces))+"",j=(j=i.length)>3?j%3:0;return sign+(j?i.substr(0,j)+thouSeparator:"")+i.substr(j).replace(/(\d{3})(?=\d)/g,"$1"+thouSeparator)+(decPlaces?decSeparator+Math.abs(n-i).toFixed(decPlaces).slice(2):"");};UTF8={encode:function(s){for(var c,i=-1,l=(s=s.split("")).length,o=String.fromCharCode;++i<l;s[i]=(c=s[i].charCodeAt(0))>=127?o(0xc0|(c>>>6))+o(0x80|(c&0x3f)):s[i]);return s.join("");},decode:function(s){for(var a,b,i=-1,l=(s=s.split("")).length,o=String.fromCharCode,c="charCodeAt";++i<l;((a=s[i][c](0))&0x80)&&(s[i]=(a&0xfc)==0xc0&&((b=s[i+1][c](0))&0xc0)==0x80?o(((a&0x03)<<6)+(b&0x3f)):o(128),s[++i]=""));return s.join("");}};