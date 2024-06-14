package Adapter_Pattern;

public class WebAdapter implements WebRequester {
    private WebService service ;
    public void connect (WebService currentService){
        this.service = currentService;

    }

    public int request (Object request){
        Json result = this.toJson(request);
    }
}
