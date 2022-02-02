
class Saliency:
    def __init__(self):
        pass

  def SpectralResidual(self, image):
        imgName = image.split('.')[0]
        img = cv2.imread(image)
        saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
        (success, saliencyMap) = saliency.computeSaliency(img)
        saliencyMap = (saliencyMap * 255).astype("uint8")

        out_name = "./outputs/" + 'SpectralResidual_' + imgName + ".jpg"
        cv2.imwrite(out_name, saliencyMap)

        SpectralResidual_keyframeSize = os.path.getsize(out_name)
        os.remove(out_name)
        return SpectralResidual_keyframeSize

    def SaliencyFineGrained(self, image):
        imgName = image.split('.')[0]
        img = cv2.imread(image)
        saliency = cv2.saliency.StaticSaliencyFineGrained_create()
        (success, saliencyMap) = saliency.computeSaliency(img)

        out_name = "SaliencyFineGrained_" + imgName + ".jpg"
        cv2.imwrite(out_name, saliencyMap)

        SaliencyFineGrained_keyframeSize = os.path.getsize(out_name)
        os.remove(out_name)
        return SaliencyFineGrained_keyframeSize
