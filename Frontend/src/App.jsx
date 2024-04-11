import axios from "axios";
import { useState } from "react";

const App = () => {
  const [image, setImage] = useState(null);
  const [name, setName] = useState("");
  const [processedImage, setProcessedImage] = useState(null);

  const uploadImage = async (e) => {
    setProcessedImage(null)
    const file = e.target.files[0];
    setName(file.name);
    setImage(URL.createObjectURL(file));
    const formData = new FormData();
    formData.append("image", file);
    try {
      const res = await axios.post("http://localhost:3000/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      console.log(res);
    } catch (err) {
      console.log(err);
    }
  };

  const processImage = async () => {
    try {
      const res = await axios.get(`http://localhost:3000/${name}`);
      console.log(res);
      setProcessedImage("/processed_image.png");
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <>
      <div className="flex w-full text-center justify-center ">
        <div className="text-5xl mt-20">Underwater Image Enhancement</div>
      </div>
      <p className="text-center mx-40 my-16">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias sequi accusamus dolorum corrupti sunt quia reprehenderit earum eum adipisci accusantium, quisquam
        consequatur eveniet quidem doloribus ex vero nihil itaque neque possimus. Nostrum, impedit dolore quibusdam fugit, voluptates repellat unde quae maxime odio quis, minima
        eveniet quas blanditiis iure harum tempora!
      </p>
      <div className="mx-auto text-center flex gap-20 justify-center">
        <input className="bg-blue-400 p-4 rounded-lg" onChange={uploadImage} type="file" name="" id="" />
        <button className="p-4 bg-green-500 text-black font-bold rounded-lg" onClick={processImage}>
          PROCESS
        </button>
      </div>
      <div className="flex justify-evenly mx-20">
        {image && (
          <div className="flex w-full text-center justify-center">
            <img className="mt-16" src={image} alt="uploaded" />
          </div>
        )}
        {processedImage && (
          <div className="flex w-full text-center justify-center">
            <img className="mt-16" src={processedImage} alt="processed" />
          </div>
        )}
      </div>
    </>
  );
};

export default App;
