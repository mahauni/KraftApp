const btn = document.getElementById('btn');

const image = document.getElementById('esg-img');

btn.addEventListener('click', async () => {
  // await the promise
  await refreshImage(
    'http://127.0.0.1:5000/esg.png',
  );

  console.log('image is refreshed =)');
});

async function refreshImage(url) {
  await fetch(url, {cache: 'reload', mode: 'no-cors'});

  document
    .querySelectorAll(`img[src='${url}']`)
    .forEach(img => (img.src = url));

  console.log('image refreshed succesfully');
}