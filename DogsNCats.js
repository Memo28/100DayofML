import "./styles.css";
import * as tf from "@tensorflow/tfjs";
import * as DogsNCats from "dogs-n-cats";
DogsNCats.load().then(dnc => {
  const [cat, catLabel] = dnc.training.get();
  cat.print();

  document.getElementById("app").innerHTML = `
    <h1>${["dog", "cat"][catLabel.dataSync()]}</h1>
    <canvas id="printCanvas"/>
    `;

  const printCanvas = document.getElementById("printCanvas");
  tf.browser.toPixels(cat, printCanvas);
});
