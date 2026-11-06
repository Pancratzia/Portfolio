/* Pancratzia studio: curved project gallery, ASCII portrait and clear contact. */
(()=>{'use strict';
const es=document.documentElement.lang==='es';
const menu=document.querySelector('.s-menu'),nav=document.getElementById('studio-navigation');
function setMenu(open){menu?.setAttribute('aria-expanded',String(open));nav?.classList.toggle('is-open',open);menu?.setAttribute('aria-label',es?(open?'Cerrar menú':'Abrir menú'):(open?'Close menu':'Open menu'));}
menu?.addEventListener('click',()=>setMenu(menu.getAttribute('aria-expanded')!=='true'));
nav?.addEventListener('click',e=>{if(e.target.closest('a'))setMenu(false);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu?.getAttribute('aria-expanded')==='true'){setMenu(false);menu.focus();}});
document.addEventListener('click',e=>{if(!e.target.closest('.s-nav'))setMenu(false);});
document.querySelectorAll('[data-copy-email]').forEach(button=>button.addEventListener('click',async()=>{const status=button.parentElement.querySelector('.s-copy-status');try{await navigator.clipboard.writeText('me@pancratzia.com');status.textContent=es?'Correo copiado.':'Email copied.';if(window.gtag)gtag('event','copy_email',{contact_method:'copy'});}catch{status.textContent='me@pancratzia.com';}}));
const compose=document.querySelector('.s-compose');
document.querySelectorAll('[data-brief]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-brief]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));const subject=(es?'Proyecto: ':'Project: ')+button.dataset.brief;const body=es?'Hola Laura,\n\nMe interesa: '+button.dataset.brief+'.\n\nMi negocio / sitio actual:\nLo que necesito:\nFechas que tengo en mente:\n\nGracias.':'Hi Laura,\n\nI’m interested in: '+button.dataset.brief+'.\n\nMy business / current website:\nWhat I need:\nDates I have in mind:\n\nThank you.';if(compose)compose.href='mailto:me@pancratzia.com?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);}));
const service=new URLSearchParams(location.search).get('service');if(service){const index=service==='agency'?3:/cms|localization/.test(service)?2:/migration|rebuild/.test(service)?1:0;document.querySelectorAll('[data-brief]')[index]?.click();}
document.querySelectorAll('.s-button,.s-text-link,.s-email').forEach(link=>link.addEventListener('click',()=>{const href=link.getAttribute('href')||'';if(/contact|mailto:/.test(href)&&window.gtag)gtag('event','project_contact_click',{link_url:href,link_text:link.textContent.trim(),language:es?'es':'en'});}));
const reduced=()=>matchMedia('(prefers-reduced-motion: reduce)').matches||document.body.classList.contains('reduce-motion');
const stage=document.querySelector('.s-reel-stage');
if(stage){
 const cards=[...stage.querySelectorAll('.s-reel')];let width=0,height=0,pitch=0,offset=0,velocity=0,last=0,drag=false,dragged=false,pause=false,startX=0,lastX=0,lastTime=0,inView=true,frame=0;
 const pauseButton=document.querySelector('[data-reel="pause"]');
 function resize(){width=stage.clientWidth;height=stage.clientHeight;pitch=(width<561?width-52:width<821?480:540)+32;paint();}
 function paint(){const circumference=pitch*cards.length;cards.forEach((card,i)=>{let t=((i*pitch-offset+circumference*10)%circumference);if(t>circumference/2)t-=circumference;const half=Math.max(width/2,340),d=Math.abs(t)/half,w=pitch-32;const ratio=Number(card.dataset.ratio)||4/3,h=w/ratio+68;const x=width/2+t,y=(height-h)/2-18*Math.min(d*d,2);card.style.width=w+'px';card.style.height=h+'px';card.style.transform=`translate3d(${x-w/2}px,${y}px,0) rotate(${Math.max(-4,Math.min(4,t/half*3))}deg)`;card.style.clipPath='none';card.style.zIndex=String(Math.round(20-d));const visible=x+w/2>0&&x-w/2<width;card.tabIndex=visible?0:-1;card.setAttribute('aria-hidden',String(!visible));});}
 function tick(now){const dt=Math.min((now-(last||now))/1000,.05);last=now;if(!drag&&inView&&!document.hidden){if(!reduced()&&!pause){offset+=dt*(width<561?23:36);}if(Math.abs(velocity)>.1){offset+=velocity*dt;velocity*=Math.exp(-4*dt);}}paint();frame=requestAnimationFrame(tick);}
 stage.addEventListener('pointerdown',e=>{if(e.button!==0||e.target.closest('button'))return;drag=true;dragged=false;startX=lastX=e.clientX;lastTime=performance.now();velocity=0;stage.classList.add('is-dragging');});
 stage.addEventListener('pointermove',e=>{if(!drag)return;const now=performance.now();const dx=e.clientX-lastX;const dt=Math.max(8,now-lastTime);if(Math.abs(e.clientX-startX)>7){dragged=true;if(!stage.hasPointerCapture(e.pointerId))stage.setPointerCapture(e.pointerId);}offset-=dx;velocity=-(dx/dt)*1000;lastX=e.clientX;lastTime=now;paint();});
 function end(){drag=false;stage.classList.remove('is-dragging');if(reduced())velocity=0;}
 stage.addEventListener('pointerup',end);stage.addEventListener('pointercancel',end);window.addEventListener('pointerup',end);
 stage.addEventListener('click',e=>{if(dragged){e.preventDefault();e.stopPropagation();dragged=false;}},true);
 stage.addEventListener('dragstart',e=>e.preventDefault());
 document.querySelectorAll('[data-reel]').forEach(b=>b.addEventListener('click',()=>{const action=b.dataset.reel;if(action==='pause'){pause=!pause;b.textContent=pause?'▶':'Ⅱ';b.setAttribute('aria-pressed',String(pause));b.setAttribute('aria-label',es?(pause?'Reanudar galería':'Pausar galería'):(pause?'Resume gallery':'Pause gallery'));}else{offset+=action==='next'?pitch:-pitch;velocity=0;paint();}}));
 cards.forEach(card=>{card.addEventListener('focus',()=>{pause=true;if(pauseButton){pauseButton.setAttribute('aria-pressed','true');pauseButton.textContent='▶';}});});
 if('ResizeObserver'in window)new ResizeObserver(resize).observe(stage);else window.addEventListener('resize',resize);
 if('IntersectionObserver'in window)new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;}).observe(stage);
 resize();frame=requestAnimationFrame(tick);
}
const pre=document.querySelector('[data-ascii]'),source=document.querySelector('.s-ascii-source');
if(pre&&source){function renderPortrait(){try{const cols=76,rows=78,canvas=document.createElement('canvas');canvas.width=cols;canvas.height=rows;const ctx=canvas.getContext('2d',{willReadFrequently:true});ctx.drawImage(source,0,0,cols,rows);const data=ctx.getImageData(0,0,cols,rows).data;const chars=' .,:;i1tfLCG08@';let output='';for(let y=0;y<rows;y++){for(let x=0;x<cols;x++){const k=(y*cols+x)*4;const alpha=data[k+3]/255;const lum=(data[k]*.299+data[k+1]*.587+data[k+2]*.114)/255;output+=alpha<.12?' ':chars[Math.min(chars.length-1,Math.floor((1-lum)*alpha*(chars.length-1)))];}output+='\n';}pre.textContent=output;}catch{pre.textContent='[ P A N C R A T Z I A ]\n\n  DESIGN + DEVELOPMENT\n\n        *\n       ***\n    *********\n       ***\n        *\n\n  IDEAS INTO WEBSITES';}}if(source.complete)renderPortrait();else source.addEventListener('load',renderPortrait,{once:true});}
})();
