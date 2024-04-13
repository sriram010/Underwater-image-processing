import axios from "axios";
import { useState } from "react";
import { TailSpin } from "react-loader-spinner";

const App = () => {
  const [image, setImage] = useState(null);
  const [name, setName] = useState("");
  const [processedImage, setProcessedImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadImage = async (e) => {
    setProcessedImage("");
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
    setLoading(true);
    try {
      const res = await axios.get(`http://localhost:3000/${name}`);
      console.log(res);
      setProcessedImage(res.data.path);
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="h-fit pb-20">
      <div className="flex w-full text-center justify-center ">
        <div className="text-5xl mt-20">Underwater Image Enhancement</div>
      </div>
      <p className="text-center mx-60 my-16 text-gray-400">
      Unlock the beauty of the ocean depths! Upload your underwater image for our advanced enhancement. Our algorithms reveal vivid colors and intricate details, breathing life into your underwater memories. Experience the majesty of marine life and pristine waters as never before. Dive into your memories and let us transform them into breathtaking masterpieces. Begin your underwater journey now!
      </p>
      <div className="mx-auto text-center flex gap-12 justify-center">
        <input
          className="bg-white text-black rounded-full file:bg-[#0f172a] px-[2px] file:w-[8em] file:my-[2px] file:mr-[12px] file:placeholder:text-black file:py-2 file:rounded-full file:text-white"
          onChange={uploadImage}
          type="file"
          name=""
          id=""
        />
        <button className="px-10 py-3 bg-[#0ea5e9] text-black rounded-full hover:shadow-black shadow-md" onClick={processImage}>
          PROCESS
        </button>
      </div>
      <div className="w-[75vw] h-fit bg-[#1e293b] mx-auto rounded-2xl mt-16 border-[1px] border-gray-700">
        <table className="w-full rounded-t-2xl">
          <thead className="bg-[#293548]">
            <th className="p-5 rounded-tl-2xl">Original Image</th>
            <th className="p-5 rounded-tr-2xl">Processed Image</th>
          </thead>
          <tbody className="h-full">
            <tr>
              <td className="px-4 w-[40em] h-[28em] py-6"> {image && <img className="w-[35em] mx-auto" src={image} alt="uploaded" />}</td>
              <td className="px-4 w-[40em] h-[28em] py-6">
                {processedImage ? (
                  <img className="w-[35em] mx-auto" src={"/processed_image.png"} alt="uploaded" />
                ) : (
                  loading && (
                    <div className="flex justify-center items-center"> 
                      <TailSpin visible={true} height="60" width="60" color="#0ea5e9" ariaLabel="tail-spin-loading" radius="1" wrapperStyle={{}} wrapperClass="" />
                    </div>
                  )
                )}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default App;